# Głosowania Sejmu nad ustawami i uchwałami o TK oraz wyborami sędziów, 2015-2026

- Autor: Sejm Rzeczypospolitej Polskiej (dane z oficjalnego API Sejmu).
- URL: https://api.sejm.gov.pl/sejm/term{N}/votings/{posiedzenie}/{numer}. Każdy wiersz ma własny adres.
- Dostęp: 2026.11.03.
- Lokalizator: kadencja, numer posiedzenia i numer głosowania, podane w kolumnie "Źródło" (np. pos. 1, nr 78 w 8. kadencji).
- Normalizacja: z JSON przepisano datę, godzinę, tytuł punktu (title), temat (topic), liczby za, przeciw, wstrzymanych (yes, no, abstain) i próg (majorityVotes). Teksty są dosłowne; zmieniono tylko typografię (długie myślniki i cudzysłowy na zwykłe znaki). "Za, przeciw, wstrz." to liczba głosów; "próg" to liczba głosów potrzebna do przyjęcia, podana przez Sejm. Rozkład według klubów wyliczono z imiennej listy głosujących (pole votes) w tym samym JSON: za, przeciw, wstrz., nieob. (nieobecny lub niegłosujący). Przy wyborze z listą kilku kandydatów (2026.09.04) podano, na kogo głosował klub. Nazwy klubów jak w API Sejmu.

Karta uzupełnia [głosowania z 2015 roku](glosowania-2015.md), których tu nie powtarzamy (ustawa z 2015.05.27, wybór z 2015.10.08, uchwały z 2015.11.25, wybór z 2015.12.02).

## Jak czytać wyniki

W większości głosowań są dwa kroki: najpierw głosuje się wniosek o odrzucenie projektu, potem "całość projektu". Przyjęcie ustawy lub uchwały to więc wiersz "w całości" albo "nad całością projektu". Wiersz "wniosek o odrzucenie" jest głosowaniem odwrotnym (za = odrzucić). Przy poprawkach Senatu głosowano nad ich odrzuceniem: mała liczba "za" znaczy, że Sejm nie odrzucił poprawki, czyli ją przyjął.

## Najkrócej: jak głosowały główne kluby w głosowaniach końcowych

To zestawienie faktów z tabel poniżej, bez oceny.

- 2015.11.19, ustawa zmieniająca ustawę o TK (pos. 1, nr 78): za 268, przeciw 0. PiS za 229, Kukiz15 za 37. PO (138), Nowoczesna (28) i PSL (16) są w tym głosowaniu oznaczone jako nieobecne lub niegłosujące. We wcześniejszym głosowaniu nad wnioskiem o odrzucenie (nr 66) PiS było przeciw (234), a za głosowały PO 114, N 23, PSL 12.
- 2015.12.22, ustawa zmieniająca ustawę o TK (pos. 6, nr 68): za 235, przeciw 181, wstrz. 4. PiS za 232; PO przeciw 107, Kukiz15 przeciw 34, N przeciw 25, PSL przeciw 14.
- 2016.07.07, ustawa o TK (pos. 22, nr 104): za 238, przeciw 173. PiS za 233; PO przeciw 128, N przeciw 30, PSL przeciw 14. Poprawki Senatu rozpatrzono 2016.07.22 (część C2): większość odrzuceń poprawek miała 0-11 głosów za, wyjątki to nr 87 (300 za) i nr 88 (202 za, 240 przeciw).
- 2016.11.04, ustawa o statusie sędziów TK (pos. 29, nr 66): za 228, przeciw 189, wstrz. 9. Poprawki Senatu rozpatrzono 2016.11.30 (część D2).
- 2016.11.30, ustawa o organizacji i trybie postępowania przed TK (pos. 31, nr 37): za 228, przeciw 200, wstrz. 6. PiS za 222; PO przeciw 123, N przeciw 31, PSL przeciw 15, Kukiz15 przeciw 28.
- 2016.12.13, przepisy wprowadzające (pos. 32, nr 32): za 229, przeciw 198, wstrz. 4. PiS za 225; PO przeciw 122, Kukiz15 przeciw 30, N przeciw 29, PSL przeciw 14.
- 2024.03.06, uchwała w sprawie usunięcia skutków kryzysu konstytucyjnego (pos. 7, nr 8): za 240, przeciw 197. KO za 154, PSL-TD za 27, Polska2050-TD za 33, Lewica za 26; PiS przeciw 177, Konfederacja przeciw 16.
- 2024.07.24, ustawa o TK (pos. 16, nr 12): za 242, przeciw 202. KO za 154, PSL-TD za 31, Polska2050-TD za 31, Lewica za 25; PiS przeciw 180, Konfederacja przeciw 18. Przepisy wprowadzające (nr 15): za 242, przeciw 200, ten sam układ klubów.
- 2026.03.13, uchwała o działaniach dla spełniania przez TK wymogów sądu ustanowionego na mocy prawa (pos. 53, nr 81): za 235, przeciw 197. KO za 152, PSL-TD za 31, Centrum za 15, Polska2050 za 15, Lewica za 19; PiS przeciw 176, Konfederacja przeciw 14.
- 2026.03.13, wybór sędziów TK (nr 125-132): sześcioro kandydatów (Bentkowska, Dziurda, Korwin-Piotrowska, Markiewicz, Szostek, Taborowski) dostało po 236-237 głosów za. Za głosowały KO, PSL-TD, Centrum, Polska2050 i Lewica, przeciw PiS i Konfederacja, a Razem wstrzymało się. Kandydatury Artura Kotowskiego (171 za) i Michała Skwarzyńskiego (172 za) przy progu 213-215 nie uzyskały większości; za nimi głosował głównie PiS.
- 2026.06.11, wybór Sławomira Patyry (pos. 59, nr 69): za 235, przeciw 184, wstrz. 5, próg 213. Kandydatura Artura Kotowskiego (nr 68) dostała 173 głosy za.
- 2026.09.04, wybór sędziego (pos. 64, nr 14): Maciej Berek 226 głosów, Artur Kotowski 184, przeciw wszystkim 27, próg 219. Za Berkiem głosowały KO, PSL-TD, Centrum, Lewica i Polska2050; za Kotowskim PiS, RozwojPlus i Demokracja; Konfederacja przeciw wszystkim.

