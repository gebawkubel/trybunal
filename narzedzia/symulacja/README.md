# Skrypt symulacji negocjacji o TK (issue #46, etap 3)

Skrypt `symulacja.py` prowadzi jedną rozmowę dziesięciu postaci i arbitra według [instrukcji arbitra](../../badania/symulacja/etap-2/arbiter.md). Każda postać i arbiter to osobne wywołanie tego samego modelu (domyślnie Claude Opus 5.5) z tymi samymi ustawieniami. Skrypt nie zmienia treści materiałów etapów 1 i 2: wysyła je dosłownie i przed każdym przebiegiem sprawdza ich sumy SHA-256 z nagłówków plików etapu 2.

Napisał wykonawca etapu 3 (Claude Opus 5.5, agent Claude Code) na repozytorium w wersji 0726d6f, według treści issue #46 z komentarzami. To narzędzie i szacunek do jawnej recenzji; płatny przebieg uruchamia koordynator po PASS.

## Jak uruchomić

Wymagania: Python 3.10 lub nowszy, git, pakiet z `requirements.txt` (oficjalne SDK Anthropic). Skrypt czyta pakiet wiedzy z historii git w wersji 70b735a, więc działa w pełnym klonie repozytorium.

| Tryb | Co robi | Koszt |
|---|---|---|
| `zbuduj` | skleja pakiet wiedzy, warianty, karty i instrukcję arbitra, sprawdza sumy z etapu 2, wypisuje sumy gotowych tekstów ([sumy.json](sumy.json)) | bez API |
| `policz` | mierzy wielkość tekstów endpointem `messages.count_tokens` ([tokeny.json](tokeny.json)) | bez generowania, bez opłat za tokeny |
| `proba` | przebieg na atrapie modelu: kolejność, limity, zapis, limit kosztu; z plikiem z trybu `policz` daje szacunek kosztu | bez API |
| `przebieg` | płatny przebieg | według `usage` |

Przykłady:

```
python3 narzedzia/symulacja/symulacja.py zbuduj --wyjscie narzedzia/symulacja/sumy.json
python3 narzedzia/symulacja/symulacja.py policz --zmienna-klucza ANTHROPIC_CREDITS_API_KEY --wyjscie tokeny.json
python3 narzedzia/symulacja/symulacja.py proba --tokeny narzedzia/symulacja/tokeny.json --wyjscie <katalog>
python3 narzedzia/symulacja/symulacja.py przebieg --wariant b --zmienna-klucza ANTHROPIC_CREDITS_API_KEY \
    --limit-usd 25 --cennik-sprawdzony <dzisiejsza data yyyy.mm.dd> --potwierdzam-koszt --wyjscie <katalog>
```

Klucz API: skrypt czyta go tylko ze zmiennej środowiskowej, której nazwę podaje `--zmienna-klucza`, i przekazuje jawnie do klienta SDK. Klucz nie trafia do kodu, zapisu ani repozytorium. Płatny przebieg nie ruszy bez `--potwierdzam-koszt` i bez daty sprawdzenia cennika równej dniu przebiegu.

Przebiegi 2 i 3 tego samego wariantu zmieniają kolejność otwarcia opcją `--przesuniecie` (1: zaczyna Tusk, potem Kaczyński; 2: zaczyna Kaczyński), jak w etapie 1, część 4.

## Co dostaje model

Każda postać przy każdej wypowiedzi:

1. w polu `system`: instrukcję wariantu motywacji (część wspólna i jeden wariant z `warianty-motywacji.md`, dosłownie), potem pakiet wiedzy;
2. w pierwszej wiadomości: cały dotychczasowy wątek, po jednym bloku na wypowiedź, z oznaczeniem rundy i podpisem;
3. w wiadomości systemowej po wątku: swoją kartę prywatną (tylko swoją) i jedno zdanie, czyja teraz kolej.

Arbiter: `arbiter.md`, pakiet wiedzy i karty źródeł z części 4 pakietu (arbiter.md na to pozwala; opcja `--bez-kart-zrodel` je wyłącza), potem wątek i zdanie o zadaniu. Arbiter nie widzi kart postaci ani instrukcji wariantów.

