> Etap 2 [symulacji negocjacji (issue #46)](https://github.com/gebawkubel/trybunal/issues/46). Napisał Claude Fable 5.1 (wysoki wysiłek rozumowania, agent Claude Code) na repozytorium w wersji 70b735a (gałąź symulacja-baza-etap-2), według [treści issue](polecenie-issue.md) i [wiadomości technicznej](wiadomosc.md). Zakazy (internet, zmiany, inne katalogi) były w wiadomości, nie wymuszone technicznie. To robocze materiały symulacji: oceny i wnioski autora etapu, nie ustalenia projektu; postacie są symulowane przez AI. Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `ac458f6ffa259d9d5ae80500583efb14e9744ef6735976fd6ee4e9e77b8d66cb`.

---

# Etap 2 symulacji negocjacji o TK (issue #46): pakiet wiedzy wspólny dla wszystkich postaci

Wykonane na polecenie z issue #46 (plik `issue-46.md`, treść z komentarzami). Materiał: repozytorium w wersji 70b735a, bez internetu. Podstawa: `badania/symulacja/etap-1.md` (wersja 4, PASS w rundzie 4), skład podstawowy W1. Nie czytałem plików `badania/rekomendacje-modeli.md`, `badania/rekomendacje/`, `badania/bilans-propozycji.md` ani `badania/odpowiedz.md`; z `badania/odpowiedzialnosc-i-rozwiazania.md` odczytałem tylko nagłówek i pierwsze wiersze tabeli, żeby uzasadnić wyłączenie; z `badania/scenariusze-naprawy.md` pominąłem część "Scenariusze z analiz AI".

Oznaczenia: fakt ma w nawiasie nazwę pliku. Zdania "ocena wykonawcy" to moje wnioski, nie ustalenia repozytorium. Numery linii odnoszą się do plików w wersji 70b735a; skrypt etapu 3 wycina fragmenty po tych numerach i liczy sumy SHA-256 gotowych tekstów przed pierwszym przebiegiem.

## 1. Zasady doboru

1. Pakiet zawiera wyłącznie fakty, stanowiska stron w ich własnych słowach, treść propozycji i warunki prawne. Postacie mają z niego wiedzieć, co się stało, kto czego chce, ile kto ma głosów i czego wymaga prawo.
2. Pakiet nie zawiera: rekomendacji modeli, bilansu propozycji, odpowiedzi z issue #38, ocen odpowiedzialności, sekcji "Scenariusze z analiz AI" ani zdań, które w zachowanych plikach odsyłają do tych analiz. Nie zawiera też dokumentu etapu 1, bo jego oceny, kto jest "niezbędny" i kto ma "największą swobodę ruchu", zakotwiczyłyby rozmowę; rachunek progów trafia do instrukcji arbitra.
3. Każda postać dostaje ten sam pakiet. Karta prywatna (osobny plik) dodaje tylko to, co dotyczy danej osoby.
4. Stan wiedzy: 2026.11.04 (najnowszy materiał: wywiad Krzysztofa Bosaka z rana 2026.11.04 i notatka o posiedzeniu komisji z 2026.04.28, oba zrecenzowane, w repozytorium w wersji 70b735a).
5. Fragmenty wycinane z plików zachowują nagłówki i tabele w oryginalnym brzmieniu. Linki wewnętrzne i zewnętrzne zostają jako tekst; postacie nie mają internetu, więc skrypt powinien dopisać na początku pakietu zdanie: "Linki w tekście są tylko adresami źródeł; nie masz do nich dostępu".

## 2. Pakiet podstawowy (zalecany do przebiegu 1)

Kolejność w pakiecie odpowiada kolejności w tabeli: najpierw prawo i głosy, potem historia, na końcu propozycje i najnowsze stanowiska.

| Nr | Plik | Fragment (linie) | Słów | Dlaczego w pakiecie | Co pominięte i dlaczego |
|---|---|---|---|---|---|
| 1 | `zrodla/konstytucja.md` | art. 7 (112-114), art. 10 (122-125), art. 87 (463-466), art. 98 (524-530), art. 120-122 (631-645), art. 125 (657-662), art. 126 (668-671), art. 131 (698-708), art. 135 (730-733), art. 144-145 (759-797), art. 154-158 (860-879), art. 188-198 (1021-1076), art. 225 (1197-1198), art. 235 (1252-1259) | 2901 | progi głosowań, droga ustawy, weto, zmiana Konstytucji, prerogatywy Prezydenta, wotum nieufności, skrócenie kadencji, TK i Trybunał Stanu, immunitet sędziego TK | reszta Konstytucji nie dotyczy sporu; art. 144 w całości, bo lista prerogatyw (podpis ustawy, wniosek do TK, powołanie Prezesa TK, powołanie sędziów) jest krótsza niż jej streszczanie |
| 2 | `badania/sily-i-glosy.md` | całość | 832 | kluby, liczby posłów, progi, kto z kim ma większość; tabela "Za jakimi rozwiązaniami" odsyła numerami do scenariuszy | nic; sekcja "Kto z kim ma większość" to rachunek repozytorium, nie rekomendacja |
| 3 | `badania/warunki-rozwiazan.md` | całość | 1477 | Senat (58 z 99, jedno miejsce puste), spór, czy Prezydent może skierować zmianę Konstytucji do TK, treść Kp 3/24, K 3/26 i U 5/24, co projekty resetu z 2024 roku robiły z sędziami i wyrokami, opinia Komisji Weneckiej 2024 i stan opinii z 2026.10.13 | nic; "nasza analiza" dotyczy wykładni przepisów, nie wyboru rozwiązania |
| 4 | `historia-sporu.md` | 1-72, ale bez zdań zaczynających się od "Według naszej analizy" (w punktach 2015.12.03, 2021.05.07, 2025.12.18, 2017.10.24, 2025.07.29, 2026.05.12 i 2026.11.03) i bez odsyłacza "[kto odpowiada za kryzys]" w ostatnim punkcie | około 2050 po cięciach (2242 przed) | oś czasu od 1997 roku do 2026.11.04 w pełnych zdaniach, z głosowaniami klubów; jedyny tekst, który daje wszystkim postaciom tę samą historię | zdania "Według naszej analizy" nazywają "błędy" i "kroki", od których "zależało najwięcej"; to oceny odpowiedzialności, wyłączone przez issue. Plik sam je oznacza, więc cięcie jest mechaniczne |
| 5 | `badania/okres-2024-2026.md` | 1-43 | 1875 | jedenaście punktów 2024-2026 z dokumentami stron: uchwały Sejmu, pakiet ustaw, powołanie Święczkowskiego, Kp 3/24, TSUE, wybór ośmiorga, ślubowania, Kpt 1/26, ETPC, Patyra i Berek, 2026.10.30-11.03 (TK, SN, RBN), lista sędziów na stronie TK, II ZZ 2/26 | "Zapis pracy" (44-50): metadane agentów, bez treści |
| 6 | `badania/zgromadzenie-2026-11-03.md` | 1-80 i 85-91 | 1953 | przepisy o Zgromadzeniu Ogólnym (kworum, zwołanie, obecność Prezesa, art. 11 ust. 2, art. 12 ust. 4, art. 130 u.s.p.), spór w pięciu punktach, staż Korwin-Piotrowskiej i Sycha, budżet TK na 2027 rok, wniosek "nie ma organu, którego rozstrzygnięcie obie strony uznają" | "Jak powstała ta notatka" (81-84): opis metody z nazwami modeli; nie zmienia faktów. Uwaga: tekst wspomina "analizę A" i "analizę B" jako źródła argumentów prawnych o kworum i zastępstwie; to analizy prawne jednego zdarzenia, nie scenariusze wyjścia ze sporu, więc zostają |
| 7 | `badania/postepowania-wobec-osob.md` | 1-70 | 1457 | Trybunał Stanu (brak wniosków), śledztwa 2016-2019 i 2024-2026, przeszukanie w TK, 7 wniosków o immunitet, kto je rozpozna, zawiadomienia wobec Korwin-Piotrowskiej, sprawy dyscyplinarne, co nieustalone | "Karta przebiegu" (71-74) |
| 8 | `badania/skutki-dla-obywateli.md` | 1-63 | 1402 | co sądy robią z wyrokami TK, 85 nieopublikowanych wyroków (22, 41, 22), pieniądze z ETPC, konkretne skutki (aborcja, adwokaci z urzędu, emerytury SK 140/20, 6 lat czekania), co nieustalone | "Zapis pracy" (64-67). "Nasz wniosek (interpretacja)" zostaje: opisuje niepewność prawa, nie rozwiązanie |
| 9 | `badania/wyroki-europejskie.md` | 1-66 | 1639 | Xero Flor, M.L., A.R., C-448/23, decyzje Komitetu Ministrów (środki generalne, ocena z 2026.06.11, "przypomina" odmowę z 2015), art. 260 TFUE, stanowiska stron | "Zapis pracy" (67-70) |
| 10 | `zrodla/glosowania-tk-2015-2026.md` | 15-30 ("Najkrócej: jak głosowały główne kluby") | 489 | wyniki wszystkich głosowań końcowych 2015-2026 z rozkładem na kluby (w tym Razem "wstrzymało się" w G2-G3, "przeciw wszystkim" w G4, Centrum z koalicją w 2026 roku) | pełne tabele (43-306): te same liczby plus adresy API i godziny; około 2500 słów, których postać nie potrzebuje |
| 11 | `badania/scenariusze-naprawy.md` | 1-123, 142-169, 188-196, z trzema cięciami w środku: w linii 3 zdanie "Dodaliśmy też scenariusze, które wskazały niezależne analizy modeli AI, choć nikt z polityków ich nie proponuje."; w linii 81 zdanie "Recenzenci obu analiz AI wskazali wyroki ETPC Baka przeciwko Węgrom i Grzęda przeciwko Polsce o przedwczesnym usuwaniu sędziów."; cała linia 90 ("Uwaga z analiz AI" o "odwetowym resecie") | około 3500 po cięciach (3566 przed) | najważniejsze fakty (w tym 2026.11.03), osiem scenariuszy obecnych w debacie z listą "za" i "przeciw" i cytatami, indeks stron, korekty | 124-141 "Scenariusze z analiz AI" (594 słowa): wyłączone przez issue; 170-187 "Jak powstała ta lista" i "Ograniczenia" (262 słowa): metoda i nazwy modeli, bez faktów o sporze poza zastrzeżeniami, które powtarza każda karta źródła; trzy zdania w zachowanych częściach odsyłają do analiz AI, więc wypadają |
| 12 | `badania/propozycje-na-stole.md` | całość | 2447 | dosłowna treść propozycji PSL, Rozwoju Plus, Konfederacji (w tym wywiad Bosaka z 2026.11.04), Fundacji Batorego, HFPC, Klubu Jagiellońskiego, Kukiz'15, Razem, Boguckiego, Dudka i premiera; tabela porównawcza; czego nie wiemy | nic; plik nie ocenia propozycji |
| 13 | `badania/komisja-2026-04-28.md` | 1-5, 18-111, 128-137 | 2891 | materiał z issue #45: kto mówił 2026.04.28, 50 twierdzeń o faktach z oceną zgodności z bazą, stanowiska stron wobec rozwiązań w kwietniu 2026 (KPRP: Prezydent "nigdy" nie odmówił i wykona wyrok w Kpt 1/26; Żurek: okrągły stół; czworo sędziów: gotowi ślubować w Pałacu; PiS: czworo nie są sędziami) | 6-17 "Co to za nagranie" (metoda porównania napisów, 276 słów), 112-127 "Co nowego dla bazy" (lista zadań dla projektu), 138-141 "Zapis pracy"; razem 638 słów bez faktów o sporze poza tymi, które są w tabelach |
| 14 | `badania/bosak-2026-11-04.md` | 1-64 | 2201 | materiał z issue #48: 36 twierdzeń i propozycji Bosaka z 2026.11.04 z porównaniem z bazą (dwa etapy: najpierw policja, Prezes, publikacja, ślubowania przed Prezydentem; potem reset ze stanem spoczynku), gdzie się myli (9 wyroków opublikowanych do 2024.03.04, 30 dni z art. 235 ust. 3) | 65-68 "Zapis pracy" |

Razem około 27 100 słów. Szacunek tokenów: polski tekst z tabelami i adresami to około 2,2-2,6 tokena na słowo, czyli **około 60-70 tys. tokenów** (przyjmuję 65 tys.). To więcej niż 35 tys. założone w etapie 1, bo etap 1 nie znał jeszcze materiału z #45 i #48 i nie liczył Konstytucji, historii ani postępowań wobec osób. Ocena wykonawcy: pakiet w tej wielkości jest stałą częścią każdego wywołania i trafia do bufora (cache), więc jego koszt rośnie wolniej niż liczba wypowiedzi; mimo to agent budujący skrypt powinien policzyć koszt dla obu wersji pakietu (podstawowej i minimalnej) i wybrać według limitu 100$.

## 3. Pakiet minimalny (zapasowy, gdy koszt przebiegu 1 przekroczy założenia)

| Nr | Plik | Fragment | Słów |
|---|---|---|---|
| 1 | `zrodla/konstytucja.md` | art. 98 (524-530), art. 120-122 (631-645), art. 158 (877-879), art. 190-191 (1032-1048), art. 194-196 (1056-1066), art. 225 (1197-1198), art. 235 (1252-1259) | 1468 |
| 2 | `badania/sily-i-glosy.md` | całość | 832 |
| 3 | `badania/warunki-rozwiazan.md` | całość | 1477 |
| 4 | `badania/okres-2024-2026.md` | 1-43 | 1875 |
| 5 | `badania/postepowania-wobec-osob.md` | 1-70 | 1457 |
| 6 | `zrodla/glosowania-tk-2015-2026.md` | 15-30 | 489 |
| 7 | `badania/scenariusze-naprawy.md` | jak w pakiecie podstawowym | około 3500 |
| 8 | `badania/propozycje-na-stole.md` | całość | 2447 |
| 9 | `badania/komisja-2026-04-28.md` | 128-137 ("Stanowiska wobec rozwiązań") | 291 |
| 10 | `badania/bosak-2026-11-04.md` | 57-64 ("Podsumowanie") | 241 |

Razem około 14 100 słów, **około 31-37 tys. tokenów**. Postacie tracą pełną oś czasu, wyroki europejskie, skutki dla obywateli, notatkę o Zgromadzeniu i tabele z komisji; karty prywatne powtarzają z tych plików to, co dotyczy danej osoby, więc strata dotyczy głównie wiedzy o cudzych faktach.

## 4. Uzupełnienie (karty źródeł, tylko na żądanie arbitra)

Postacie nie dostają kart źródeł w pakiecie, bo ich treść jest streszczona w notatkach wyżej. Arbiter może odczytać postaci na jej prośbę dosłowny fragment jednej z tych kart (to odpowiada zasadzie z etapu 1, że arbiter "może przypominać stanowiska na życzenie postaci"):

`zrodla/okres-2024-2026/`: `rbn-2026-11-03.md` (180 słów), `premier-2026-11-03.md` (144), `psl-reset-2026-11-03.md` (257), `konfederacja-reset-2026-10-31.md` (335), `konfederacja-po-rbn-2026-11-03.md` (831), `bosak-polsat-2026-11-04.md` (1162), `rozwoj-plus-trybunal-2026.md` (612), `zandberg-po-spotkaniu-2026-10-31.md` (565), `zandberg-po-rbn-2026-11-03.md` (540), `hfpc-zarzad-2026-10-31.md` (229), `batory-zalasinski-2026.md` (617), `kj-29-warunkow.md` (410), `dudek-2026-11-01.md` (257), `komunikat-31-pazdziernika.md` (115), `zarzadzenie-przerwy-2026.md` (192), `zarzadzenie-2-2026.md` (117), `etpc-17392-26.md` (208), `kpt-1-26.md` (174), `k-3-26.md` (408), `kp-3-24.md` (526), `u-5-24.md` (243), `uchwala-sejmu-2026-299.md` (206), `uchwala-sejmu-2024-198.md` (183), `pk-immunitety-2026.md` (383), `pk-immunitet-2025.md` (145), `pk-uchwala-zo-2025.md` (137), `pk-sledztwo-niedopuszczenie.md` (152), `pk-napasc-2026-11-03.md` (130), `tk-postepowanie-trojga-sedziow.md` (119), `uchwala-kolegium-sn.md` (243), `oswiadczenie-zo-sn.md` (110), `sn-ii-zz-2-26.md` (104), `senat-sklad-2026-11.md` (197), `komisja-wenecka-2024.md` (384), `slubowanie-patyry.md` (82), `berek-sejm.md` (161), `informacja-tk-2024.md` (414), `senat-druk-55.md` (238), `druki-253-254.md` (406), `druk-166-2015.md` (382), `km-xero-flor-2024-2026.md` (419), `tsue-c-448-23.md` (274); `zrodla/xero-flor.md` (272). Razem około 13 500 słów, około 30 tys. tokenów, gdyby skrypt chciał dać je wszystkie; zalecam, by arbiter miał je w swoim kontekście, a postacie nie.

Pełny zapis posiedzenia komisji (`zrodla/okres-2024-2026/spc-149-2026-04-28.md`, 14 110 słów) zostaje poza pakietem i poza uzupełnieniem: notatka z #45 streszcza go z cytatami, a sam zapis kosztowałby około 35 tys. tokenów.

## 5. Wyłączenia z uzasadnieniem

| Plik lub fragment | Powód |
|---|---|
| `badania/rekomendacje-modeli.md`, `badania/rekomendacje/` (7 plików), `badania/bilans-propozycji.md`, `badania/odpowiedz.md` | wyłączone przez issue; nie czytałem ich |
| `badania/odpowiedzialnosc-i-rozwiazania.md` | oceny odpowiedzialności i porównanie rozwiązań według kryteriów projektu; wyłączone przez issue. Odczytałem tylko nagłówek i początek tabeli |
| `badania/scenariusze-naprawy.md` 124-141 | "Scenariusze z analiz AI" (kompromis pakietowy, wąska zmiana Konstytucji, dobrowolne odejścia, Trybunał Stanu, referendum i inne); wyłączone przez issue. Fakty o Trybunale Stanu i referendum są w pakiecie przez art. 125 i 145 Konstytucji oraz `postepowania-wobec-osob.md` |
| `badania/scenariusze-naprawy.md` linia 3 (jedno zdanie), 81 (jedno zdanie), 90 (cała linia), 170-187 | zdania odsyłające do analiz AI i opis metody |
| `historia-sporu.md`, zdania "Według naszej analizy" i link do `odpowiedzialnosc-i-rozwiazania.md` | oceny, który krok był "błędem"; to ocena odpowiedzialności |
| `badania/symulacja/etap-1.md` i pozostałe pliki `badania/symulacja/` | oceny wykonawcy etapu 1, kto jest niezbędny i kto ma swobodę ruchu; zakotwiczyłyby rozmowę. Rachunek progów jest w `sily-i-glosy.md`, a reguły liczenia w instrukcji arbitra |
| `README.md`, `AGENTS.md`, `plan.md`, `analizy.md`, `metodologia.md`, `historia-prac.md`, `techniczne.md`, `wspolpraca.md` | organizacja projektu, nie wiedza o sporze; `README.md` i `analizy.md` linkują do wyłączonych plików |
| `badania/geneza-przed-2015.md`, `badania/skad-art-137.md`, `badania/piec-miejsc.md`, `badania/kierownictwo-2016.md`, `badania/okres-2016-2019.md`, `badania/okres-2020-2023.md`, `badania/okres-2020-2023-uzupelnienie.md`, `badania/kadencja-prezes-2022-2023.md`, `badania/publikacja-wyrokow.md` | szczegóły lat 1997-2023; oś czasu w `historia-sporu.md` streszcza je z datami i wynikami głosowań. Wyjątek dla kart: z `kadencja-prezes-2022-2023.md` biorę przepis o 6-letniej kadencji Prezesa, a z `publikacja-wyrokow.md` zdanie, kto wydaje Dziennik Ustaw |
| `badania/materialy-do-sprawdzenia.md` | lista zadań projektu |
| `zrodla/` poza wymienionymi w uzupełnieniu (wyroki K 34/15 i K 35/15 w całości, ustawy z 2015 i 2016 roku, druki 1590 i 3397, zapis komisji z 2015 roku, karty 2016-2023, uchwały z 2015 roku, karty przed 2015) | pełne teksty aktów i wyroków, razem ponad 150 tys. słów; ich treść istotna dla sporu jest w notatkach. Fragmenty K 34/15 o ślubowaniu (obowiązek "bez zwłoki", trzy wyjątki) są cytowane w `komisja-2026-04-28.md` i `bosak-2026-11-04.md` |
| `zrodla/okres-2024-2026/spc-149-2026-04-28.md` | pełny zapis, 14 110 słów; streszczony w notatce z #45 |
| `.github/`, `narzedzia/`, `zrodla/manifest.json` | pliki techniczne |

## 6. Uwagi dla etapu 3 (skrypt)

1. Przed pierwszym przebiegiem skrypt wycina fragmenty po numerach linii z wersji 70b735a, skleja pakiet w podanej kolejności, dopisuje zdanie o linkach i zdanie "Stan wiedzy: 2026.11.04", liczy SHA-256 pakietu, każdej karty, trzech instrukcji wariantów i instrukcji arbitra, i publikuje je razem z tekstami.
2. Kolejność w kontekście postaci: instrukcja wariantu motywacji, pakiet wiedzy, karta prywatna, wątek rozmowy. Pakiet przed kartą, żeby karta (krótsza, osobista) była bliżej wypowiedzi.
3. Ocena wykonawcy: jeśli przebieg 1 pokaże, że postacie mylą liczby głosów, warto dać `sily-i-glosy.md` także na końcu pakietu (powtórzenie 832 słów), bo modele lepiej pamiętają koniec długiego kontekstu. To zmiana techniczna, nie merytoryczna, i powinna być zapisana w raporcie z przebiegu.

## Zapis pracy

Przeczytane pliki: `issue-46.md`, `badania/symulacja/etap-1.md`, `badania/sily-i-glosy.md`, `badania/warunki-rozwiazan.md`, `badania/scenariusze-naprawy.md` (bez 124-141), `badania/propozycje-na-stole.md`, `badania/komisja-2026-04-28.md`, `badania/bosak-2026-11-04.md`, `badania/okres-2024-2026.md`, `badania/zgromadzenie-2026-11-03.md`, `badania/postepowania-wobec-osob.md`, `badania/skutki-dla-obywateli.md`, `badania/wyroki-europejskie.md`, `badania/kadencja-prezes-2022-2023.md` (część), `badania/publikacja-wyrokow.md` (początek), `badania/odpowiedzialnosc-i-rozwiazania.md` (nagłówek), `historia-sporu.md`, `README.md` (początek), `zrodla/konstytucja.md` (wymienione artykuły), `zrodla/glosowania-tk-2015-2026.md` (1-44, 199-306), karty w `zrodla/okres-2024-2026/`: `rbn-2026-11-03`, `premier-2026-11-03`, `psl-reset-2026-11-03`, `konfederacja-reset-2026-10-31`, `konfederacja-po-rbn-2026-11-03`, `bosak-polsat-2026-11-04`, `rozwoj-plus-trybunal-2026`, `komunikat-31-pazdziernika`, `zarzadzenie-przerwy-2026`, `etpc-17392-26`, `kpt-1-26`, `k-3-26`, `kp-3-24`, `uchwala-sejmu-2026-299`, `pk-immunitety-2026`, `uchwala-kolegium-sn`, `tk-postepowanie-trojga-sedziow`, `berek-sejm`, `slubowanie-patyry`, `informacja-tk-2024`, `zandberg-po-rbn-2026-11-03`, `spc-149-2026-04-28` (nagłówek). Liczby słów policzone skryptem na plikach w wersji 70b735a.

Agent-Role: wykonawca etapu 2 (issue #46). Agent-Model: claude-fable-5-1 (Claude Fable 5.1), agent Claude Code. Agent-Run: niepotwierdzony.