## Strona sejm.gov.pl

Wzór https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=1&NrGlosowania=78 (dla 10. kadencji Sejm10.nsf) daje przekierowanie (kod 302) na stronę kontroli bezpieczeństwa z weryfikacją hCaptcha. W Chrome (2026.11.03) wyświetliła się tylko ta kontrola, nie głosowanie. Zabezpieczenia nie obchodzono, więc nie potwierdzono, że wzór otwiera właściwe głosowanie z listą klubów i nazwisk. Link "strona" w tabelach to ten wzór, niesprawdzony. Podstawą kopii jest API.

## Luki

- W API nie znaleziono głosowań nad poprawkami Senatu do ustawy o organizacji i trybie postępowania przed TK ani do przepisów wprowadzających (posiedzenia 31-34 Sejmu 8. kadencji). Możliwe, że Senat nie wniósł poprawek, ale nie sprawdzano tego w źródłach Senatu.
- Powiązanie głosowania 2026.03.13 (pos. 53, nr 81) z M.P. 2026 poz. 299 wynika z daty i tematu (druki 2316 i 2330). API głosowań nie podaje numeru M.P. Tak samo głosowanie 2024.03.06 (nr 8, druk 226) i M.P. 2024 poz. 198.
- Daty ustaw z 2016.07.22 i 2016.11.30 (status sędziów) zgadzają się z dniami głosowań nad poprawkami Senatu. To wniosek z dat, nie zapis z API.
- Nie objęto etapów Senatu, podpisu Prezydenta ani publikacji. Karta zawiera tylko głosowania Sejmu.

## Tabele głosowań

### A. Ustawa z 2015.11.19 zmieniająca ustawę o TK (Sejm VIII kadencji)