Pakiet wiedzy powstaje dokładnie według tabeli w [pakiet-wiedzy.md](../../badania/symulacja/etap-2/pakiet-wiedzy.md), część 2: te same pliki, zakresy linii i wycięcia, z wersji 70b735a. Każdy plik ma linię z nazwą i zakresem, a przerwy między zakresami oznacza "[...]". Na początku jest zdanie o stanie wiedzy i o linkach (część 1, pkt 5). Plik `zgromadzenie-2026-11-03.md` ma 90 linii, więc zakres "85-91" kończy się na 90. Pakiet minimalny (część 3) jest dostępny opcją `--pakiet minimalny`.

Ustawienia jednakowe dla wszystkich wywołań w przebiegu: model, `thinking: adaptive` (w Opus 5.5 rozumowania nie da się wyłączyć), ten sam poziom wysiłku (domyślnie `medium`, domyślny dla tego modelu), `max_tokens` 16 000 (limit obejmuje rozumowanie; limit tekstu wypowiedzi jest osobno, niżej). Arbiter dodatkowo odpowiada w formacie JSON (pole `tekst` i decyzje), bo skrypt musi odczytać jego decyzje. Skrypt nie używa automatycznego przełączania na inny model (`fallbacks`).

Teksty techniczne skryptu (nagłówek wątku, zdania o kolejce, zdania dla arbitra, adnotacje) są stałymi na początku `symulacja.py`; ich sumy są w [sumy.json](sumy.json), a każdy przebieg zapisuje je w `teksty/techniczne.json`.

## Reguły przebiegu

Kolejność według arbiter.md, część 2: otwarcie arbitra, runda otwarcia, najwyżej 8 rund dyskusji, runda głosowania, ewentualnie jedna dodatkowa runda i powtórne głosowanie. Po każdej rundzie arbiter pisze stan stołu i wybiera decyzję. Skrypt pilnuje liczb i nie pozwala wybrać decyzji, których reguły w danej chwili nie dopuszczają (lista dozwolonych wartości w schemacie odpowiedzi).

| Reguła | Jak działa w skrypcie |
|---|---|
| Głos poza kolejnością | arbiter może go udzielić raz na rundę, w podsumowaniu rundy; postać mówi zaraz po nim, a wypowiedź liczy się do tej rundy. Najwyżej 10 w przebiegu, tylko w rundach dyskusji 1-8. Uproszczenie: arbiter decyduje po rundzie, nie w jej trakcie, żeby nie wywoływać go po każdej wypowiedzi |
| Runda głosowania | gdy arbiter ją ogłosi (wniosek o głosowanie i pełna runda od wniosku, ocenia arbiter); po 8. rundzie i po rundzie samych "Pas" skrypt dopuszcza tylko głosowanie albo brak porozumienia; po rundzie otwarcia tylko dalszą dyskusję. Każda postać głosuje raz, po kolei nad wszystkimi pakietami wymienionymi przez arbitra |
| "Pas" | skrypt rozpoznaje wypowiedź zaczynającą się od "Pas" (także po podpisie w pierwszej linii) |
| Dodatkowa runda | najwyżej jedna, na decyzję arbitra po głosowaniu; po powtórnym głosowaniu przebieg się kończy |
| Długość wypowiedzi | po odpowiedzi skrypt liczy tokeny tekstu (count_tokens); powyżej 1100 ucina do ostatniego pełnego zdania i dopisuje adnotację; pełny tekst zostaje w zapisie JSONL |
| Odmowa modelu albo pusta odpowiedź postaci | liczy się jako "Pas" z adnotacją skryptu widoczną w wątku; bez ponawiania i bez zmiany modelu |
| Błędna odpowiedź arbitra | jedno ponowienie tego samego zapytania; po drugim błędzie przebieg się kończy |
| Limit wypowiedzi | najwyżej 130 wypowiedzi postaci (arbiter.md: 10 + 80 + 10 poza kolejnością + 10 + 10 + 10) |
| Limit kosztu | domyślnie 25 USD. Przed każdym wywołaniem skrypt sprawdza, czy wydana kwota plus zapas na to wywołanie i na końcowe ogłoszenie arbitra mieści się w limicie (zapas: 1,5 razy najdroższe z 10 ostatnich wywołań tej roli). Jeśli nie, przerywa, arbiter ogłasza brak porozumienia według warunku (d), a stan zostaje zapisany |

