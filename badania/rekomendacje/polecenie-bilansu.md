> Polecenie dla GPT-6.1 Sol: bilans propozycji. Napisał koordynator (Claude Opus 5.5). Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `2a14146659aaf8b8269d4dce28ab62a5bc27192556af473007ffb6621fe23013`.
> Wynik: [bilans propozycji](../bilans-propozycji.md).

---

# Polecenie: bilans zysków i strat każdej propozycji dla każdej siły

Materiał: repozytorium bazy wiedzy o sporze wokół TK w bieżącym katalogu (wersja d8b2eb1). Najważniejsze pliki: badania/propozycje-na-stole.md (treść propozycji z dokumentów autorów), badania/scenariusze-naprawy.md (scenariusze w debacie i stanowiska stron), badania/sily-i-glosy.md (kluby, liczby posłów, progi, możliwe większości), badania/warunki-rozwiazan.md (Senat, rola Prezydenta, Kp 3/24, Komisja Wenecka), historia-sporu.md. Inne pliki według potrzeby, w tym karty źródeł w zrodla/okres-2024-2026/. Nie szukaj w internecie.

## Zadanie

Dla każdej propozycji poniżej oceń, co zyskuje i co traci każda siła, i podaj bilans. Potem oceń, czy propozycja ma szansę na potrzebne głosy.

Propozycje (każda osobno):
1. Scenariusz 1 ze scenariusze-naprawy.md: Sejm obsadza wakaty, ślubowanie bez udziału Prezydenta.
2. Scenariusz 2: ślubowanie tylko przed Prezydentem, który może je wstrzymać (stan obecny utrwalony).
3. Reset według PSL (propozycje-na-stole.md, część 1).
4. Reset według Rozwoju Plus (część 2).
5. Reset według Konfederacji (część 3).
6. Propozycja Fundacji Batorego (część 4).
7. Propozycje HFPC i Klubu Jagiellońskiego (część 5), osobno, jeśli się różnią.
8. Kukiz'15, druk 166 (część 6).
9. Scenariusz 4: reset po wyborach w 2027 roku.
10. Scenariusz 5: przedterminowe wybory lub zmiana rządu.
11. Scenariusz 6: nowa ustawa o TK bez zmiany Konstytucji.
12. Scenariusz 7: nowa Konstytucja. Scenariusz 8: likwidacja TK. Te dwa możesz ocenić krócej.

Siły: KO (156), PiS (147), Rozwój Plus (40), PSL (32), Lewica (21), Konfederacja (17), Polska 2050 (15), Centrum (15), Razem (4), Korona (3), Prezydent, sędziowie TK sprzed 2026 roku, sędziowie wybrani w 2026 roku, obywatele. Liczby posłów: API Sejmu 2026.11.04, jak w sily-i-glosy.md.

## Format (po polsku, Markdown, najwyżej około 5000 słów)

1. **Jak czytać.** Dwa-trzy zdania: co znaczy zysk i strata (interes polityczny i instytucjonalny danej siły, nie ocena moralna), że to ocena, nie fakt.
2. **Macierz bilansów.** Jedna tabela: wiersze to propozycje, kolumny to siły, w komórkach tylko znak: `+` zysk, `-` strata, `+/-` mieszany, `0` obojętnie, `?` brak danych. Pod tabelą legenda.
3. **Każda propozycja osobno** (nagłówek `## N. Nazwa`):
   - jednym zdaniem, co przewiduje, z plikiem źródłowym;
   - jaki akt i jaki próg (zwykła ustawa, 276 przy wecie, 307 i Senat przy zmianie Konstytucji);
   - tabela: Siła | Zysk | Strata | Bilans, po jednym krótkim zdaniu w komórce;
   - **arytmetyka:** która konfiguracja klubów daje próg, ile brakuje; które siły z bilansem ujemnym są niezbędne arytmetycznie (to najważniejsza informacja: kto musiałby zagłosować wbrew swojemu interesowi);
   - **szansa:** niska, średnia albo wysoka, jednym zdaniem dlaczego.
4. **Wnioski.** Najwyżej 8 punktów: które propozycje nie mają szans, bo niezbędna siła traci; które są arytmetycznie możliwe; które siły są języczkiem u wagi; czego brakuje w danych.

## Zasady

- Fakty z repozytorium z nazwą pliku; oceny oznaczaj jako oceny. Stanowisko siły (co zadeklarowała) to fakt; zysk lub strata to ocena.
- Nie wymyślaj stanowisk. Gdy siła nie zajęła stanowiska, napisz to.
- Licz przy pełnej sali i zaznacz to. Zmiana Konstytucji: 2/3 głosujących przy kworum, 307 przy pełnej sali, plus bezwzględna większość Senatu; Prezydent podpisuje w 21 dni. Odrzucenie weta: 3/5, 276 przy pełnej sali.
- Pisz dla osoby bez wiedzy prawniczej, krótkimi zdaniami. Nie używaj długiego myślnika ani półpauzy, tylko zwykłego łącznika. Proste apostrofy.
- Końcowa odpowiedź ma być wyłącznie gotowym tekstem notatki.