Sejm 8. kadencji, posiedzenie 1. Punkt porządku dziennego (z API): Pkt 15. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy o zmianie ustawy o Trybunale Konstytucyjnym

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2015.11.19 14:37 | głosowanie nad wnioskiem o przystąpienie do trzeciego czytania projektu ustawy  po doręczeniu zestawienia poprawek bez odsyłania projektu do komisji | 270 | 166 | 1 | 167 | [Sejm 8. kad., pos. 1, nr 47](https://api.sejm.gov.pl/sejm/term8/votings/1/47), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=1&NrGlosowania=47) |
| 2015.11.19 16:56 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy w całości | 151 | 273 | 1 | 274 | [Sejm 8. kad., pos. 1, nr 66](https://api.sejm.gov.pl/sejm/term8/votings/1/66), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=1&NrGlosowania=66) |
| 2015.11.19 17:13 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 20 | 268 | 0 | 0 | 1 | [Sejm 8. kad., pos. 1, nr 78](https://api.sejm.gov.pl/sejm/term8/votings/1/78), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=1&NrGlosowania=78) |

Głosy klubów:

- nr 47: PiS: za 233, nieob. 1; PO: przeciw 124, nieob. 14; Kukiz15: za 35, przeciw 1, wstrz. 1, nieob. 4; N: przeciw 25, nieob. 3; PSL: przeciw 15, nieob. 1; niez.: za 2, przeciw 1
- nr 66: PiS: przeciw 234; PO: za 114, przeciw 1, nieob. 23; Kukiz15: za 1, przeciw 36, wstrz. 1, nieob. 3; N: za 23, nieob. 5; PSL: za 12, nieob. 4; niez.: za 1, przeciw 2
- nr 78: PiS: za 229, nieob. 5; PO: nieob. 138; Kukiz15: za 37, nieob. 4; N: nieob. 28; PSL: nieob. 16; niez.: za 2, nieob. 1

### B. Ustawa z 2015.12.22 zmieniająca ustawę o TK (tzw. naprawcza)

Sejm 8. kadencji, posiedzenie 6. Punkt porządku dziennego (z API): Pkt 8. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy o zmianie ustawy o Trybunale Konstytucyjnym

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2015.12.22 20:15 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy w całości | 195 | 233 | 4 | 234 | [Sejm 8. kad., pos. 6, nr 44](https://api.sejm.gov.pl/sejm/term8/votings/6/44), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=6&NrGlosowania=44) |
| 2015.12.22 22:14 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 144, wraz z przyjętymi poprawkami | 235 | 181 | 4 | 182 | [Sejm 8. kad., pos. 6, nr 68](https://api.sejm.gov.pl/sejm/term8/votings/6/68), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=6&NrGlosowania=68) |

Głosy klubów:

- nr 44: PiS: przeciw 232, nieob. 2; PO: za 119, nieob. 19; Kukiz15: za 35, wstrz. 3, nieob. 2; N: za 26, nieob. 2; PSL: za 14, nieob. 2; niez.: za 1, przeciw 1, wstrz. 1, nieob. 1
- nr 68: PiS: za 232, nieob. 2; PO: przeciw 107, nieob. 31; Kukiz15: za 2, przeciw 34, wstrz. 2, nieob. 2; N: przeciw 25, wstrz. 1, nieob. 2; PSL: przeciw 14, nieob. 2; niez.: za 1, przeciw 1, wstrz. 1, nieob. 1

### C1. Ustawa o TK z 2016.07.22: głosowania w Sejmie 2016.07.07

Sejm 8. kadencji, posiedzenie 22. Punkt porządku dziennego (z API): Pkt 32. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy o Trybunale Konstytucyjnym

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.07.07 10:33 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy w całości | 177 | 230 | 15 | 231 | [Sejm 8. kad., pos. 22, nr 66](https://api.sejm.gov.pl/sejm/term8/votings/22/66), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=22&NrGlosowania=66) |
| 2016.07.07 13:10 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 693 | 238 | 173 | 0 | 174 | [Sejm 8. kad., pos. 22, nr 104](https://api.sejm.gov.pl/sejm/term8/votings/22/104), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=22&NrGlosowania=104) |

Głosy klubów:

- nr 66: PiS: przeciw 224, nieob. 9; PO: za 120, nieob. 17; Kukiz15: za 27, wstrz. 1, nieob. 8; N: za 28, nieob. 2; PSL: za 1, wstrz. 14, nieob. 1; niez.: za 1, przeciw 3; WiS: przeciw 3
- nr 104: PiS: za 233; PO: przeciw 128, nieob. 9; Kukiz15: przeciw 1, nieob. 35; N: przeciw 30; PSL: przeciw 14, nieob. 2; niez.: za 2, nieob. 2; WiS: za 3

### C2. Ustawa o TK z 2016.07.22: poprawki Senatu rozpatrzone 2016.07.22

Sejm 8. kadencji, posiedzenie 23. Punkt porządku dziennego (z API): Pkt 40. porz. dzien. Sprawozdanie Komisji o uchwale Senatu w sprawie ustawy o Trybunale Konstytucyjnym

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.07.22 11:34 | głosowanie nad odrzuceniem wymienionych poprawek | 9 | 415 | 3 | 214 | [Sejm 8. kad., pos. 23, nr 75](https://api.sejm.gov.pl/sejm/term8/votings/23/75), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=75) |
| 2016.07.22 11:39 | głosowanie nad odrzuceniem 2. poprawki | 0 | 438 | 1 | 220 | [Sejm 8. kad., pos. 23, nr 76](https://api.sejm.gov.pl/sejm/term8/votings/23/76), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=76) |
| 2016.07.22 11:47 | głosowanie nad odrzuceniem 3. poprawki | 4 | 298 | 132 | 218 | [Sejm 8. kad., pos. 23, nr 77](https://api.sejm.gov.pl/sejm/term8/votings/23/77), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=77) |
| 2016.07.22 11:51 | głosowanie nad odrzuceniem 4. poprawki | 0 | 435 | 2 | 219 | [Sejm 8. kad., pos. 23, nr 78](https://api.sejm.gov.pl/sejm/term8/votings/23/78), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=78) |
| 2016.07.22 11:53 | głosowanie nad odrzuceniem poprawek 7. i 17. | 1 | 434 | 1 | 219 | [Sejm 8. kad., pos. 23, nr 79](https://api.sejm.gov.pl/sejm/term8/votings/23/79), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=79) |
| 2016.07.22 11:54 | głosowanie nad odrzuceniem poprawek 8., 24. i 26. | 2 | 436 | 1 | 220 | [Sejm 8. kad., pos. 23, nr 80](https://api.sejm.gov.pl/sejm/term8/votings/23/80), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=80) |
| 2016.07.22 11:55 | głosowanie nad odrzuceniem poprawek 9., 11., 14. i 22. | 1 | 435 | 1 | 219 | [Sejm 8. kad., pos. 23, nr 81](https://api.sejm.gov.pl/sejm/term8/votings/23/81), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=81) |
| 2016.07.22 11:55 | głosowanie nad odrzuceniem 10. poprawki | 11 | 421 | 1 | 217 | [Sejm 8. kad., pos. 23, nr 82](https://api.sejm.gov.pl/sejm/term8/votings/23/82), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=82) |
| 2016.07.22 11:56 | głosowanie nad odrzuceniem 12. poprawki | 0 | 441 | 1 | 222 | [Sejm 8. kad., pos. 23, nr 83](https://api.sejm.gov.pl/sejm/term8/votings/23/83), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=83) |
| 2016.07.22 11:56 | głosowanie nad odrzuceniem 13. poprawki | 0 | 316 | 127 | 222 | [Sejm 8. kad., pos. 23, nr 84](https://api.sejm.gov.pl/sejm/term8/votings/23/84), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=84) |
| 2016.07.22 11:57 | głosowanie nad odrzuceniem 18. poprawki | 0 | 440 | 1 | 221 | [Sejm 8. kad., pos. 23, nr 85](https://api.sejm.gov.pl/sejm/term8/votings/23/85), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=85) |
| 2016.07.22 11:57 | głosowanie nad odrzuceniem 23. poprawki | 3 | 439 | 1 | 222 | [Sejm 8. kad., pos. 23, nr 86](https://api.sejm.gov.pl/sejm/term8/votings/23/86), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=86) |
| 2016.07.22 11:58 | głosowanie nad odrzuceniem 25. poprawki | 300 | 141 | 2 | 222 | [Sejm 8. kad., pos. 23, nr 87](https://api.sejm.gov.pl/sejm/term8/votings/23/87), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=87) |
| 2016.07.22 11:59 | głosowanie nad odrzuceniem 27. poprawki | 202 | 240 | 1 | 222 | [Sejm 8. kad., pos. 23, nr 88](https://api.sejm.gov.pl/sejm/term8/votings/23/88), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=23&NrGlosowania=88) |

Głosy klubów:

- nr 75: PiS: przeciw 221, nieob. 13; PO: za 6, przeciw 120, nieob. 8; Kukiz15: przeciw 27, wstrz. 2, nieob. 7; N: przeciw 29, nieob. 1; PSL: za 3, przeciw 10, nieob. 3; niez.: przeciw 5, wstrz. 1, nieob. 1; WiS: przeciw 3
- nr 76: PiS: przeciw 228, nieob. 6; PO: przeciw 128, nieob. 6; Kukiz15: przeciw 31, wstrz. 1, nieob. 4; N: przeciw 30; PSL: przeciw 13, nieob. 3; niez.: przeciw 5, nieob. 2; WiS: przeciw 3
- nr 77: PiS: przeciw 222, nieob. 12; PO: za 1, przeciw 24, wstrz. 103, nieob. 6; Kukiz15: za 1, przeciw 31, wstrz. 1, nieob. 3; N: za 1, przeciw 1, wstrz. 26, nieob. 2; PSL: za 1, przeciw 13, nieob. 2; niez.: przeciw 4, wstrz. 2, nieob. 1; WiS: przeciw 3
- nr 78: PiS: przeciw 225, nieob. 9; PO: przeciw 127, wstrz. 1, nieob. 6; Kukiz15: przeciw 31, wstrz. 1, nieob. 4; N: przeciw 30; PSL: przeciw 14, nieob. 2; niez.: przeciw 5, nieob. 2; WiS: przeciw 3
- nr 79: PiS: za 1, przeciw 224, nieob. 9; PO: przeciw 128, nieob. 6; Kukiz15: przeciw 31, wstrz. 1, nieob. 4; N: przeciw 29, nieob. 1; PSL: przeciw 14, nieob. 2; niez.: przeciw 5, nieob. 2; WiS: przeciw 3
- nr 80: PiS: za 2, przeciw 225, nieob. 7; PO: przeciw 129, nieob. 5; Kukiz15: przeciw 31, wstrz. 1, nieob. 4; N: przeciw 29, nieob. 1; PSL: przeciw 14, nieob. 2; niez.: przeciw 5, nieob. 2; WiS: przeciw 3
- nr 81: PiS: za 1, przeciw 226, nieob. 7; PO: przeciw 128, nieob. 6; Kukiz15: przeciw 31, wstrz. 1, nieob. 4; N: przeciw 27, nieob. 3; PSL: przeciw 14, nieob. 2; niez.: przeciw 6, nieob. 1; WiS: przeciw 3
- nr 82: PiS: przeciw 227, nieob. 7; PO: przeciw 124, nieob. 10; Kukiz15: przeciw 29, wstrz. 1, nieob. 6; N: przeciw 29, nieob. 1; PSL: za 11, przeciw 3, nieob. 2; niez.: przeciw 6, nieob. 1; WiS: przeciw 3
- nr 83: PiS: przeciw 229, nieob. 5; PO: przeciw 127, nieob. 7; Kukiz15: przeciw 32, wstrz. 1, nieob. 3; N: przeciw 30; PSL: przeciw 14, nieob. 2; niez.: przeciw 6, nieob. 1; WiS: przeciw 3
- nr 84: PiS: przeciw 229, nieob. 5; PO: przeciw 33, wstrz. 95, nieob. 6; Kukiz15: przeciw 32, wstrz. 1, nieob. 3; N: przeciw 1, wstrz. 29; PSL: przeciw 14, nieob. 2; niez.: przeciw 4, wstrz. 2, nieob. 1; WiS: przeciw 3
- nr 85: PiS: przeciw 230, nieob. 4; PO: przeciw 130, nieob. 4; Kukiz15: przeciw 30, wstrz. 1, nieob. 5; N: przeciw 27, nieob. 3; PSL: przeciw 14, nieob. 2; niez.: przeciw 6, nieob. 1; WiS: przeciw 3
- nr 86: PiS: przeciw 230, nieob. 4; PO: przeciw 127, nieob. 7; Kukiz15: za 2, przeciw 30, wstrz. 1, nieob. 3; N: za 1, przeciw 29; PSL: przeciw 14, nieob. 2; niez.: przeciw 6, nieob. 1; WiS: przeciw 3
- nr 87: PiS: za 228, nieob. 6; PO: za 1, przeciw 129, nieob. 4; Kukiz15: za 31, wstrz. 1, nieob. 4; N: za 27, przeciw 2, wstrz. 1; PSL: za 10, przeciw 4, nieob. 2; niez.: za 1, przeciw 5, nieob. 1; WiS: za 2, przeciw 1
- nr 88: PiS: przeciw 229, nieob. 5; PO: za 125, przeciw 5, nieob. 4; Kukiz15: za 30, wstrz. 1, nieob. 5; N: za 30; PSL: za 13, przeciw 1, nieob. 2; niez.: za 4, przeciw 2, nieob. 1; WiS: przeciw 3

### D1. Ustawa o statusie sędziów TK: głosowania 2016.11.04

Sejm 8. kadencji, posiedzenie 29. Punkt porządku dziennego (z API): Pkt 7. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy o statusie sędziów Trybunału Konstytucyjnego

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.11.04 13:43 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy oraz 1. wniosku mniejszości | 176 | 218 | 1 | 219 | [Sejm 8. kad., pos. 29, nr 45](https://api.sejm.gov.pl/sejm/term8/votings/29/45), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=29&NrGlosowania=45) |
| 2016.11.04 14:42 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 920, wraz z przyjętymi poprawkami | 228 | 189 | 9 | 190 | [Sejm 8. kad., pos. 29, nr 66](https://api.sejm.gov.pl/sejm/term8/votings/29/66), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=29&NrGlosowania=66) |

Głosy klubów:

- nr 45: PiS: za 1, przeciw 214, nieob. 19; PO: za 116, nieob. 17; Kukiz15: za 23, nieob. 13; N: za 22, nieob. 8; PSL: za 11, nieob. 5; niez.: za 2, przeciw 1, wstrz. 1; ED: za 1, nieob. 3; WiS: przeciw 3
- nr 66: PiS: za 222, nieob. 12; PO: przeciw 124, nieob. 9; Kukiz15: za 1, przeciw 23, wstrz. 9, nieob. 3; N: przeciw 27, nieob. 3; PSL: przeciw 11, nieob. 5; niez.: za 2, przeciw 2; ED: przeciw 2, nieob. 2; WiS: za 3

### D2. Ustawa o statusie sędziów TK: poprawki Senatu rozpatrzone 2016.11.30

Sejm 8. kadencji, posiedzenie 31. Punkt porządku dziennego (z API): Pkt 14. porz. dzien. Sprawozdanie Komisji o uchwale Senatu w sprawie ustawy o statusie sędziów Trybunału Konstytucyjnego

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.11.30 12:18 | głosowanie nad odrzuceniem poprawek 1. i 4. | 16 | 370 | 16 | 202 | [Sejm 8. kad., pos. 31, nr 92](https://api.sejm.gov.pl/sejm/term8/votings/31/92), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=92) |
| 2016.11.30 12:19 | głosowanie nad odrzuceniem 2. poprawki | 32 | 388 | 0 | 211 | [Sejm 8. kad., pos. 31, nr 93](https://api.sejm.gov.pl/sejm/term8/votings/31/93), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=93) |
| 2016.11.30 12:19 | głosowanie nad odrzuceniem 3. poprawki Senatu | 30 | 390 | 0 | 211 | [Sejm 8. kad., pos. 31, nr 94](https://api.sejm.gov.pl/sejm/term8/votings/31/94), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=94) |
| 2016.11.30 12:20 | głosowanie nad odrzuceniem 5. poprawki | 29 | 394 | 0 | 212 | [Sejm 8. kad., pos. 31, nr 95](https://api.sejm.gov.pl/sejm/term8/votings/31/95), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=95) |
| 2016.11.30 12:20 | głosowanie nad odrzuceniem 6. poprawki | 1 | 395 | 31 | 214 | [Sejm 8. kad., pos. 31, nr 96](https://api.sejm.gov.pl/sejm/term8/votings/31/96), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=96) |
| 2016.11.30 12:25 | głosowanie nad odrzuceniem 7. poprawki | 4 | 423 | 0 | 214 | [Sejm 8. kad., pos. 31, nr 97](https://api.sejm.gov.pl/sejm/term8/votings/31/97), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=97) |
| 2016.11.30 12:26 | głosowanie nad odrzuceniem 8. poprawki | 0 | 389 | 28 | 209 | [Sejm 8. kad., pos. 31, nr 98](https://api.sejm.gov.pl/sejm/term8/votings/31/98), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=98) |
| 2016.11.30 12:31 | głosowanie nad odrzuceniem 9. poprawki | 0 | 397 | 26 | 212 | [Sejm 8. kad., pos. 31, nr 99](https://api.sejm.gov.pl/sejm/term8/votings/31/99), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=99) |
| 2016.11.30 12:31 | głosowanie nad odrzuceniem 10. poprawki | 1 | 397 | 28 | 214 | [Sejm 8. kad., pos. 31, nr 100](https://api.sejm.gov.pl/sejm/term8/votings/31/100), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=100) |
| 2016.11.30 12:35 | głosowanie nad odrzuceniem 11. poprawki | 137 | 287 | 1 | 213 | [Sejm 8. kad., pos. 31, nr 101](https://api.sejm.gov.pl/sejm/term8/votings/31/101), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=101) |

Głosy klubów:

- nr 92: PiS: za 1, przeciw 195, wstrz. 1, nieob. 37; PO: za 1, przeciw 117, nieob. 14; Kukiz15: za 1, przeciw 34, nieob. 1; N: za 13, przeciw 1, wstrz. 15, nieob. 2; PSL: przeciw 14, nieob. 2; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 93: PiS: przeciw 215, nieob. 19; PO: przeciw 118, nieob. 14; Kukiz15: za 1, przeciw 34, nieob. 1; N: za 31; PSL: przeciw 14, nieob. 2; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 1, nieob. 2
- nr 94: PiS: przeciw 213, nieob. 21; PO: przeciw 120, nieob. 12; Kukiz15: za 1, przeciw 34, nieob. 1; N: za 28, przeciw 2, nieob. 1; PSL: za 1, przeciw 12, nieob. 3; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 95: PiS: przeciw 219, nieob. 15; PO: przeciw 119, nieob. 13; Kukiz15: za 1, przeciw 33, nieob. 2; N: za 28, przeciw 3; PSL: przeciw 13, nieob. 3; niez.: przeciw 4; ED: nieob. 4; WiS: przeciw 3
- nr 96: PiS: przeciw 219, nieob. 15; PO: przeciw 119, nieob. 13; Kukiz15: przeciw 34, wstrz. 1, nieob. 1; N: za 1, wstrz. 30; PSL: przeciw 14, nieob. 2; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 97: PiS: przeciw 219, nieob. 15; PO: za 3, przeciw 116, nieob. 13; Kukiz15: przeciw 36; N: za 1, przeciw 28, nieob. 2; PSL: przeciw 15, nieob. 1; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 98: PiS: przeciw 212, nieob. 22; PO: przeciw 117, nieob. 15; Kukiz15: przeciw 35, wstrz. 1; N: przeciw 2, wstrz. 27, nieob. 2; PSL: przeciw 15, nieob. 1; niez.: przeciw 3, nieob. 1; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 99: PiS: przeciw 216, nieob. 18; PO: przeciw 119, nieob. 13; Kukiz15: przeciw 35, wstrz. 1; N: przeciw 3, wstrz. 25, nieob. 3; PSL: przeciw 15, nieob. 1; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3
- nr 100: PiS: przeciw 219, nieob. 15; PO: przeciw 118, nieob. 14; Kukiz15: przeciw 35, wstrz. 1; N: za 1, przeciw 2, wstrz. 27, nieob. 1; PSL: przeciw 15, nieob. 1; niez.: przeciw 4; ED: przeciw 1, nieob. 3; WiS: przeciw 3
- nr 101: PiS: przeciw 218, nieob. 16; PO: za 97, przeciw 23, nieob. 12; Kukiz15: za 2, przeciw 33, wstrz. 1; N: za 28, nieob. 3; PSL: za 10, przeciw 4, nieob. 2; niez.: przeciw 4; ED: przeciw 2, nieob. 2; WiS: przeciw 3

### D3. Ustawa o organizacji i trybie postępowania przed TK: głosowania 2016.11.30

Sejm 8. kadencji, posiedzenie 31. Punkt porządku dziennego (z API): Pkt 7. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy o organizacji i trybie postępowania przed Trybunałem Konstytucyjnym

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.11.30 09:36 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy w całości | 194 | 231 | 7 | 232 | [Sejm 8. kad., pos. 31, nr 20](https://api.sejm.gov.pl/sejm/term8/votings/31/20), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=20) |
| 2016.11.30 10:21 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 1052, wraz z przyjętymi poprawkami | 228 | 200 | 6 | 201 | [Sejm 8. kad., pos. 31, nr 37](https://api.sejm.gov.pl/sejm/term8/votings/31/37), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=31&NrGlosowania=37) |

Głosy klubów:

- nr 20: PiS: przeciw 224, nieob. 10; PO: za 121, nieob. 11; Kukiz15: za 25, przeciw 1, wstrz. 6, nieob. 4; N: za 30, przeciw 1; PSL: za 15, nieob. 1; niez.: za 1, przeciw 2, wstrz. 1; ED: za 2, nieob. 2; WiS: przeciw 3
- nr 37: PiS: za 222, nieob. 12; PO: przeciw 123, nieob. 9; Kukiz15: za 1, przeciw 28, wstrz. 5, nieob. 2; N: przeciw 31; PSL: przeciw 15, nieob. 1; niez.: za 2, przeciw 1, wstrz. 1; ED: przeciw 2, nieob. 2; WiS: za 3

### D4. Przepisy wprowadzające ustawę o organizacji i trybie postępowania przed TK: głosowania 2016.12.13

Sejm 8. kadencji, posiedzenie 32. Punkt porządku dziennego (z API): Pkt 4. porz. dzien. Sprawozdanie Komisji o poselskim projekcie ustawy - Przepisy wprowadzające ustawę o organizacji i trybie postępowania przed Trybunałem Konstytucyjnym oraz ustawę o statusie sędziów Trybunału Konstytucyjnego

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2016.12.13 20:40 | głosowanie nad przyjęciem wniosku o odrzucenie projektu ustawy w całości | 196 | 224 | 3 | 225 | [Sejm 8. kad., pos. 32, nr 9](https://api.sejm.gov.pl/sejm/term8/votings/32/9), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=32&NrGlosowania=9) |
| 2016.12.13 21:21 | głosowanie nad przyjęciem w całości projektu ustawy w brzmieniu z druku nr 1115, wraz z przyjętymi poprawkami | 229 | 198 | 4 | 199 | [Sejm 8. kad., pos. 32, nr 32](https://api.sejm.gov.pl/sejm/term8/votings/32/32), [strona](https://www.sejm.gov.pl/Sejm8.nsf/agent.xsp?symbol=glosowania&NrKadencji=8&NrPosiedzenia=32&NrGlosowania=32) |

Głosy klubów:

- nr 9: PiS: przeciw 221, nieob. 13; PO: za 122, nieob. 10; Kukiz15: za 30, wstrz. 2, nieob. 4; N: za 27, nieob. 4; PSL: za 14, nieob. 2; niez.: za 1, przeciw 1, wstrz. 1, nieob. 1; ED: za 2, nieob. 2; WiS: przeciw 2, nieob. 1
- nr 32: PiS: za 225, nieob. 9; PO: przeciw 122, nieob. 10; Kukiz15: przeciw 30, wstrz. 3, nieob. 3; N: przeciw 29, nieob. 2; PSL: przeciw 14, nieob. 2; niez.: za 1, przeciw 1, wstrz. 1, nieob. 1; ED: przeciw 2, nieob. 2; WiS: za 3

### E. Uchwała Sejmu z 2024.03.06 w sprawie usunięcia skutków kryzysu konstytucyjnego

Sejm 10. kadencji, posiedzenie 7. Punkt porządku dziennego (z API): Pkt. 3 Pierwsze czytanie poselskiego projektu uchwały w sprawie usunięcia skutków kryzysu konstytucyjnego lat 2015-2023 w kontekście działalności Trybunału Konstytucyjnego (druk nr 226)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2024.03.06 17:58 | wniosek o odrzucenie projektu w całości | 197 | 239 | 0 | 240 | [Sejm 10. kad., pos. 7, nr 7](https://api.sejm.gov.pl/sejm/term10/votings/7/7), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=7&NrGlosowania=7) |
| 2024.03.06 17:59 | głosowanie nad całością projektu. | 240 | 197 | 0 | 198 | [Sejm 10. kad., pos. 7, nr 8](https://api.sejm.gov.pl/sejm/term10/votings/7/8), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=7&NrGlosowania=8) |

Głosy klubów:

- nr 7: PiS: za 177, nieob. 12; KO: przeciw 153, nieob. 4; PSL-TD: przeciw 27, nieob. 5; Konfederacja: za 16, nieob. 2; Polska2050-TD: przeciw 33; Lewica: przeciw 26; Kukiz15: za 3; niez.: za 1
- nr 8: PiS: przeciw 177, nieob. 12; KO: za 154, nieob. 3; PSL-TD: za 27, nieob. 5; Konfederacja: przeciw 16, nieob. 2; Polska2050-TD: za 33; Lewica: za 26; Kukiz15: przeciw 3; niez.: przeciw 1

### F1. Ustawa o TK: głosowania 2024.07.24

Sejm 10. kadencji, posiedzenie 16. Punkt porządku dziennego (z API): Pkt. 2 Sprawozdanie Komisji o poselskim projekcie ustawy o Trybunale Konstytucyjnym (druki nr 253, 543 i 543-A)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2024.07.24 17:02 | wniosek o odrzucenie w całości projektu. | 202 | 242 | 0 | 243 | [Sejm 10. kad., pos. 16, nr 8](https://api.sejm.gov.pl/sejm/term10/votings/16/8), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=16&NrGlosowania=8) |
| 2024.07.24 17:05 | głosowanie nad całością projektu. | 242 | 202 | 0 | 203 | [Sejm 10. kad., pos. 16, nr 12](https://api.sejm.gov.pl/sejm/term10/votings/16/12), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=16&NrGlosowania=12) |

Głosy klubów:

- nr 8: PiS: za 180, nieob. 10; KO: przeciw 154, nieob. 3; Kukiz15: za 4; PSL-TD: przeciw 31, nieob. 1; Konfederacja: za 18; Polska2050-TD: przeciw 31, nieob. 1; Lewica: przeciw 25, nieob. 1; niez.: przeciw 1
- nr 12: PiS: przeciw 180, nieob. 10; KO: za 154, nieob. 3; Kukiz15: przeciw 4; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 18; Polska2050-TD: za 31, nieob. 1; Lewica: za 25, nieob. 1; niez.: za 1

### F2. Przepisy wprowadzające ustawę o TK: głosowania 2024.07.24

Sejm 10. kadencji, posiedzenie 16. Punkt porządku dziennego (z API): Pkt. 3 Sprawozdanie Komisji o poselskim projekcie ustawy - Przepisy wprowadzające ustawę o Trybunale Konstytucyjnym (druki nr 254, 544 i 544-A)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2024.07.24 17:07 | wniosek o odrzucenie w całości projektu. | 200 | 241 | 0 | 242 | [Sejm 10. kad., pos. 16, nr 13](https://api.sejm.gov.pl/sejm/term10/votings/16/13), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=16&NrGlosowania=13) |
| 2024.07.24 17:08 | głosowanie nad całością projektu. | 242 | 200 | 0 | 201 | [Sejm 10. kad., pos. 16, nr 15](https://api.sejm.gov.pl/sejm/term10/votings/16/15), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=16&NrGlosowania=15) |

Głosy klubów:

- nr 13: PiS: za 178, nieob. 12; KO: przeciw 154, nieob. 3; Kukiz15: za 4; PSL-TD: przeciw 31, nieob. 1; Konfederacja: za 17, nieob. 1; Polska2050-TD: przeciw 31, nieob. 1; Lewica: za 1, przeciw 24, nieob. 1; niez.: przeciw 1
- nr 15: PiS: przeciw 178, nieob. 12; KO: za 154, nieob. 3; Kukiz15: przeciw 4; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 18; Polska2050-TD: za 31, nieob. 1; Lewica: za 25, nieob. 1; niez.: za 1

### G1. Uchwała Sejmu z 2026.03.13 o wymogach sądu ustanowionego na mocy prawa dla TK

Sejm 10. kadencji, posiedzenie 53. Punkt porządku dziennego (z API): Pkt. 12 Sprawozdanie Komisji o poselskim projekcie uchwały w sprawie działań niezbędnych do zapewnienia spełniania przez Trybunał Konstytucyjny wymogów sądu ustanowionego na mocy prawa, niezawisłego i bezstronnego (druki nr 2316, 2330 i 2330-A)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2026.03.13 12:10 | wniosek o odrzucenie w całości projektu. | 198 | 232 | 0 | 233 | [Sejm 10. kad., pos. 53, nr 79](https://api.sejm.gov.pl/sejm/term10/votings/53/79), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=79) |
| 2026.03.13 12:11 | głosowanie nad całością projektu. | 235 | 197 | 0 | 198 | [Sejm 10. kad., pos. 53, nr 81](https://api.sejm.gov.pl/sejm/term10/votings/53/81), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=81) |

Głosy klubów:

- nr 79: PiS: za 176, nieob. 12; KO: przeciw 151, nieob. 5; Demokracja: za 2, nieob. 2; PSL-TD: przeciw 30, nieob. 2; Konfederacja: za 15, nieob. 1; Centrum: przeciw 15; Polska2050: przeciw 15; Lewica: przeciw 18, nieob. 3; Konfederacja_KP: za 3; niez.: za 2, przeciw 3, nieob. 1; Razem: nieob. 4
- nr 81: PiS: przeciw 176, nieob. 12; KO: za 152, nieob. 4; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 14, nieob. 2; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 3; niez.: za 3, przeciw 2, nieob. 1; Razem: nieob. 4

### G2. Wybór sędziów TK 2026.03.13

Sejm 10. kadencji, posiedzenie 53. Punkt porządku dziennego (z API): Pkt. 29 Wybór sędziów Trybunału Konstytucyjnego (druki nr 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2344, 2345, 2346, 2347, 2348, 2349, 2350 i 2351)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2026.03.13 13:33 | głosowanie nad kandydaturą Pani Magdaleny Bentkowskiej na stanowisko sędziego Trybunału Konstytucyjnego | 236 | 186 | 4 | 214 | [Sejm 10. kad., pos. 53, nr 125](https://api.sejm.gov.pl/sejm/term10/votings/53/125), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=125) |
| 2026.03.13 13:34 | głosowanie nad kandydaturą Pana Marcina Dziurdy na stanowisko sędziego Trybunału Konstytucyjnego | 237 | 182 | 6 | 213 | [Sejm 10. kad., pos. 53, nr 126](https://api.sejm.gov.pl/sejm/term10/votings/53/126), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=126) |
| 2026.03.13 13:35 | głosowanie nad kandydaturą Pani Anny Korwin-Piotrowskiej na stanowisko sędziego Trybunału Konstytucyjnego | 236 | 185 | 4 | 213 | [Sejm 10. kad., pos. 53, nr 127](https://api.sejm.gov.pl/sejm/term10/votings/53/127), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=127) |
| 2026.03.13 13:36 | głosowanie nad kandydaturą Pana Artura Kotowskiego na stanowisko sędziego Trybunału Konstytucyjnego | 171 | 249 | 4 | 213 | [Sejm 10. kad., pos. 53, nr 128](https://api.sejm.gov.pl/sejm/term10/votings/53/128), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=128) |
| 2026.03.13 13:36 | głosowanie nad kandydaturą Pana Krystiana Markiewicza na stanowisko sędziego Trybunału Konstytucyjnego | 236 | 187 | 4 | 214 | [Sejm 10. kad., pos. 53, nr 129](https://api.sejm.gov.pl/sejm/term10/votings/53/129), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=129) |
| 2026.03.13 13:37 | głosowanie nad kandydaturą Pana Michała Skwarzyńskiego na stanowisko sędziego Trybunału Konstytucyjnego | 172 | 253 | 4 | 215 | [Sejm 10. kad., pos. 53, nr 130](https://api.sejm.gov.pl/sejm/term10/votings/53/130), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=130) |
| 2026.03.13 13:38 | głosowanie nad kandydaturą Pana Dariusza Szostka na stanowisko sędziego Trybunału Konstytucyjnego | 237 | 185 | 4 | 214 | [Sejm 10. kad., pos. 53, nr 131](https://api.sejm.gov.pl/sejm/term10/votings/53/131), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=131) |
| 2026.03.13 13:39 | głosowanie nad kandydaturą Pana Macieja Taborowskiego na stanowisko sędziego Trybunału Konstytucyjnego | 237 | 185 | 4 | 214 | [Sejm 10. kad., pos. 53, nr 132](https://api.sejm.gov.pl/sejm/term10/votings/53/132), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=53&NrGlosowania=132) |

Głosy klubów:

- nr 125: PiS: przeciw 170, nieob. 18; KO: za 153, nieob. 3; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 11, nieob. 5; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4
- nr 126: PiS: przeciw 168, wstrz. 1, nieob. 19; KO: za 153, nieob. 3; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: za 1, przeciw 9, wstrz. 1, nieob. 5; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4
- nr 127: PiS: przeciw 169, nieob. 19; KO: za 153, nieob. 3; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 11, nieob. 5; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4
- nr 128: PiS: za 169, nieob. 19; KO: przeciw 153, nieob. 3; Demokracja: za 2, nieob. 2; PSL-TD: przeciw 30, nieob. 2; Konfederacja: przeciw 11, nieob. 5; Centrum: przeciw 15; Polska2050: przeciw 15; Lewica: przeciw 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: przeciw 4, nieob. 2; Razem: wstrz. 4
- nr 129: PiS: przeciw 169, nieob. 19; KO: za 153, nieob. 3; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: przeciw 13, nieob. 3; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4
- nr 130: PiS: za 170, nieob. 18; KO: przeciw 154, nieob. 2; Demokracja: za 2, nieob. 2; PSL-TD: przeciw 31, nieob. 1; Konfederacja: przeciw 13, nieob. 3; Centrum: przeciw 15; Polska2050: przeciw 15; Lewica: przeciw 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: przeciw 4, nieob. 2; Razem: wstrz. 4
- nr 131: PiS: przeciw 168, nieob. 20; KO: za 153, nieob. 3; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 31, nieob. 1; Konfederacja: za 1, przeciw 12, nieob. 3; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4
- nr 132: PiS: za 1, przeciw 167, nieob. 20; KO: za 154, nieob. 2; Demokracja: przeciw 2, nieob. 2; PSL-TD: za 30, nieob. 2; Konfederacja: przeciw 13, nieob. 3; Centrum: za 15; Polska2050: za 15; Lewica: za 19, nieob. 2; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 1, nieob. 2; Razem: wstrz. 4

### G3. Wybór sędziego TK 2026.06.11

Sejm 10. kadencji, posiedzenie 59. Punkt porządku dziennego (z API): Pkt. 27 Wybór sędziego Trybunału Konstytucyjnego (druki nr 2618, 2619, 2634 i 2635)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2026.06.11 13:32 | głosowanie nad kandydaturą Artura Kotowskiego na stanowisko sędziego Trybunału Konstytucyjnego | 173 | 245 | 6 | 213 | [Sejm 10. kad., pos. 59, nr 68](https://api.sejm.gov.pl/sejm/term10/votings/59/68), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=59&NrGlosowania=68) |
| 2026.06.11 13:33 | głosowanie nad kandydaturą Sławomira Patyry na stanowisko sędziego Trybunału Konstytucyjnego | 235 | 184 | 5 | 213 | [Sejm 10. kad., pos. 59, nr 69](https://api.sejm.gov.pl/sejm/term10/votings/59/69), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=59&NrGlosowania=69) |

Głosy klubów:

- nr 68: PiS: za 167, nieob. 19; KO: przeciw 154, nieob. 2; Demokracja: za 2, wstrz. 1, nieob. 1; PSL-TD: przeciw 29, nieob. 3; Konfederacja: przeciw 9, nieob. 7; Centrum: przeciw 14, nieob. 1; Lewica: przeciw 21; Polska2050: przeciw 14, nieob. 1; Konfederacja_KP: za 1, przeciw 1, nieob. 1; niez.: za 3, przeciw 3, wstrz. 1, nieob. 1; Razem: wstrz. 4
- nr 69: PiS: przeciw 167, nieob. 19; KO: za 154, nieob. 2; Demokracja: przeciw 3, nieob. 1; PSL-TD: za 29, nieob. 3; Konfederacja: przeciw 9, nieob. 7; Centrum: za 14, nieob. 1; Lewica: za 21; Polska2050: za 14, nieob. 1; Konfederacja_KP: przeciw 2, nieob. 1; niez.: za 3, przeciw 3, wstrz. 1, nieob. 1; Razem: wstrz. 4

### G4. Wybór sędziego TK 2026.09.04

Sejm 10. kadencji, posiedzenie 64. Punkt porządku dziennego (z API): Wybór sędziego Trybunału Konstytucyjnego (druki nr 3005, 3006, 3057 i 3058)

| Data i godzina | Temat (z API) | Za | Przeciw | Wstrz. | Próg | Źródło |
|---|---|---|---|---|---|---|
| 2026.09.04 10:25 | Wybór sędziego Trybunału Konstytucyjnego | Berek Maciej 226, Kotowski Artur 184 | przeciw wszystkim 27 | 0 | 219 | [Sejm 10. kad., pos. 64, nr 14](https://api.sejm.gov.pl/sejm/term10/votings/64/14), [strona](https://www.sejm.gov.pl/Sejm10.nsf/agent.xsp?symbol=glosowania&NrKadencji=10&NrPosiedzenia=64&NrGlosowania=14) |

Głosy klubów:

- nr 14: PiS: za Kotowski Artur 143, nieob. 3; KO: za Berek Maciej 154, nieob. 1, przeciw wszystkim 1; Demokracja: za Kotowski Artur 2, nieob. 1, przeciw wszystkim 1; RozwojPlus: za Kotowski Artur 38, nieob. 3; PSL-TD: za Berek Maciej 30, nieob. 2; Konfederacja: nieob. 1, przeciw wszystkim 15; Centrum: za Berek Maciej 12, nieob. 2, przeciw wszystkim 1; Lewica: za Berek Maciej 17, nieob. 3, przeciw wszystkim 1; Polska2050: za Berek Maciej 11, nieob. 3, przeciw wszystkim 1; Konfederacja_KP: nieob. 1, przeciw wszystkim 2; niez.: za Berek Maciej 2, za Kotowski Artur 1, nieob. 2, przeciw wszystkim 2; Razem: nieob. 1, przeciw wszystkim 3
