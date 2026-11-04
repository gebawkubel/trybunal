#!/usr/bin/env python3
"""Symulacja negocjacji o TK (issue #46, etapy 3 i 4): skrypt rozmowy i arbitra.

Tryby:
  zbuduj    skleja teksty (pakiet, warianty, karty, arbiter), sprawdza sumy SHA-256
            oryginałów z etapu 2 i zapisuje sumy gotowych tekstów; bez API.
  policz    mierzy wielkość tekstów endpointem messages.count_tokens (bez generowania).
  proba     przebieg na atrapie modelu: kolejność, limity, zapis, limit kosztu;
            usage atrapy pochodzi z modelu bufora i z pomiaru tokenów, więc wynik
            jest szacunkiem kosztu prawdziwego przebiegu przy podanych założeniach.
  przebieg  płatny przebieg (messages.stream). Wymaga --potwierdzam-koszt.

Klucz API jest czytany wyłącznie ze zmiennej środowiskowej o nazwie podanej w
--zmienna-klucza i przekazywany jawnie do klienta. Nie trafia do zapisu.
Opis reguł: README.md w tym katalogu.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WERSJA_PAKIETU = "70b735a"  # numery linii pakietu odnoszą się do tej wersji
ETAP2 = "badania/symulacja/etap-2"
STAN_WIEDZY = "2026.11.04"

# --- Cennik (USD za 1 mln tokenów) -------------------------------------------
# Źródło: https://platform.claude.com/docs/en/about-claude/pricing, sprawdzone 2026.11.04.
# Przed płatnym przebiegiem operator sprawdza cennik i podaje datę w --cennik-sprawdzony.
CENNIK = {
    "claude-opus-5-5": {"wejscie": 4.00, "zapis_5m": 5.00, "zapis_1h": 8.00,
                        "odczyt": 0.20, "wyjscie": 20.00},
}
CENNIK_ZRODLO = "https://platform.claude.com/docs/en/about-claude/pricing"
CENNIK_DATA = "2026.11.04"

# --- Skład W5 (etap 4; przebieg 1 miał skład W1, wersja skryptu z commita e28858b) ---
POSTACIE = [  # kolejność otwarcia z arbiter.md, część 2
    ("nawrocki", "Karol Nawrocki"),
    ("tusk", "Donald Tusk"),
    ("kaczynski", "Jarosław Kaczyński"),
    ("czarzasty", "Włodzimierz Czarzasty"),
    ("swieczkowski", "Bogdan Święczkowski"),
    ("korwin-piotrowska", "Anna Korwin-Piotrowska"),
]
NAZWA = dict(POSTACIE)
PODPIS_ARBITRA = "Arbiter (agent AI, nie negocjuje)"


def podpis(klucz: str) -> str:
    return f"{NAZWA[klucz]} (postać symulowana przez AI)"


# --- Limity z arbiter.md, część 2 ----------------------------------------------
RUNDY_DYSKUSJI = 8
LIMIT_POZA_KOLEJNOSCIA = 8   # najwyżej raz na rundę dyskusji
LIMIT_WYPOWIEDZI = 80        # 6 + 48 + 8 + 6 + 6 + 6
LIMIT_TOKENOW_WYPOWIEDZI = 1400

# --- Pakiet wiedzy (pakiet-wiedzy.md, części 2-4) --------------------------------
# Wycięcia: (nr linii, rodzaj, tekst). "od": usuń od tekstu do końca linii;
# "usun": usuń dokładnie ten tekst; "linia": usuń całą linię zaczynającą się od tekstu.
CIECIA = {
    "historia-sporu.md": [
        (11, "od", " Według naszej analizy, gdyby nie ten przepis"),
        (15, "od", " Według naszej analizy to był krok, od którego zależało najwięcej"),
        (26, "od", " Według naszej analizy to był drugi, poważniejszy błąd"),
        (40, "od", " Według naszej analizy to był trzeci krok"),
        (72, "usun", "[kto odpowiada za kryzys](badania/odpowiedzialnosc-i-rozwiazania.md), "),
    ],
    "badania/scenariusze-naprawy.md": [
        (3, "usun", " Dodaliśmy też scenariusze, które wskazały niezależne analizy modeli AI,"
                    " choć nikt z polityków ich nie proponuje."),
        (81, "usun", " Recenzenci obu analiz AI wskazali wyroki ETPC Baka przeciwko Węgrom i"
                     " Grzęda przeciwko Polsce o przedwczesnym usuwaniu sędziów."),
        (90, "linia", "- **Uwaga z analiz AI:**"),
    ],
}
KONSTYTUCJA_PODST = [(112, 114), (122, 125), (463, 466), (524, 530), (631, 645), (657, 662),
                     (668, 671), (698, 708), (730, 731), (759, 797), (860, 879), (1021, 1076),
                     (1197, 1198), (1252, 1259)]
KONSTYTUCJA_MIN = [(524, 530), (631, 645), (877, 879), (1032, 1048), (1056, 1066),
                   (1197, 1198), (1252, 1259)]
SCENARIUSZE = [(1, 123), (142, 169), (188, 196)]
CALOSC = None  # cały plik

PAKIETY = {
    "podstawowy": [
        ("zrodla/konstytucja.md", KONSTYTUCJA_PODST),
        ("badania/sily-i-glosy.md", CALOSC),
        ("badania/warunki-rozwiazan.md", CALOSC),
        ("historia-sporu.md", [(1, 72)]),
        ("badania/okres-2024-2026.md", [(1, 43)]),
        ("badania/zgromadzenie-2026-11-03.md", [(1, 80), (85, 91)]),
        ("badania/postepowania-wobec-osob.md", [(1, 70)]),
        ("badania/skutki-dla-obywateli.md", [(1, 63)]),
        ("badania/wyroki-europejskie.md", [(1, 66)]),
        ("zrodla/glosowania-tk-2015-2026.md", [(15, 30)]),
        ("badania/scenariusze-naprawy.md", SCENARIUSZE),
        ("badania/propozycje-na-stole.md", CALOSC),
        ("badania/komisja-2026-04-28.md", [(1, 5), (18, 111), (128, 137)]),
        ("badania/bosak-2026-11-04.md", [(1, 64)]),
    ],
    "minimalny": [
        ("zrodla/konstytucja.md", KONSTYTUCJA_MIN),
        ("badania/sily-i-glosy.md", CALOSC),
        ("badania/warunki-rozwiazan.md", CALOSC),
        ("badania/okres-2024-2026.md", [(1, 43)]),
        ("badania/postepowania-wobec-osob.md", [(1, 70)]),
        ("zrodla/glosowania-tk-2015-2026.md", [(15, 30)]),
        ("badania/scenariusze-naprawy.md", SCENARIUSZE),
        ("badania/propozycje-na-stole.md", CALOSC),
        ("badania/komisja-2026-04-28.md", [(128, 137)]),
        ("badania/bosak-2026-11-04.md", [(57, 64)]),
    ],
}
KARTY_ZRODEL = [f"zrodla/okres-2024-2026/{n}.md" for n in (
    "rbn-2026-11-03 premier-2026-11-03 psl-reset-2026-11-03 konfederacja-reset-2026-10-31 "
    "konfederacja-po-rbn-2026-11-03 bosak-polsat-2026-11-04 rozwoj-plus-trybunal-2026 "
    "zandberg-po-spotkaniu-2026-10-31 zandberg-po-rbn-2026-11-03 hfpc-zarzad-2026-10-31 "
    "batory-zalasinski-2026 kj-29-warunkow dudek-2026-11-01 komunikat-31-pazdziernika "
    "zarzadzenie-przerwy-2026 zarzadzenie-2-2026 etpc-17392-26 kpt-1-26 k-3-26 kp-3-24 u-5-24 "
    "uchwala-sejmu-2026-299 uchwala-sejmu-2024-198 pk-immunitety-2026 pk-immunitet-2025 "
    "pk-uchwala-zo-2025 pk-sledztwo-niedopuszczenie pk-napasc-2026-11-03 "
    "tk-postepowanie-trojga-sedziow uchwala-kolegium-sn oswiadczenie-zo-sn sn-ii-zz-2-26 "
    "senat-sklad-2026-11 komisja-wenecka-2024 slubowanie-patyry berek-sejm informacja-tk-2024 "
    "senat-druk-55 druki-253-254 druk-166-2015 km-xero-flor-2024-2026 tsue-c-448-23").split()]
KARTY_ZRODEL.append("zrodla/xero-flor.md")

# --- Teksty techniczne skryptu (jawne, wchodzą do sum SHA-256) -------------------
PAKIET_WSTEP = (f"Pakiet wiedzy, wspólny dla wszystkich uczestników symulacji. Stan wiedzy: "
                f"{STAN_WIEDZY}. Linki w tekście są tylko adresami źródeł; nie masz do nich dostępu.")
ZRODLA_WSTEP = ("Karty źródeł (widzi je tylko arbiter; na prośbę postaci arbiter może odczytać "
                "z nich dosłowny fragment).")
WATEK_NAGLOWEK = ("Zapis rozmowy przy stole od początku do tej chwili. Każda wypowiedź zaczyna się "
                  "oznaczeniem rundy i podpisem mówiącego.")
KARTA_NAGLOWEK = "Twoja karta prywatna (widzisz ją tylko Ty):"
TURA = {
    "otwarcie": "Runda otwarcia. Teraz mówi {imie}, czyli Ty. Napisz jedną wypowiedź.",
    "dyskusja": "Runda dyskusji {n} z {max}. Teraz mówi {imie}, czyli Ty. Napisz jedną wypowiedź.",
    "poza_kolejnoscia": ("Runda dyskusji {n} z {max}. Arbiter udzielił głosu poza kolejnością "
                         "Tobie ({imie}), bo w tej rundzie wezwano Cię do odpowiedzi. "
                         "Napisz jedną wypowiedź."),
    "dodatkowa": ("Dodatkowa runda dyskusji przed powtórnym głosowaniem. Teraz mówi {imie}, "
                  "czyli Ty. Napisz jedną wypowiedź."),
    "glosowanie": ("{nazwa_rundy}. Pakiety do głosowania, w tej kolejności: {pakiety} (opis w "
                   "ostatniej wypowiedzi arbitra). Teraz głosuje {imie}, czyli Ty: dla każdego "
                   "pakietu po kolei napisz krótko \"za\" albo \"przeciw\", co deklarujesz i jakie masz "
                   "zastrzeżenia, bez powtarzania treści pakietu."),
}
ARBITER_FORMAT = (
    "Wiadomość techniczna skryptu. Odpowiadasz obiektem JSON zgodnym ze schematem, który jest "
    "taki sam przy każdym Twoim wywołaniu. Pole \"tekst\" to Twoja wypowiedź do zapisu rozmowy. "
    "Pola \"decyzja\", \"poza_kolejnoscia\", \"pakiety\" i \"wynik\" to decyzje, które skrypt "
    "wykonuje. W danej chwili dozwolone są tylko wartości wymienione niżej; pole, którego zdanie "
    "niżej nie wymienia, wypełniasz wartością \"nie_dotyczy\" (pole \"pakiety\": pusta lista). "
    "Skrypt sprawdza wartości i pilnuje limitów liczbowych.")
ARBITER_TURA = {
    "otwarcie": ("Pierwsza wypowiedź arbitra: otwarcie spotkania, przed rundą otwarcia. "
                 "Kolejność wypowiedzi w tym przebiegu: {kolejnosc}. Pola decyzji: \"nie_dotyczy\"."),
    "po_rundzie": ("Koniec rundy: {nazwa_rundy}. Napisz stan stołu po tej rundzie i zdecyduj, co "
                   "dalej. {informacje} Pole \"decyzja\", dozwolone teraz: {decyzje}. Znaczenie: "
                   "\"dalej\" (następna runda dyskusji), \"glosowanie\" (runda głosowania; w polu "
                   "\"pakiety\" podaj numery pakietów w kolejności głosowania i wymień je w tekście), "
                   "\"brak_porozumienia\". Pole \"poza_kolejnoscia\", dozwolone teraz: {poza}; to "
                   "postać, której udzielasz głosu poza kolejnością, bo w tej rundzie wezwano ją wprost "
                   "do odpowiedzi; mówi zaraz po Twojej wypowiedzi, a jej wypowiedź liczy się do tej "
                   "rundy. Pole \"wynik\": \"nie_dotyczy\"."),
    "po_glosowaniu": ("Koniec rundy: {nazwa_rundy}. Ogłoś wynik według części 6 instrukcji. "
                      "{informacje} Pole \"wynik\", dozwolone teraz: {wyniki}. Znaczenie: "
                      "\"porozumienie\", \"porozumienie_czesciowe\", \"brak_porozumienia\", "
                      "\"dodatkowa_runda\" (jedna dodatkowa runda dyskusji i powtórne głosowanie, gdy "
                      "pakiet przeszedł z zastrzeżeniami, które zmieniają jego treść). Pola "
                      "\"decyzja\" i \"poza_kolejnoscia\": \"nie_dotyczy\"."),
    "przerwanie": ("Skrypt przerywa przebieg: {powod}. Ogłoś brak porozumienia według części 6 "
                   "instrukcji (warunek d): ostatni stan stołu, które progi były najbliżej "
                   "spełnienia i czego zabrakło. Pola decyzji: \"nie_dotyczy\"."),
}
ARBITER_POPRAWKA = ("Poprzednia odpowiedź nie została przyjęta ({blad}). Odpowiedz ponownie, "
                    "z dozwolonymi wartościami.")
ODMOWA_PAS = ("Pas. [Adnotacja skryptu: model nie wygenerował wypowiedzi ({powod}); zgodnie z "
              "regułą skryptu liczy się to jako \"Pas\".]")
UCIECIE = "[Adnotacja skryptu: wypowiedź ucięta po limicie {limit} tokenów.]"
NAGLOWEK_ZAPISU = (
    "# Zapis przebiegu symulacji negocjacji o Trybunał Konstytucyjny\n\n"
    "**To symulacja. Wypowiedzi są generowane przez modele AI grające prawdziwe osoby; nie są "
    "słowami tych osób.** Każda postać i arbiter to osobne wywołanie tego samego modelu. "
    f"Stan wiedzy postaci: {STAN_WIEDZY}. Symulacja nie przewiduje, co zrobią prawdziwi ludzie; "
    "sprawdza, które porozumienia da się złożyć przy podanych założeniach "
    "([issue #46](https://github.com/gebawkubel/trybunal/issues/46)).\n\n")


# =============================================================================
# Teksty
# =============================================================================
def sha(t: str | bytes) -> str:
    return hashlib.sha256(t.encode() if isinstance(t, str) else t).hexdigest()


def git_show(sciezka: str, wersja: str = WERSJA_PAKIETU) -> str:
    return subprocess.run(["git", "show", f"{wersja}:{sciezka}"], cwd=REPO, check=True,
                          capture_output=True).stdout.decode("utf-8")


def oryginal_etapu2(nazwa: str) -> str:
    """Tekst pod linią z pliku etapu 2; sprawdza SHA-256 podany w nagłówku."""
    s = (REPO / ETAP2 / nazwa).read_text(encoding="utf-8")
    m = re.search(r"SHA-256 oryginału: `([0-9a-f]{64})`", s.split("\n", 1)[0])
    if not m:
        raise SystemExit(f"Brak sumy oryginału w nagłówku: {nazwa}")
    tekst = s[s.index("\n---\n\n") + 6:]
    if sha(tekst) != m.group(1):
        raise SystemExit(f"Suma SHA-256 nie zgadza się z nagłówkiem: {nazwa}")
    return tekst


def tnij(sciezka: str, linie: list[str]) -> list[str]:
    linie = list(linie)
    usuniete = set()
    for nr, rodzaj, wzor in CIECIA.get(sciezka, []):
        l = linie[nr - 1]
        if rodzaj == "linia":
            if not l.startswith(wzor):
                raise SystemExit(f"Cięcie nie pasuje: {sciezka}:{nr}")
            usuniete.add(nr - 1)
            continue
        if l.count(wzor) != 1:
            raise SystemExit(f"Cięcie nie pasuje: {sciezka}:{nr}")
        linie[nr - 1] = l[:l.index(wzor)] if rodzaj == "od" else l.replace(wzor, "")
    return [None if i in usuniete else l for i, l in enumerate(linie)]


def fragment(sciezka: str, zakresy) -> tuple[str, str]:
    linie = tnij(sciezka, git_show(sciezka).split("\n"))
    if linie and linie[-1] == "":
        linie = linie[:-1]
    n = len(linie)
    if zakresy is None:
        czesci, opis = [linie], "całość"
    else:
        czesci, opisy = [], []
        for a, b in zakresy:
            if a > n:
                raise SystemExit(f"Zakres poza plikiem: {sciezka} {a}-{b} (plik ma {n} linii)")
            czesci.append(linie[a - 1:min(b, n)])
            opisy.append(f"{a}-{min(b, n)}")
        opis = "linie " + ", ".join(opisy)
    tekst = "\n\n[...]\n\n".join("\n".join(l for l in c if l is not None).strip("\n")
                                 for c in czesci)
    return tekst, opis


def zbuduj_pakiet(nazwa: str) -> str:
    pliki = PAKIETY[nazwa]
    out = [PAKIET_WSTEP]
    for i, (p, z) in enumerate(pliki, 1):
        tekst, opis = fragment(p, z)
        out.append(f"===== Plik {i} z {len(pliki)}: {p}, {opis} (repozytorium w wersji "
                   f"{WERSJA_PAKIETU}) =====\n\n{tekst}")
    return "\n\n".join(out)


def zbuduj_zrodla() -> str:
    out = [ZRODLA_WSTEP]
    for p in KARTY_ZRODEL:
        out.append(f"===== Karta źródła: {p} (repozytorium w wersji {WERSJA_PAKIETU}) =====\n\n"
                   + git_show(p).strip("\n"))
    return "\n\n".join(out)


def warianty() -> dict[str, str]:
    t = oryginal_etapu2("warianty-motywacji.md")
    sekcje = re.split(r"(?m)^(?=## )", t)
    wspolna = next(s for s in sekcje if s.startswith("## Część wspólna")).strip()
    out = {}
    for w in "abc":
        sek = next(s for s in sekcje if s.startswith(f"## Wariant ({w})")).strip()
        out[w] = wspolna + "\n\n" + sek
    return out


def karty() -> dict[str, str]:
    out = {}
    for k, imie in POSTACIE:
        t = oryginal_etapu2(f"karta-{k}.md")
        if not t.startswith(f"# Karta prywatna: {imie}"):
            raise SystemExit(f"Karta nie pasuje do postaci: {k}")
        out[k] = t
    return out


@dataclass
class Teksty:
    wariant: str
    pakiet: str
    karty: dict
    arbiter: str
    zrodla: str
    nazwa_wariantu: str
    nazwa_pakietu: str

    def system_postaci(self) -> str:
        return self.wariant + "\n\n" + self.pakiet

    def system_arbitra(self) -> str:
        czesci = [self.arbiter, self.pakiet] + ([self.zrodla] if self.zrodla else [])
        return "\n\n".join(czesci)

    def sumy(self) -> dict:
        d = {"wariant": sha(self.wariant), "pakiet": sha(self.pakiet),
             "arbiter": sha(self.arbiter), "system_postaci": sha(self.system_postaci()),
             "system_arbitra": sha(self.system_arbitra())}
        if self.zrodla:
            d["karty_zrodel"] = sha(self.zrodla)
        d.update({f"karta_{k}": sha(v) for k, v in self.karty.items()})
        return d


def wczytaj_teksty(wariant: str, pakiet: str, ze_zrodlami: bool) -> Teksty:
    return Teksty(warianty()[wariant], zbuduj_pakiet(pakiet), karty(),
                  oryginal_etapu2("arbiter.md"), zbuduj_zrodla() if ze_zrodlami else "",
                  wariant, pakiet)


def teksty_techniczne() -> dict:
    return {"PAKIET_WSTEP": PAKIET_WSTEP, "ZRODLA_WSTEP": ZRODLA_WSTEP,
            "WATEK_NAGLOWEK": WATEK_NAGLOWEK, "KARTA_NAGLOWEK": KARTA_NAGLOWEK,
            **{f"TURA.{k}": v for k, v in TURA.items()}, "ARBITER_FORMAT": ARBITER_FORMAT,
            **{f"ARBITER_TURA.{k}": v for k, v in ARBITER_TURA.items()},
            "ARBITER_POPRAWKA": ARBITER_POPRAWKA, "SCHEMAT_ARBITRA": json.dumps(
                SCHEMAT_ARBITRA, ensure_ascii=False, sort_keys=True),
            "ODMOWA_PAS": ODMOWA_PAS, "UCIECIE": UCIECIE, "NAGLOWEK_ZAPISU": NAGLOWEK_ZAPISU}


# =============================================================================
# Budowa zapytań
# =============================================================================
def cc(ttl: str) -> dict:
    return {"type": "ephemeral", "ttl": ttl} if ttl == "1h" else {"type": "ephemeral"}


@dataclass
class Wpis:
    nr: int
    rola: str          # klucz postaci albo "arbiter"
    runda: str         # opis rundy do zapisu
    tekst: str

    def blok(self) -> str:
        kto = PODPIS_ARBITRA if self.rola == "arbiter" else podpis(self.rola)
        return f"[{self.runda}] {kto}:\n\n{self.tekst}"


def bloki_watku(watek: list[Wpis], ttl: str) -> list[dict]:
    bloki = [{"type": "text", "text": WATEK_NAGLOWEK}] + [
        {"type": "text", "text": w.blok()} for w in watek]
    bloki[-1] = dict(bloki[-1], cache_control=cc(ttl))
    return bloki


def przepis_watku(watek: list[Wpis]) -> dict:
    return {"wpisy_watku": len(watek),
            "sha256_wpisow": sha("\n\n".join(w.blok() for w in watek))}


def zapytanie_postaci(t: Teksty, klucz: str, watek: list[Wpis], tura: str, uklad: str,
                      ttl: str) -> dict:
    """Zwraca zapytanie i jego przepis (z czego się składa, z sumami SHA-256)."""
    karta = f"{KARTA_NAGLOWEK}\n\n{t.karty[klucz]}"
    przepis = {"uklad": uklad, "system_postaci": sha(t.system_postaci()), "karta": klucz,
               "sha256_karty": sha(t.karty[klucz]), **przepis_watku(watek), "tura": tura}
    if uklad == "wspolny-watek":
        # wariant + pakiet (wspólne) | wątek (wspólny dla postaci) | karta i tura (prywatne)
        system = [{"type": "text", "text": t.system_postaci(), "cache_control": cc(ttl)}]
        messages = [{"role": "user", "content": bloki_watku(watek, ttl)},
                    {"role": "system", "content": f"{karta}\n\n{tura}"}]
    else:  # "etap2": wariant, pakiet, karta, wątek (kolejność z pakiet-wiedzy.md, część 6)
        system = [{"type": "text", "text": t.system_postaci(), "cache_control": cc(ttl)},
                  {"type": "text", "text": karta, "cache_control": cc(ttl)}]
        messages = [{"role": "user", "content": bloki_watku(watek, ttl)},
                    {"role": "system", "content": tura}]
    return {"system": system, "messages": messages}, przepis


def zapytanie_arbitra(t: Teksty, watek: list[Wpis], tura: str, ttl: str) -> dict:
    system = [{"type": "text", "text": t.system_arbitra(), "cache_control": cc(ttl)}]
    messages = [{"role": "user", "content": bloki_watku(watek, ttl)},
                {"role": "system", "content": f"{ARBITER_FORMAT}\n\n{tura}"}]
    przepis = {"system_arbitra": sha(t.system_arbitra()), **przepis_watku(watek),
               "format": ARBITER_FORMAT, "tura": tura}
    return {"system": system, "messages": messages}, przepis


NIE_DOTYCZY = "nie_dotyczy"
DECYZJE = ["dalej", "glosowanie", "brak_porozumienia"]
WYNIKI = ["porozumienie", "porozumienie_czesciowe", "brak_porozumienia", "dodatkowa_runda"]
# Jeden stały schemat dla wszystkich wywołań arbitra: zmiana output_config.format unieważnia
# bufor (dokumentacja structured outputs). Co dozwolone w danej chwili, mówi zdanie tury,
# a sprawdza skrypt (Przebieg.arbitruj).
SCHEMAT_ARBITRA = {"type": "json_schema", "schema": {
    "type": "object",
    "properties": {
        "tekst": {"type": "string"},
        "decyzja": {"type": "string", "enum": DECYZJE + [NIE_DOTYCZY]},
        "poza_kolejnoscia": {"type": "string",
                             "enum": ["brak", NIE_DOTYCZY] + [n for _, n in POSTACIE]},
        "pakiety": {"type": "array", "items": {"type": "string"}},
        "wynik": {"type": "string", "enum": WYNIKI + [NIE_DOTYCZY]},
    },
    "required": ["tekst", "decyzja", "poza_kolejnoscia", "pakiety", "wynik"],
    "additionalProperties": False}}


def cialo(model: str, max_tokens: int, effort: str, req: dict, arbiter: bool) -> dict:
    """Pełne ciało zapytania: to samo trafia do API i do sumy SHA-256 w zapisie."""
    oc = {"effort": effort}
    if arbiter:
        oc["format"] = SCHEMAT_ARBITRA
    return {"model": model, "max_tokens": max_tokens, "thinking": {"type": "adaptive"},
            "output_config": oc, **req}


# =============================================================================
# Model bufora (do atrapy i do szacunku)
# =============================================================================
@dataclass
class ModelBufora:
    """Przybliża usage API: odczyt od najdłuższego zapisanego prefiksu, zapis do ostatniego
    punktu bufora, reszta jako wejście bez bufora. Zakłada, że wpisy nie wygasają (TTL 1h)."""
    wpisy: set = field(default_factory=set)

    def policz(self, bloki: list[tuple[str, int, bool]]) -> dict:
        klucze, suma, pref = [], [], 0
        h = hashlib.sha256()
        for bid, tok, _ in bloki:
            h.update(bid.encode())
            klucze.append(h.hexdigest())
            pref += tok
            suma.append(pref)
        bp = [i for i, (_, _, b) in enumerate(bloki) if b]
        ost = bp[-1] if bp else -1
        traf = max([i for i in range(ost + 1) if klucze[i] in self.wpisy], default=-1)
        odczyt = suma[traf] if traf >= 0 else 0
        zapis = (suma[ost] - odczyt) if ost >= 0 else 0
        wejscie = suma[-1] - (suma[ost] if ost >= 0 else 0)
        for i in bp:
            self.wpisy.add(klucze[i])
        return {"input_tokens": wejscie, "cache_read_input_tokens": odczyt,
                "cache_creation_input_tokens": zapis}


def koszt(usage: dict, model: str, ttl: str) -> float:
    c = CENNIK[model]
    cr = usage.get("cache_creation") or {}
    z5 = cr.get("ephemeral_5m_input_tokens")
    z1 = cr.get("ephemeral_1h_input_tokens")
    if z5 is None and z1 is None:
        z = usage.get("cache_creation_input_tokens") or 0
        z5, z1 = (0, z) if ttl == "1h" else (z, 0)
    return ((usage.get("input_tokens") or 0) * c["wejscie"] + (z5 or 0) * c["zapis_5m"]
            + (z1 or 0) * c["zapis_1h"] + (usage.get("cache_read_input_tokens") or 0) * c["odczyt"]
            + (usage.get("output_tokens") or 0) * c["wyjscie"]) / 1e6


# =============================================================================
# Wykonawcy: atrapa i API
# =============================================================================
class Atrapa:
    """Atrapa modelu. Teksty są sztuczne; usage pochodzi z modelu bufora i z liczby tokenów
    tekstów stałych zmierzonej w trybie policz (albo z przelicznika 4,4 tokena na słowo)."""

    def __init__(self, scenariusz: str, tokeny: dict, zal: dict, teksty: Teksty):
        self.karty = {k: f"{KARTA_NAGLOWEK}\n\n{v}" for k, v in teksty.karty.items()}
        self.sc = scenariusz
        self.tok = tokeny
        self.zal = zal
        self.bufor = ModelBufora()
        self.licznik = 0

    def _tokeny_tekstu(self, tekst: str, nazwa: str | None) -> int:
        if nazwa and nazwa in self.tok:
            return self.tok[nazwa]
        for k, karta in self.karty.items():
            nk = f"karta_{k}_z_naglowkiem"
            if tekst.startswith(karta) and nk in self.tok:
                return self.tok[nk] + int(len(tekst[len(karta):].split()) * 4.4) + 4
        return int(len(tekst.split()) * 4.4) + 4

    def _usage(self, req: dict, stale: dict, wyjscie: int) -> dict:
        # Ustawienia (model, rozumowanie, output_config ze schematem) wchodzą do prefiksu bufora:
        # inny schemat albo wysiłek to inny prefiks. Schemat arbitra liczy się w tokenach.
        ust = json.dumps({k: req[k] for k in ("model", "thinking", "output_config")},
                         sort_keys=True)
        tok_ust = self.tok.get("schemat_arbitra", 300) if "format" in req["output_config"] else 0
        bloki = [(sha(ust), tok_ust, False)]
        for b in req["system"]:
            bloki.append((sha(b["text"]), self._tokeny_tekstu(b["text"], stale.get(sha(b["text"]))),
                          "cache_control" in b))
        for m in req["messages"]:
            zaw = m["content"]
            zaw = zaw if isinstance(zaw, list) else [{"text": zaw}]
            for b in zaw:
                t = b["text"]
                bloki.append((sha(t), self._tokeny_tekstu(t, stale.get(sha(t))),
                              "cache_control" in b))
        u = self.bufor.policz(bloki)
        u["output_tokens"] = wyjscie
        u["cache_creation"] = {"ephemeral_5m_input_tokens": 0,
                               "ephemeral_1h_input_tokens": u["cache_creation_input_tokens"]}
        return u

    def postac(self, klucz, req, stale, faza, runda):
        self.licznik += 1
        sc, z = self.sc, self.zal
        stop, details = "end_turn", None
        if sc == "pas" and faza == "dyskusja":
            tekst = "Pas. Nie mam nic do dodania (atrapa)."
        elif faza == "glosowanie":
            tekst = f"Atrapa: {NAZWA[klucz]} głosuje: pakiet 1: za; deklaruję głosy klubu."
        else:
            slowa = z["slowa_wypowiedzi"]
            if sc == "maks" and runda == 3 and klucz == "czarzasty":
                slowa = 500  # sprawdza ucinanie
            tekst = (f"Atrapa: {NAZWA[klucz]}, {faza} {runda}. "
                     + " ".join(["słowo"] * max(slowa - 6, 1)) + ".")
            if sc == "maks" and runda == 2 and klucz == "kaczynski":
                stop, tekst, details = "refusal", "", {"type": "refusal", "category": None}
        wyj = z["tokeny_myslenia_postaci"] + (int(len(tekst.split()) * 4.4) if tekst else 0)
        return tekst, stop, details, self._usage(req, stale, wyj)

    def arbiter(self, typ, req, stale, dozwolone, kontekst):
        sc = self.sc
        d = {"tekst": f"Atrapa arbitra: {typ}, {kontekst.get('nazwa_rundy', '')}. "
                      + " ".join(["słowo"] * self.zal["slowa_arbitra"])}
        if typ == "po_rundzie":
            r = kontekst["runda"]
            d.update(decyzja="dalej", poza_kolejnoscia="brak", pakiety=[], wynik=NIE_DOTYCZY)
            if sc == "maks" or sc == "typowy":
                ostatni = kontekst.get("ostatni_mowca")
                kandydaci = [x for x in dozwolone["poza_kolejnoscia"] if x not in ("brak", ostatni)]
                co_runde = sc == "maks" or self.zal.get("poza_co_runde")
                if r >= 1 and (co_runde or r % 2 == 0) and kandydaci:
                    d["poza_kolejnoscia"] = kandydaci[0]
            if "dalej" not in dozwolone["decyzja"]:
                d["decyzja"] = "glosowanie" if sc != "pas" else "brak_porozumienia"
                d["pakiety"] = ["1"] if d["decyzja"] == "glosowanie" else []
            if sc == "typowy" and r == self.zal.get("glosowanie_po", 6):
                d.update(decyzja="glosowanie", pakiety=["1"])
            poprawka = "Poprzednia odpowiedź nie została przyjęta" in req["messages"][-1]["content"]
            if sc == "maks" and r == RUNDY_DYSKUSJI and not poprawka:
                d["decyzja"] = "dalej"  # niedozwolone po 8. rundzie: sprawdza ponowienie z poprawką
        elif typ == "po_glosowaniu":
            d.update(decyzja=NIE_DOTYCZY, poza_kolejnoscia=NIE_DOTYCZY, pakiety=[])
            d["wynik"] = "dodatkowa_runda" if "dodatkowa_runda" in dozwolone["wynik"] else (
                "porozumienie_czesciowe" if sc == "typowy" else "brak_porozumienia")
        else:
            d.update(decyzja=NIE_DOTYCZY, poza_kolejnoscia=NIE_DOTYCZY, pakiety=[], wynik=NIE_DOTYCZY)
        tekst = json.dumps(d, ensure_ascii=False)
        wyj = self.zal["tokeny_myslenia_arbitra"] + int(len(tekst.split()) * 4.4)
        if self.zal.get("drogie_ogloszenie") and typ in ("po_glosowaniu", "przerwanie"):
            wyj = self.zal["max_tokens"]  # najdroższe możliwe wyjście w ostatnich wywołaniach
        return d, "end_turn", None, self._usage(req, stale, wyj)


class Api:
    def __init__(self, klucz_api: str, model: str, effort: str, max_tokens: int):
        import anthropic
        self.anthropic = anthropic
        self.client = anthropic.Anthropic(api_key=klucz_api, max_retries=4, timeout=900)
        self.model, self.effort, self.max_tokens = model, effort, max_tokens
        self._baza = None

    def _wywolaj(self, body):
        with self.client.messages.stream(**body) as s:
            m = s.get_final_message()
        tekst = "".join(b.text for b in m.content if b.type == "text")
        details = m.stop_details.model_dump() if getattr(m, "stop_details", None) else None
        return tekst, m.stop_reason, details, m.usage.model_dump(), m.id

    def postac(self, klucz, req, stale, faza, runda):
        return self._wywolaj(req)

    def arbiter(self, typ, req, stale, dozwolone, kontekst):
        tekst, stop, details, usage, mid = self._wywolaj(req)
        try:
            d = json.loads(tekst) if stop != "refusal" else None
        except json.JSONDecodeError:
            d = None
        return d, stop, details, usage, mid

    def tokeny_tekstu(self, tekst: str) -> int:
        if self._baza is None:
            self._baza = self.client.messages.count_tokens(
                model=self.model, messages=[{"role": "user", "content": "."}]).input_tokens
        n = self.client.messages.count_tokens(
            model=self.model, messages=[{"role": "user", "content": tekst}]).input_tokens
        return max(n - self._baza, 0)


# =============================================================================
# Przebieg
# =============================================================================
class Przerwanie(Exception):
    pass


class Przebieg:
    def __init__(self, args, teksty: Teksty, wykonawca, tryb: str):
        self.a, self.t, self.w, self.tryb = args, teksty, wykonawca, tryb
        self.model = args.model
        self.kolejnosc = [k for k, _ in POSTACIE]
        r = args.przesuniecie % len(self.kolejnosc)
        self.kolejnosc = self.kolejnosc[r:] + self.kolejnosc[:r]
        self.watek: list[Wpis] = []
        self.wydano = 0.0
        self.koszty = {"postac": [], "arbiter": []}
        self.ostatnie = {}  # rola albo "postac:<klucz>" -> (usage, liczba wpisów wątku)
        self.pakiety = []
        self.l_wypowiedzi = 0
        self.l_poza = 0
        self.l_wywolan = 0
        self.wyniki = []
        self.dir = Path(args.wyjscie)
        self.dir.mkdir(parents=True, exist_ok=True)
        if (self.dir / "zapis.jsonl").exists():
            raise SystemExit(f"Katalog wyjścia zawiera już zapis: {self.dir}")
        self.stale = self._stale_teksty()
        self._ustawienia()
        with open(self.dir / "zapis.md", "w", encoding="utf-8") as f:
            f.write(NAGLOWEK_ZAPISU + self._opis_ustawien_md() + "\n\n## Rozmowa\n\n")

    # --- zapis -------------------------------------------------------------
    def _stale_teksty(self) -> dict:
        t = self.t
        d = {sha(t.system_postaci()): "system_postaci", sha(t.system_arbitra()): "system_arbitra",
             sha(WATEK_NAGLOWEK): "WATEK_NAGLOWEK"}
        for k, v in t.karty.items():
            d[sha(f"{KARTA_NAGLOWEK}\n\n{v}")] = f"karta_{k}_z_naglowkiem"
        (self.dir / "teksty").mkdir(exist_ok=True)
        for nazwa, tekst in [("system_postaci", t.system_postaci()),
                             ("system_arbitra", t.system_arbitra()),
                             *[(f"karta_{k}", v) for k, v in t.karty.items()]]:
            (self.dir / "teksty" / f"{nazwa}.md").write_text(tekst, encoding="utf-8")
        (self.dir / "teksty" / "techniczne.json").write_text(
            json.dumps(teksty_techniczne(), ensure_ascii=False, indent=1), encoding="utf-8")
        return d

    def _ustawienia(self):
        try:
            import anthropic
            sdk = anthropic.__version__
        except ImportError:
            sdk = None
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True,
                              text=True).stdout.strip()
        self.ust = {
            "tryb": self.tryb, "scenariusz_atrapy": self.a.scenariusz if self.tryb == "proba" else None,
            "model": self.model, "effort": self.a.effort, "thinking": {"type": "adaptive"},
            "max_tokens": self.a.max_tokens, "ttl_bufora": self.a.ttl, "uklad": self.a.uklad,
            "wariant": self.t.nazwa_wariantu, "pakiet": self.t.nazwa_pakietu,
            "karty_zrodel_dla_arbitra": bool(self.t.zrodla), "kolejnosc": self.kolejnosc,
            "przesuniecie_kolejnosci": self.a.przesuniecie, "limit_usd": self.a.limit_usd,
            "limity": {"rundy_dyskusji": RUNDY_DYSKUSJI, "poza_kolejnoscia": LIMIT_POZA_KOLEJNOSCIA,
                       "wypowiedzi": LIMIT_WYPOWIEDZI, "tokeny_wypowiedzi": LIMIT_TOKENOW_WYPOWIEDZI},
            "cennik": {"usd_za_mln": CENNIK[self.model], "zrodlo": CENNIK_ZRODLO,
                       "data_w_skrypcie": CENNIK_DATA,
                       "sprawdzony_przez_operatora": getattr(self.a, "cennik_sprawdzony", None)},
            "repozytorium_head": head, "wersja_pakietu": WERSJA_PAKIETU,
            "sha256_skryptu": sha(Path(__file__).read_bytes()), "sdk_anthropic": sdk,
            "sha256_tekstow": self.t.sumy(),
            "sha256_tekstow_technicznych": {k: sha(v) for k, v in teksty_techniczne().items()},
            "fallbacks": "wyłączone (issue #46: bez przełączania na inny model)",
            "start": dt.datetime.now().isoformat(timespec="seconds"),
        }
        self._zapisz_json("ustawienia.json", self.ust)

    def _opis_ustawien_md(self) -> str:
        u = self.ust
        return (f"Ustawienia: model `{u['model']}`, wysiłek `{u['effort']}`, adaptacyjne "
                f"rozumowanie, max_tokens {u['max_tokens']}, wariant motywacji ({u['wariant']}), "
                f"pakiet {u['pakiet']}, kolejność: "
                + ", ".join(NAZWA[k] for k in self.kolejnosc)
                + f". Tryb: {u['tryb']}" + (f" (atrapa, scenariusz {u['scenariusz_atrapy']}; "
                                            "teksty nie pochodzą z modelu)" if u["tryb"] == "proba" else "")
                + ". Pełne ustawienia i sumy SHA-256: `ustawienia.json`.")

    def _zapisz_json(self, nazwa, obj):
        tmp = self.dir / (nazwa + ".tmp")
        tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
        tmp.replace(self.dir / nazwa)

    def _dopisz(self, nazwa, tekst):
        with open(self.dir / nazwa, "a", encoding="utf-8") as f:
            f.write(tekst)
            f.flush()
            os.fsync(f.fileno())

    def _stan(self, faza):
        self._zapisz_json("stan.json", {
            "faza": faza, "wydano_usd": round(self.wydano, 6), "wywolania": self.l_wywolan,
            "wypowiedzi_postaci": self.l_wypowiedzi, "poza_kolejnoscia": self.l_poza,
            "wpisy_watku": len(self.watek), "wyniki": self.wyniki,
            "czas": dt.datetime.now().isoformat(timespec="seconds")})

    def _do_watku(self, rola, runda, tekst, rekord):
        w = Wpis(len(self.watek) + 1, rola, runda, tekst)
        self.watek.append(w)
        rekord.update(nr=w.nr, rola=rola, podpis=PODPIS_ARBITRA if rola == "arbiter" else podpis(rola),
                      runda=runda, tekst=tekst)
        self._dopisz("zapis.jsonl", json.dumps(rekord, ensure_ascii=False) + "\n")
        kto = PODPIS_ARBITRA if rola == "arbiter" else podpis(rola)
        self._dopisz("zapis.md", f"### {w.nr}. {kto}\n\n*{runda}*\n\n{tekst}\n\n")

    # --- koszt ---------------------------------------------------------------
    def _granica(self, rola, klucz=None) -> float:
        """Szacowana górna granica kosztu następnego wywołania. Zakłada, że prefiks z poprzedniego
        wywołania o tym samym prefiksie jest w buforze (stały schemat i ustawienia, TTL 1 h):
        odczyt tego prefiksu, zapis wszystkiego, co doszło od tamtej chwili (tekst liczony po
        1 tokenie na 1,5 znaku, z zapasem), wejście bez bufora jak poprzednio i pełne max_tokens
        wyjścia; co najmniej 1,5 x najdroższe z 10 ostatnich wywołań roli (bez pierwszego, które
        zawiera jednorazowy zapis prefiksu). W układzie etap2 prefiks postaci zawiera jej kartę,
        więc punktem odniesienia jest poprzednie wywołanie tej samej postaci; jej pierwsze
        wywołanie zapisuje kartę i cały dotychczasowy wątek. Przed pierwszym wywołaniem roli:
        cały prefiks zapisany do bufora."""
        c = CENNIK[self.model]
        wyj = self.a.max_tokens * c["wyjscie"]
        znaki = lambda od: sum(len(w.blok()) for w in self.watek[od:])  # noqa: E731
        osobny = rola == "postac" and self.a.uklad == "etap2" and klucz is not None
        klucz_pref = f"postac:{klucz}" if osobny else rola
        if klucz_pref in self.ostatnie:
            u, n0 = self.ostatnie[klucz_pref]
            nowe = znaki(n0) / 1.5 + 1000
        elif rola in self.ostatnie:
            u, _ = self.ostatnie[rola]
            nowe = (znaki(0) + len(self.t.karty[klucz])) / 1.5 + 1000
        else:
            pref = (300_000 if rola == "arbiter" else 200_000) + znaki(0) / 1.5
            return (pref * c["zapis_1h"] + wyj) / 1e6
        odczyt = (u.get("cache_read_input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0)
        g = (odczyt * c["odczyt"] + (u.get("input_tokens") or 0) * c["wejscie"]
             + nowe * c["zapis_1h"] + wyj) / 1e6
        ostatnie = self.koszty[rola][1:][-10:]
        return max(g, 1.5 * max(ostatnie)) if ostatnie else g

    def _sprawdz_limit(self, rola, klucz=None):
        """Przed wywołaniem: wydane + to wywołanie + zapas na ogłoszenie przerwania przez arbitra
        musi się zmieścić w limicie. Przed wywołaniem arbitra zapas obejmuje dwa wywołania arbitra
        (to i ewentualne ogłoszenie przerwania)."""
        potrzeba = self._granica(rola, klucz) + self._granica("arbiter")
        if self.wydano + potrzeba > self.a.limit_usd:
            raise Przerwanie(f"limit kosztu {self.a.limit_usd} USD (wydano {self.wydano:.2f} USD, "
                             f"zapas na następne wywołanie i ogłoszenie arbitra {potrzeba:.2f} USD)")

    def _rekord_wywolania(self, body, przepis, wynik, rola, typ, klucz=None):
        tekst, stop, details, usage = wynik[:4]
        mid = wynik[4] if len(wynik) > 4 else None
        c = koszt(usage, self.model, self.a.ttl)
        self.wydano += c
        self.koszty[rola].append(c)
        self.ostatnie[rola] = (usage, len(self.watek))
        if klucz:
            self.ostatnie[f"postac:{klucz}"] = (usage, len(self.watek))
        self.l_wywolan += 1
        cialo_json = json.dumps(body, ensure_ascii=False, sort_keys=True)
        oc = body["output_config"]
        przepis = dict(przepis, model=body["model"], max_tokens=body["max_tokens"],
                       thinking=body["thinking"], effort=oc["effort"],
                       format="SCHEMAT_ARBITRA" if "format" in oc else None)
        return {"wywolanie": self.l_wywolan, "typ": typ, "id_odpowiedzi": mid,
                "stop_reason": stop, "stop_details": details, "usage": usage,
                "koszt_usd": round(c, 6), "wydano_lacznie_usd": round(self.wydano, 6),
                "sha256_zapytania": sha(cialo_json), "przepis_zapytania": przepis,
                "czas": dt.datetime.now().isoformat(timespec="seconds")}

    # --- wywołania -------------------------------------------------------------
    def mow(self, klucz, faza, runda_nr, nazwa_rundy, tura_klucz):
        if self.l_wypowiedzi >= LIMIT_WYPOWIEDZI:
            raise Przerwanie(f"limit {LIMIT_WYPOWIEDZI} wypowiedzi postaci")
        self._sprawdz_limit("postac", klucz)
        tura = TURA[tura_klucz].format(imie=NAZWA[klucz], n=runda_nr, max=RUNDY_DYSKUSJI,
                                       nazwa_rundy=nazwa_rundy,
                                       pakiety=", ".join(self.pakiety) or "(arbiter nie podał numerów)")
        req, przepis = zapytanie_postaci(self.t, klucz, self.watek, tura, self.a.uklad, self.a.ttl)
        body = cialo(self.model, self.a.max_tokens, self.a.effort, req, arbiter=False)
        wynik = self._wywolaj(lambda: self.w.postac(klucz, body, self.stale, faza, runda_nr),
                              "postac", klucz)
        tekst, stop = wynik[0], wynik[1]
        rek = self._rekord_wywolania(body, przepis, wynik, "postac", faza, klucz)
        if stop == "refusal" or not tekst.strip():
            powod = "odmowa, stop_reason refusal" if stop == "refusal" else f"pusta odpowiedź, stop_reason {stop}"
            rek["tekst_modelu"] = tekst
            tekst = ODMOWA_PAS.format(powod=powod)
            rek["regula"] = "odmowa albo pusta odpowiedź liczy się jako Pas"
        else:
            n = self._tokeny(tekst)
            rek["tokeny_tekstu"] = n
            if n > LIMIT_TOKENOW_WYPOWIEDZI:
                rek["tekst_modelu"] = tekst
                tekst = utnij(tekst, n) + "\n\n" + UCIECIE.format(limit=LIMIT_TOKENOW_WYPOWIEDZI)
                rek["regula"] = "ucięcie po limicie tokenów"
        self.l_wypowiedzi += 1
        self._do_watku(klucz, nazwa_rundy, tekst, rek)
        self._stan(nazwa_rundy)
        return tekst

    def _tokeny(self, tekst):
        if isinstance(self.w, Api):
            return self.w.tokeny_tekstu(tekst)
        return int(len(tekst.split()) * 4.4)

    def _wywolaj(self, f, rola, klucz=None):
        """Jedno ponowienie po błędzie połączenia albo serwera w trakcie strumienia (SDK ponawia
        tylko przed rozpoczęciem odpowiedzi). Przed ponowieniem skrypt sprawdza limit kosztu;
        koszt nieudanego strumienia nie jest znany ze `usage`."""
        try:
            return f()
        except Exception as e:  # noqa: BLE001
            if not ponawialny(e):
                raise
            self._dopisz("zapis.jsonl", json.dumps({"blad_wywolania": f"{type(e).__name__}: {e}",
                                                    "czas": dt.datetime.now().isoformat(
                                                        timespec="seconds")},
                                                   ensure_ascii=False) + "\n")
            time.sleep(30)
            self._sprawdz_limit(rola, klucz)
            return f()

    def arbitruj(self, typ, nazwa_rundy, dozwolone=None, **kontekst):
        dozwolone = dozwolone or {}
        opis = {k: ", ".join(f'"{x}"' for x in v) for k, v in dozwolone.items()}
        tura = ARBITER_TURA[typ].format(nazwa_rundy=nazwa_rundy, decyzje=opis.get("decyzja"),
                                        poza=opis.get("poza_kolejnoscia"), wyniki=opis.get("wynik"),
                                        **kontekst)
        kontekst["nazwa_rundy"] = nazwa_rundy
        blad = None
        for proba in (1, 2):
            if typ != "przerwanie":
                self._sprawdz_limit("arbiter")
            t = tura if blad is None else f"{tura}\n\n{ARBITER_POPRAWKA.format(blad=blad)}"
            req, przepis = zapytanie_arbitra(self.t, self.watek, t, self.a.ttl)
            body = cialo(self.model, self.a.max_tokens, self.a.effort, req, arbiter=True)
            wynik = self._wywolaj(
                lambda: self.w.arbiter(typ, body, self.stale, dozwolone, kontekst), "arbiter")
            d, stop = wynik[0], wynik[1]
            rek = self._rekord_wywolania(body, przepis, wynik, "arbiter", f"arbiter_{typ}")
            blad = sprawdz_arbitra(d, dozwolone, stop)
            if blad is None:
                rek["decyzje"] = {k: v for k, v in d.items() if k != "tekst"}
                self._do_watku("arbiter", nazwa_rundy, d["tekst"], rek)
                self._stan(nazwa_rundy)
                return d
            rek["odpowiedz_json"] = d
            rek["blad"] = f"odpowiedź arbitra nieprzyjęta (próba {proba}): {blad}"
            self._dopisz("zapis.jsonl", json.dumps(rek, ensure_ascii=False) + "\n")
            if typ == "przerwanie":
                break
        raise Przerwanie("arbiter dwa razy nie dał poprawnej odpowiedzi")

    # --- przebieg ---------------------------------------------------------------
    def runda(self, faza, nr, nazwa, tura_klucz):
        teksty = []
        for k in self.kolejnosc:
            teksty.append((k, self.mow(k, faza, nr, nazwa, tura_klucz)))
        return teksty

    def po_rundzie(self, nazwa, nr, teksty, dyskusja: bool, wymuszona=False):
        wszyscy_pas = bool(teksty) and all(jest_pas(t) for _, t in teksty)
        decyzje = ["dalej", "glosowanie", "brak_porozumienia"]
        info = []
        if wszyscy_pas:
            info.append("W tej rundzie wszystkie postacie napisały \"Pas\".")
        if not dyskusja and not wymuszona:
            decyzje = ["dalej"]  # po rundzie otwarcia zawsze dyskusja (arbiter.md, część 2)
        elif wymuszona or wszyscy_pas or (dyskusja and nr >= RUNDY_DYSKUSJI):
            decyzje = ["glosowanie", "brak_porozumienia"]
            info.append("Następnej rundy dyskusji nie ma według reguł; wybierz głosowanie albo brak "
                        "porozumienia.")
        poza = ["brak"]
        if dyskusja and self.l_poza < LIMIT_POZA_KOLEJNOSCIA:
            poza += [NAZWA[k] for k in self.kolejnosc]
        info.append(f"Wykorzystane wypowiedzi poza kolejnością: {self.l_poza} z {LIMIT_POZA_KOLEJNOSCIA}.")
        ostatni = NAZWA[teksty[-1][0]] if teksty else None
        d = self.arbitruj("po_rundzie", nazwa, {"decyzja": decyzje, "poza_kolejnoscia": poza},
                          informacje=" ".join(info), runda=nr, ostatni_mowca=ostatni)
        if d["poza_kolejnoscia"] not in ("brak", NIE_DOTYCZY) and d["decyzja"] != "brak_porozumienia":
            klucz = next(k for k, v in NAZWA.items() if v == d["poza_kolejnoscia"])
            self.l_poza += 1
            self.mow(klucz, "dyskusja", nr, nazwa + ", głos poza kolejnością", "poza_kolejnoscia")
        return d

    def glosowanie(self, nazwa, dodatkowa_dostepna, pakiety):
        self.pakiety = [str(x) for x in pakiety]
        self.runda("glosowanie", 0, nazwa, "glosowanie")
        wyniki = ["porozumienie", "porozumienie_czesciowe", "brak_porozumienia"]
        if dodatkowa_dostepna:
            wyniki.append("dodatkowa_runda")
        return self.arbitruj("po_glosowaniu", nazwa, {"wynik": wyniki},
                             informacje=("Dodatkowa runda jest dostępna." if dodatkowa_dostepna
                                         else "Dodatkowa runda nie jest już dostępna."))

    def wykonaj(self):
        wynik = None
        try:
            self.arbitruj("otwarcie", "Otwarcie", kolejnosc=", ".join(NAZWA[k] for k in self.kolejnosc))
            t = self.runda("otwarcie", 0, "Runda otwarcia", "otwarcie")
            d = self.po_rundzie("Runda otwarcia", 0, t, dyskusja=False)
            nr = 0
            while d["decyzja"] == "dalej":
                nr += 1
                nazwa = f"Runda dyskusji {nr}"
                t = self.runda("dyskusja", nr, nazwa, "dyskusja")
                d = self.po_rundzie(nazwa, nr, t, dyskusja=True)
            if d["decyzja"] == "brak_porozumienia":
                wynik = "brak_porozumienia"
            else:
                g = self.glosowanie("Runda głosowania", dodatkowa_dostepna=True,
                                    pakiety=d["pakiety"])
                wynik = g["wynik"]
                if wynik == "dodatkowa_runda":
                    t = self.runda("dyskusja", nr + 1, "Dodatkowa runda dyskusji", "dodatkowa")
                    d = self.po_rundzie("Dodatkowa runda dyskusji", nr + 1, t, dyskusja=False,
                                        wymuszona=True)
                    if d["decyzja"] == "brak_porozumienia":
                        wynik = "brak_porozumienia"
                    else:
                        wynik = self.glosowanie("Powtórne głosowanie", dodatkowa_dostepna=False,
                                                pakiety=d["pakiety"])["wynik"]
            stan = "zakończony"
        except Przerwanie as e:
            stan = f"przerwany: {e}"
            self._dopisz("zapis.md", f"*Adnotacja skryptu: przebieg przerwany ({e}).*\n\n")
            try:
                self.arbitruj("przerwanie", "Przerwanie przebiegu", powod=str(e))
            except Exception as e2:  # noqa: BLE001 - zapisujemy każdy błąd ogłoszenia
                self._dopisz("zapis.md", f"*Adnotacja skryptu: arbiter nie ogłosił wyniku ({e2}).*\n\n")
            wynik = "brak_porozumienia (przerwanie)"
        except Exception as e:  # noqa: BLE001 - błąd API: zapisz stan i zakończ
            stan = f"przerwany: błąd {type(e).__name__}: {e}"
            self._dopisz("zapis.md", f"*Adnotacja skryptu: przebieg przerwany ({stan}).*\n\n")
            wynik = None
        podsum = {"stan": stan, "wynik": wynik, "wydano_usd": round(self.wydano, 4),
                  "wywolania": self.l_wywolan, "wypowiedzi_postaci": self.l_wypowiedzi,
                  "poza_kolejnoscia": self.l_poza, "wpisy_watku": len(self.watek),
                  "koniec": dt.datetime.now().isoformat(timespec="seconds")}
        self._zapisz_json("wynik.json", podsum)
        self._stan("koniec")
        self._dopisz("zapis.md", f"## Wynik\n\nStan: {stan}. Wynik według arbitra: {wynik}. "
                                 f"Koszt z `usage`: {self.wydano:.2f} USD, wywołań: {self.l_wywolan}, "
                                 f"wypowiedzi postaci: {self.l_wypowiedzi}.\n")
        return podsum


def sprawdz_arbitra(d, dozwolone: dict, stop) -> str | None:
    """Zwraca opis błędu albo None. Sprawdza tylko pola, których dotyczy dana chwila."""
    if stop == "refusal":
        return "odmowa modelu"
    if not isinstance(d, dict) or not isinstance(d.get("tekst"), str) or not d["tekst"].strip():
        return f"brak poprawnego JSON z polem tekst (stop_reason {stop})"
    for pole, wartosci in dozwolone.items():
        w = d.get(pole)
        if pole == "poza_kolejnoscia" and w == NIE_DOTYCZY:
            w = "brak"
        if w not in wartosci:
            return f"pole {pole} = {d.get(pole)!r}, dozwolone: {', '.join(wartosci)}"
    if dozwolone.get("decyzja") and d.get("decyzja") == "glosowanie" and not d.get("pakiety"):
        return "decyzja glosowanie bez numerów pakietów w polu pakiety"
    return None


def ponawialny(e: Exception) -> bool:
    try:
        import anthropic
    except ImportError:
        return False
    if isinstance(e, anthropic.APIConnectionError):
        return True
    return isinstance(e, anthropic.APIStatusError) and (e.status_code >= 500 or e.status_code == 429)


def jest_pas(tekst: str) -> bool:
    """Wypowiedź jest "Pas", gdy (po ewentualnym podpisie w pierwszej linii) zaczyna się od Pas."""
    linie = tekst.strip().split("\n")
    if linie and "(postać symulowana przez AI)" in linie[0]:
        linie = linie[1:]
    return bool(re.match(r"^\W*Pas\b", "\n".join(linie).strip()))


def utnij(tekst: str, tokeny: int) -> str:
    """Skraca tekst proporcjonalnie do limitu tokenów, do końca ostatniego pełnego zdania."""
    slowa = tekst.split(" ")
    n = max(int(len(slowa) * LIMIT_TOKENOW_WYPOWIEDZI / tokeny * 0.97), 1)
    krotszy = " ".join(slowa[:n])
    m = list(re.finditer(r"[.!?](\s|$)", krotszy))
    return krotszy[:m[-1].end()].rstrip() if m and m[-1].end() > len(krotszy) // 2 else krotszy


# =============================================================================
# Tryby
# =============================================================================
def klucz_api(args) -> str:
    if not args.zmienna_klucza:
        raise SystemExit("Podaj --zmienna-klucza (nazwa zmiennej środowiskowej z kluczem API).")
    k = os.environ.get(args.zmienna_klucza)
    if not k:
        raise SystemExit(f"Zmienna środowiskowa {args.zmienna_klucza} jest pusta albo nie istnieje.")
    return k


def tryb_zbuduj(args):
    out = {"wersja_pakietu": WERSJA_PAKIETU, "sha256_skryptu": sha(Path(__file__).read_bytes()),
           "teksty": {}, "teksty_techniczne": {k: sha(v) for k, v in teksty_techniczne().items()}}
    wd = warianty()
    for w, t in wd.items():
        out["teksty"][f"wariant_{w}"] = {"sha256": sha(t), "slowa": len(t.split())}
    for p in PAKIETY:
        t = zbuduj_pakiet(p)
        out["teksty"][f"pakiet_{p}"] = {"sha256": sha(t), "slowa": len(t.split())}
    z = zbuduj_zrodla()
    out["teksty"]["karty_zrodel"] = {"sha256": sha(z), "slowa": len(z.split())}
    a = oryginal_etapu2("arbiter.md")
    out["teksty"]["arbiter"] = {"sha256": sha(a), "slowa": len(a.split())}
    for k, t in karty().items():
        out["teksty"][f"karta_{k}"] = {"sha256": sha(t), "slowa": len(t.split())}
    if args.zapisz_teksty:
        d = Path(args.zapisz_teksty)
        d.mkdir(parents=True, exist_ok=True)
        for p in PAKIETY:
            (d / f"pakiet_{p}.md").write_text(zbuduj_pakiet(p), encoding="utf-8")
        (d / "karty_zrodel.md").write_text(z, encoding="utf-8")
        for w, t in wd.items():
            (d / f"wariant_{w}.md").write_text(t, encoding="utf-8")
    return out


def tryb_policz(args):
    import anthropic
    c = anthropic.Anthropic(api_key=klucz_api(args))
    m = args.model

    def ile(system=None, messages=None):
        kw = {"model": m, "messages": messages or [{"role": "user", "content": "."}]}
        if system:
            kw["system"] = system
        return c.messages.count_tokens(**kw).input_tokens

    baza = ile()
    wd, kd = warianty(), karty()
    res = {"model": m, "data": dt.date.today().strftime("%Y.%m.%d"), "baza_pustego_zapytania": baza,
           "teksty": {}}

    def zapisz(nazwa, tekst):
        n = ile(system=[{"type": "text", "text": tekst}]) - baza
        res["teksty"][nazwa] = {"tokeny": n, "slowa": len(tekst.split()), "sha256": sha(tekst)}
        return n

    for p in PAKIETY:
        zapisz(f"pakiet_{p}", zbuduj_pakiet(p))
    for w in "abc":
        zapisz(f"wariant_{w}", wd[w])
    for k, t in kd.items():
        zapisz(f"karta_{k}_z_naglowkiem", f"{KARTA_NAGLOWEK}\n\n{t}")
    zapisz("arbiter", oryginal_etapu2("arbiter.md"))
    zapisz("karty_zrodel", zbuduj_zrodla())
    for p in PAKIETY:
        t = Teksty(wd[args.wariant], zbuduj_pakiet(p), kd, oryginal_etapu2("arbiter.md"),
                   zbuduj_zrodla(), args.wariant, p)
        zapisz(f"system_postaci_{args.wariant}_{p}", t.system_postaci())
        zapisz(f"system_arbitra_{p}", t.system_arbitra())
        t0 = Teksty(t.wariant, t.pakiet, kd, t.arbiter, "", args.wariant, p)
        zapisz(f"system_arbitra_{p}_bez_zrodel", t0.system_arbitra())
    # Tokeny stałego schematu odpowiedzi arbitra (różnica z formatem i bez niego).
    bez = c.messages.count_tokens(model=m, messages=[{"role": "user", "content": "Test."}],
                                  output_config={"effort": "medium"}).input_tokens
    z = c.messages.count_tokens(model=m, messages=[{"role": "user", "content": "Test."}],
                                output_config={"effort": "medium", "format": SCHEMAT_ARBITRA}).input_tokens
    res["teksty"]["schemat_arbitra"] = {"tokeny": z - bez, "sha256": sha(json.dumps(
        SCHEMAT_ARBITRA, ensure_ascii=False, sort_keys=True))}
    # Kontrola rachunku: pełne pierwsze zapytanie postaci w obu układach.
    t = wczytaj_teksty(args.wariant, args.pakiet, True)
    w = [Wpis(1, "arbiter", "Otwarcie", "Otwarcie spotkania (tekst kontrolny).")]
    for uklad in ("wspolny-watek", "etap2"):
        req, _ = zapytanie_postaci(t, "nawrocki", w,
                                   TURA["otwarcie"].format(imie=NAZWA["nawrocki"]), uklad, "1h")
        res[f"pelne_zapytanie_nawrocki_{uklad}"] = c.messages.count_tokens(
            model=m, system=req["system"], messages=req["messages"]).input_tokens
    return res


def tokeny_dla_atrapy(plik, wariant, pakiet, ze_zrodlami=True) -> dict:
    """Mapuje nazwy stałych tekstów przebiegu na liczbę tokenów z trybu policz."""
    if not plik:
        return {}
    d = json.loads(Path(plik).read_text(encoding="utf-8"))["teksty"]
    out = {"system_postaci": d[f"system_postaci_{wariant}_{pakiet}"]["tokeny"],
           "system_arbitra": d[f"system_arbitra_{pakiet}" + ("" if ze_zrodlami else "_bez_zrodel")][
               "tokeny"]}
    if "schemat_arbitra" in d:
        out["schemat_arbitra"] = d["schemat_arbitra"]["tokeny"]
    for k, _ in POSTACIE:
        out[f"karta_{k}_z_naglowkiem"] = d[f"karta_{k}_z_naglowkiem"]["tokeny"]
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("tryb", choices=["zbuduj", "policz", "proba", "przebieg"])
    p.add_argument("--wyjscie", help="katalog zapisu przebiegu albo plik JSON (zbuduj, policz)")
    p.add_argument("--wariant", choices=list("abc"), default="b")
    p.add_argument("--pakiet", choices=list(PAKIETY), default="podstawowy")
    p.add_argument("--bez-kart-zrodel", action="store_true", help="arbiter bez kart źródeł")
    p.add_argument("--model", default="claude-opus-5-5")
    p.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    p.add_argument("--max-tokens", type=int, default=16000,
                   help="limit wyjścia z rozumowaniem; limit tekstu wypowiedzi to "
                        f"{LIMIT_TOKENOW_WYPOWIEDZI} tokenów")
    p.add_argument("--ttl", default="1h", choices=["5m", "1h"])
    p.add_argument("--uklad", default="etap2", choices=["etap2", "wspolny-watek"],
                   help="etap2: wariant, pakiet, karta, wątek (domyślny, rozstrzygnięcie prowadzącego "
                        "w issue #46); wspolny-watek: karta po wątku (tańszy)")
    p.add_argument("--przesuniecie", type=int, default=0,
                   help="przesunięcie kolejności otwarcia (0: od Nawrockiego, 1: od Tuska, ...)")
    p.add_argument("--limit-usd", type=float, default=18.0)
    p.add_argument("--zmienna-klucza", help="nazwa zmiennej środowiskowej z kluczem API")
    p.add_argument("--potwierdzam-koszt", action="store_true")
    p.add_argument("--cennik-sprawdzony", help="data sprawdzenia cennika (yyyy.mm.dd), dziś")
    p.add_argument("--scenariusz", default="typowy", choices=["typowy", "maks", "pas"])
    p.add_argument("--tokeny", help="plik JSON z trybu policz (dla atrapy)")
    p.add_argument("--slowa-wypowiedzi", type=int, default=160)
    p.add_argument("--slowa-arbitra", type=int, default=200)
    p.add_argument("--tokeny-myslenia-postaci", type=int, default=1500)
    p.add_argument("--tokeny-myslenia-arbitra", type=int, default=3000)
    p.add_argument("--atrapa-drogie-ogloszenie", action="store_true",
                   help="(proba) ogłoszenia arbitra po głosowaniu i przy przerwaniu z pełnym max_tokens")
    p.add_argument("--atrapa-glosowanie-po", type=int, default=6,
                   help="(proba, scenariusz typowy) po której rundzie dyskusji arbiter ogłasza głosowanie")
    p.add_argument("--atrapa-poza-co-runde", action="store_true",
                   help="(proba, scenariusz typowy) głos poza kolejnością w każdej rundzie, nie co drugą")
    p.add_argument("--zapisz-teksty", help="(zbuduj) katalog na sklejone teksty")
    a = p.parse_args()
    if a.model not in CENNIK:
        raise SystemExit(f"Brak cennika dla modelu {a.model}; dopisz go w CENNIK.")

    if a.tryb in ("zbuduj", "policz"):
        res = tryb_zbuduj(a) if a.tryb == "zbuduj" else tryb_policz(a)
        s = json.dumps(res, ensure_ascii=False, indent=1)
        if a.wyjscie:
            Path(a.wyjscie).write_text(s + "\n", encoding="utf-8")
        print(s)
        return
    if not a.wyjscie:
        raise SystemExit("Podaj --wyjscie (katalog zapisu przebiegu).")
    teksty = wczytaj_teksty(a.wariant, a.pakiet, not a.bez_kart_zrodel)
    if a.tryb == "proba":
        zal = {"slowa_wypowiedzi": a.slowa_wypowiedzi, "slowa_arbitra": a.slowa_arbitra,
               "tokeny_myslenia_postaci": a.tokeny_myslenia_postaci,
               "tokeny_myslenia_arbitra": a.tokeny_myslenia_arbitra,
               "drogie_ogloszenie": a.atrapa_drogie_ogloszenie, "max_tokens": a.max_tokens,
               "glosowanie_po": a.atrapa_glosowanie_po, "poza_co_runde": a.atrapa_poza_co_runde}
        wyk = Atrapa(a.scenariusz, tokeny_dla_atrapy(a.tokeny, a.wariant, a.pakiet, not a.bez_kart_zrodel), zal, teksty)
    else:
        dzis = dt.date.today().strftime("%Y.%m.%d")
        if not a.potwierdzam_koszt:
            raise SystemExit("Płatny przebieg wymaga --potwierdzam-koszt.")
        if a.cennik_sprawdzony != dzis:
            raise SystemExit(f"Sprawdź cennik ({CENNIK_ZRODLO}) i podaj --cennik-sprawdzony {dzis}.")
        wyk = Api(klucz_api(a), a.model, a.effort, a.max_tokens)
    wynik = Przebieg(a, teksty, wyk, a.tryb).wykonaj()
    print(json.dumps(wynik, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