Koszt każdego wywołania skrypt liczy z pola `usage` odpowiedzi według cennika w `symulacja.py` (Claude Opus 5.5: wejście 4 USD, zapis bufora 5 min 5 USD, zapis bufora 1 h 8 USD, odczyt bufora 0,20 USD, wyjście 20 USD za milion tokenów; [cennik](https://platform.claude.com/docs/en/about-claude/pricing), sprawdzony 2026.11.04). Wyjście obejmuje tokeny rozumowania.

## Bufor (cache) i układ kontekstu

Stała część (instrukcja wariantu i pakiet, około 120 tys. tokenów) jest jednakowa dla wszystkich postaci, więc trafia do bufora raz. Wątek stoi zaraz po niej, przed kartą, więc też jest wspólny: każda nowa wypowiedź trafia do bufora raz, a następna postać odczytuje cały dotychczasowy wątek z bufora. Karta i zdanie o kolejce są na końcu, bez bufora (3-8 tys. tokenów na wywołanie). Bufor ma czas życia 1 godzinę, bo arbiter mówi co około 10 wywołań.

To odstępstwo od kolejności z pakiet-wiedzy.md, część 6 (wariant, pakiet, karta, wątek). Uzasadnienie: przy kolejności z etapu 2 każda postać musi osobno zapisywać w buforze cały wątek po swojej karcie, co według atrapy podnosi koszt przebiegu o około 3-7 USD (około 20-40%). Cel tamtej uwagi ("karta bliżej wypowiedzi") jest zachowany, bo karta stoi teraz tuż przed odpowiedzią. Karta jest w wiadomości systemowej, czyli oddzielona od tekstów innych postaci w wątku. Kolejność z etapu 2 jest dostępna opcją `--uklad etap2`, gdyby recenzja uznała ją za wiążącą.

## Zapis przebiegu

W katalogu `--wyjscie` skrypt zapisuje:

- `zapis.md`: pełny wątek; zaczyna się informacją, że to symulacja, a nie słowa tych osób; każda wypowiedź jest podpisana "Imię Nazwisko (postać symulowana przez AI)" albo "Arbiter (agent AI, nie negocjuje)". Plik jest dopisywany na bieżąco po każdej wypowiedzi, żeby rozmowę dało się śledzić w trakcie przebiegu (uzupełnienie techniczne z [komentarza w issue #46](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6630142744); nie zmienia treści, którą dostają postacie ani arbiter);
- `zapis.jsonl`: jedno wywołanie na linię: tekst, runda, `stop_reason`, `usage`, koszt, suma SHA-256 pełnego zapytania i jego przepis (sumy tekstów stałych, liczba wpisów wątku, zdanie o kolejce), decyzje arbitra, pełny tekst przed ucięciem;
- `teksty/`: dokładne teksty stałe wysłane do modelu (system postaci, system arbitra, karty) i teksty techniczne;
- `ustawienia.json` (model, wysiłek, limity, cennik, wersja repozytorium, suma skryptu, sumy tekstów), `stan.json` (po każdym wywołaniu), `wynik.json`.

## Tryb próbny: wynik

Pomiar 2026.11.04 endpointem `count_tokens` dla `claude-opus-5-5` ([tokeny.json](tokeny.json)):

| Tekst | Tokeny |
|---|---|
| pakiet podstawowy (27 433 słowa) | 118 923 |
| pakiet minimalny | 65 311 |
| instrukcja wariantu (a), (b), (c) | 1 688-1 717 |
| karty postaci (z nagłówkiem) | 3 007 (Hołownia) - 8 011 (Nawrocki) |
| instrukcja arbitra | 7 765 |
| karty źródeł dla arbitra | 56 410 |
| system postaci, wariant (b), pakiet podstawowy | 120 640 |
| system arbitra z kartami źródeł | 183 098 |
| pełne pierwsze zapytanie Nawrockiego | 128 814 |

Pakiet ma 118 923 tokeny wobec 118 529 zmierzonych przez recenzenta etapu 2; różnica to linie z nazwami plików i znaczniki "[...]".

Atrapa (wariant b, skład W1) przeszła trzy scenariusze: "typowy" (głosowanie po 6. rundzie, dodatkowa runda, powtórne głosowanie: 114 wywołań, 103 wypowiedzi postaci, 3 poza kolejnością), "maks" (8 rund, głos poza kolejnością w każdej, dodatkowa runda: 141 wywołań, 128 wypowiedzi postaci; sprawdza też ucięcie zbyt długiej wypowiedzi i odmowę modelu liczoną jako "Pas") i "pas" (wszyscy "Pas" w 1. rundzie: arbiter może tylko zakończyć). Kolejność w każdej rundzie zgadza się z kolejnością otwarcia, także z `--przesuniecie 1`; żadna postać nie mówi więcej niż dwa razy w rundzie. Limit kosztu ustawiony na 5 i 8 USD przerwał przebieg przed przekroczeniem kwoty, a arbiter ogłosił brak porozumienia.

## Szacunek kosztu pierwszego przebiegu

Atrapa liczy `usage` z modelu bufora (odczyt od najdłuższego zapisanego prefiksu, zapis do ostatniego punktu bufora) i z pomiaru tokenów. Niepewne są długość wypowiedzi i liczba tokenów rozumowania, więc podaję zakres. Założenia: wariant (b), skład W1, pakiet podstawowy, arbiter z kartami źródeł, wysiłek `medium`, bufor 1 h, wpisy bufora nie wygasają, wypowiedź arbitra około 200 słów.

| Scenariusz | Wypowiedź postaci | Rozumowanie (postać / arbiter) | Koszt |
|---|---|---|---|
| typowy, 103 wypowiedzi | 160 słów (około 700 tokenów) | 500 / 1 500 | 12,4 USD |
| typowy | 160 słów | **1 500 / 3 000** | **14,8 USD** |
| typowy | 250 słów | 4 000 / 8 000 | 22,7 USD |
| maks, 128 wypowiedzi | 160 słów | 1 500 / 3 000 | 18,2 USD |
| maks | 250 słów | 4 000 / 8 000 | 28,1 USD, czyli przerwanie na limicie 25 USD |

Wynik środkowy: około 15 USD (arbiter 3,4 USD, postacie 11,5 USD: odczyt bufora 3,3, wyjście 4,3, karty bez bufora 2,3, zapis bufora 1,6). Pierwsze wywołanie każdej strony kosztuje najwięcej (zapis pakietu: około 1,0 USD u postaci i 1,5 USD u arbitra), kolejne około 0,10 USD u postaci i 0,19 USD u arbitra. Pakiet minimalny obniża koszt tylko o około 2 USD, bo pakiet i tak jest prawie cały czytany z bufora. Kolejność z etapu 2 (`--uklad etap2`) kosztuje 3-7 USD więcej. Czas przebiegu nie był mierzony; przy 114 wywołaniach po 30-60 sekund to około 1-2 godzin.

Propozycja liczby przebiegów w limicie 100 USD (ocena wykonawcy; decyzja prowadzącego po przebiegu 1, na podstawie kosztu zmierzonego z `usage`):

| Zmierzony koszt przebiegu 1 | Przebiegi W1 w limicie |
|---|---|
| do 11 USD | 9 (pełny plan 3 x 3) |
| 11-14 USD | 7 |
| 14-16,5 USD | 6 (po dwa na wariant) |
| 16,5-25 USD | 4-5, albo tańsze ustawienia: wysiłek `low`, pakiet minimalny |

## Ograniczenia

- Szacunek nie obejmuje ponowień po błędach API ani wygaśnięcia bufora przy przerwach dłuższych niż godzina.
- Atrapa sprawdza mechanikę skryptu, nie zachowanie modelu. Czy arbiter stosuje reguły z arbiter.md, pokaże dopiero przebieg 1.
- Tryb próbny nie wywołał generowania (zgodnie z poleceniem), więc prawdziwa ścieżka `messages.stream` nie była uruchomiona. Kształt zapytań postaci i arbitra (także schemat odpowiedzi arbitra i wiadomość systemowa po wątku) API przyjęło w `count_tokens`.
