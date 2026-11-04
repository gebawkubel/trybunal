> Etap 4 [symulacji negocjacji (issue #46)](https://github.com/gebawkubel/trybunal/issues/46): poprawki przed kolejnymi przebiegami, według komentarza "Etap 4: poprawki przed kolejnymi przebiegami" i uwag prowadzącego po przebiegu 1. Napisał Claude Opus 5.5 (agent Claude Code) na repozytorium w wersji e28858b (gałąź symulacja-etap-4). Polecenie: dosłowna treść issue #46 z komentarzami i wiadomość techniczna, w jednym pliku o SHA-256 `0072843696f5d995404b4e25e765214554f480ee3bb4c6809f9f1e1d599493c8`. Bez płatnych przebiegów: tylko atrapa modelu i liczenie tokenów (`count_tokens`). To ocena modelu, nie ustalenie projektu; wynik przechodzi jawną recenzję.

---

# Etap 4: mniejszy stół, porozumienie bez zgody wszystkich, dłuższy limit wypowiedzi

Prowadzący napisał po przebiegu 1: "nie wiem czy aż tylu trzeba zapraszać", "czy wszyscy muszą się zgodzić? absolutnie nie" oraz "popraw długość, ale nie przesadzaj z nią". Ten dokument odpowiada na trzy punkty z issue: kto siedzi przy stole, jak zapisać, że zgoda wszystkich nie jest potrzebna, i jak zmienić limit długości. Na końcu jest nowy plan przebiegów z kosztem.

Oznaczenia jak w etapie 1: liczby głosów z `badania/sily-i-glosy.md` (stan 2026.11.04), fakt ma w nawiasie plik, "ocena wykonawcy" to mój wniosek. Numery w nawiasach z literą "z" (np. z81) to numery wypowiedzi w [zapisie przebiegu 1](przebieg-1/zapis.md).

## 1. Skład stołu

### Kryterium

Osoba siedzi przy stole, gdy bez niej pakiet na ścieżce, która ma szansę, nie ma wymaganego progu głosów albo wymaganej czynności (podpisu, ślubowania, dopuszczenia do orzekania, czynności Marszałka), i nikt obecny przy stole jej nie zastąpi. Osoba, której głosy tylko powiększają sumę ponad próg albo zastępują głosy kogoś, kto i tak musi być przy stole, nie siedzi. To kryterium etapu 1 (weto albo niezbędność), zawężone do ścieżek z szansą.

### Które ścieżki mają szansę (ocena wykonawcy)

- **C, zmiana Konstytucji, i D, porozumienie bez ustawy:** tak. To wynik przebiegu 1 (z81). Za resetem w jakiejś formie są PSL, Polska 2050, Rozwój Plus, Konfederacja, Razem i Prezydent "po wyborach 2027"; Bosak 2026.11.04 łączy kroki bez ustawy z późniejszym resetem (`badania/scenariusze-naprawy.md`, `badania/propozycje-na-stole.md`, `badania/bosak-2026-11-04.md`).
- **A, zwykła ustawa z podpisem Prezydenta:** tak, jako część pakietu (ustawa towarzysząca w z81) albo samodzielnie, jeśli Prezydent zgodzi się podpisać.
- **B, ustawa po wecie bez PiS:** nie. Wymaga, żeby Rozwój Plus głosował z koalicją (279 wobec 276). Według pakietu Rozwój Plus ma własny projekt zmiany Konstytucji i proponuje konstruktywne wotum nieufności wobec premiera (`zrodla/okres-2024-2026/rozwoj-plus-trybunal-2026.md`, `badania/scenariusze-naprawy.md`); pakiet nie zawiera żadnej zapowiedzi poparcia ustawy koalicji. Po odrzuceniu weta 50 posłów PiS może zaskarżyć ustawę do TK, a TK w Kp 3/24 uznał, że wygaszanie kadencji ustawą "wymagałoby zmiany Konstytucji" (`badania/warunki-rozwiazan.md`). Taka ustawa nie kończy sporu, tylko go przenosi do TK.
- **E, obecna praktyka:** nie jest porozumieniem (arbiter.md, część 5).
- **F, wotum nieufności albo skrócenie kadencji:** zmienia rząd, a nie rozwiązuje sporu o TK; arbiter nie uznaje go za porozumienie, jeśli pakiet nie mówi, co z TK (arbiter.md, część 5).
- **G, rozjemca, i H, czekanie:** nie wymagają nikogo dodatkowego przy stole; to alternatywy, które każda karta opisuje jako "co zyskujesz bez porozumienia".

### Rachunek

Przy pełnej sali (wyliczenia własne):
- KO (156) z Centrum (15) i PiS (147) mają 318. To wystarcza do każdego progu w Sejmie: 231, 276 i 307.
- Bez KO jest najwyżej 304, więc zmiany Konstytucji nie ma bez Tuska (etap 1, ścieżka C).
- Bez PiS zmiana Konstytucji wymaga 307 z 313 pozostałych posłów, w tym co najmniej 11 z 17 posłów spoza klubów, którzy nie mają przy stole przedstawiciela nawet w składzie W1 (etap 1, ścieżka C). Ocena wykonawcy: to droga bez szansy.
- W Senacie KO (42) z PiS (31) mają 73 przy progu 50 (`badania/warunki-rozwiazan.md`; liczby w arbiter.md, część 3).

Wniosek: w każdej ścieżce z szansą, która wymaga głosowania nad zmianą Konstytucji, potrzebni są Tusk i Kaczyński, a pozostałe kluby nie zmieniają wyniku. W przebiegu 1 pakiet miał 443 głosy przy progu 307 (z81), a bez Rozwoju Plus, PSL, Polski 2050, Konfederacji i Lewicy miałby 318.

### Kto zostaje, kto odchodzi

| Osoba | Decyzja | Uzasadnienie |
|---|---|---|
| Karol Nawrocki, Prezydent | zostaje | podpis ustawy i zmiany Konstytucji, wniosek do TK, ślubowanie, Kpt 1/26 (art. 122, 235 ust. 7, 194 ust. 2); w przebiegu 1 zadeklarował sześć czynności (z81) |
| Donald Tusk, premier, KO | zostaje | bez KO nie ma 307 ani 231; rząd wycofuje policję i publikuje wyroki (z81) |
| Jarosław Kaczyński, PiS | zostaje | bez PiS przy stole jest najwyżej 239, mniej niż 276 i 307 |
| Włodzimierz Czarzasty, Marszałek Sejmu, Lewica | zostaje | czynności Marszałka są potrzebne w każdej ścieżce z ustawą: nadanie biegu projektowi, terminy czytań, przedstawienie ustawy Prezydentowi (art. 122 ust. 1, arbiter.md pkt 4.6); w przebiegu 1 zadeklarował je wprost (z81). Lewica (21) jest potrzebna, gdy ustawę uchwala sama koalicja (bez Lewicy 218). Jest jedynym liderem koalicji, który publicznie odrzucił zmianę Konstytucji ("Nie poprę żadnego resetu, nie poprę zmiany konstytucji", `badania/scenariusze-naprawy.md`), więc jego obecność sprawdza, czy porozumienie zbudowane bez niego wytrzyma jego sprzeciw |
| Bogdan Święczkowski, Prezes TK | zostaje | dopuszczenie sędziów do orzekania, Zgromadzenie Ogólne, składy, Kpt 1/26 (droga D); w przebiegu 1 zadeklarował pięć czynności (z81) |
| Anna Korwin-Piotrowska, sędzia z 2026 roku | zostaje | uchylenie przerwy w czynnościach Prezesa, oddanie siedziby i Kancelarii, skarga w ETPC (droga D); w przebiegu 1 zadeklarowała pięć czynności (z81) |
| Mateusz Morawiecki, Rozwój Plus | odchodzi | Rozwój Plus jest potrzebny tylko w ścieżce B bez PiS i w zmianie Konstytucji bez PiS; obie są bez szansy (wyżej). Gdy głosuje PiS, 40 głosów niczego nie zmienia. Nie blokuje też zmiany Konstytucji, bo 318 wystarcza bez niego |
| Władysław Kosiniak-Kamysz, PSL | odchodzi | PSL (32) jest potrzebny, gdy ustawę uchwala sama koalicja, i w wotum nieufności. Pierwszy przypadek obejmuje reguła liczenia z Tuskiem (niżej), drugi nie jest rozwiązaniem sporu o TK |
| Szymon Hołownia, Polska 2050 | odchodzi | jak PSL: 15 głosów, potrzebne tylko przy samej koalicji (wtedy liczone z Tuskiem) albo w wotum nieufności z Razem i niezrzeszonymi |
| Krzysztof Bosak, Konfederacja | odchodzi | Konfederacja (17) jest potrzebna tylko w zmianie Konstytucji bez PiS i w wotum nieufności; obie bez szansy albo poza sporem o TK |

Wychodzi 6 postaci zamiast 10. Nazywam ten skład **W5**, żeby nie mylić go z W1 z przebiegu 1.

Ocena wykonawcy, koszt tej decyzji. W przebiegu 1 główny pakiet złożył i uzupełniał Hołownia (z31, z66), a pomost dla sędziów z 2026 roku zaproponował Kosiniak-Kamysz (z17). Bez nich przy stole jest mniej pośredników, więc rozmowa może pójść inaczej. To nie jest powód, by ich zapraszać: kryterium dotyczy głosów i czynności, a nie roli w rozmowie. Przebieg 1 zostaje jako porównanie: ten sam wariant (b) w W1 i W5 pokaże, czy liczba osób zmienia wynik.

### Nowe reguły liczenia (arbiter.md, część 4)

1. Kluby koalicji bez przedstawiciela przy stole, czyli PSL-Trzecia Droga (32), Polska 2050 (15) i Centrum (15), liczą się tak, jak zadeklaruje Tusk. Podstawa: we wszystkich czterech głosowaniach o TK w 2026 roku (G1-G4) wszystkie pięć klubów koalicji głosowało tak samo (`zrodla/glosowania-tk-2015-2026.md`; dla Centrum ta reguła była już w W1). To założenie, nie fakt: PSL i Polska 2050 są za resetem, a KO przeciw. Arbiter podaje w wyniku, ile głosów pochodzi z tej reguły i jaka jest suma bez niej.
2. Lewica liczy się według Czarzastego, a w Senacie Trzecia Droga według Tuska, Lewica według Czarzastego.
3. Kluby opozycji bez przedstawiciela (Rozwój Plus, Konfederacja, Razem, Korona, Demokracja Bezpośrednia, niezrzeszeni, razem 74) są niedostępne, jak kluby nieobecne w W1.

Skutek przy stole:
- najwięcej 386 głosów;
- 231 wychodzi z całej koalicji (239) albo z KO i PiS;
- 276 i 307 tylko z KO i PiS (318 z samym Centrum, 386 ze wszystkimi);
- bez PiS jest najwyżej 239, a bez KO 168;
- wotum nieufności przy stole nie wychodzi (168).

Ocena wykonawcy: reguła 1 sprawia, że bez PSL i Polski 2050 przy stole nadal działa ścieżka "ustawa koalicji z podpisem Prezydenta", w której PiS nie jest potrzebny. Bez tej reguły jedyną drogą byłoby porozumienie z PiS, a to byłoby skutkiem doboru stołu, nie arytmetyki Sejmu.

### Co tracimy

- Ścieżki F (wotum nieufności) nie da się sprawdzić przy stole. To zamierzone: nie rozwiązuje sporu o TK.
- Stanowiska PSL, Polski 2050, Rozwoju Plus i Konfederacji postacie znają tylko z pakietu wiedzy, bez ich przedstawicieli w rozmowie.
- Reguła 1 zakłada, że PSL i Polska 2050 pójdą za Tuskiem. Gdyby w rzeczywistości postawiły warunki, wynik symulacji byłby zbyt optymistyczny dla ustaw uchwalanych bez PiS. Nie dotyczy to zmiany Konstytucji, bo tam KO z Centrum i PiS mają 318.

### Składy wariantowe W2-W4

Usuwam je z planu:
- **W2** (stół bez premiera) sprawdzał głównie wotum nieufności i to, czy PSL przejdzie na drugą stronę (etap 1, część 3). Ścieżka F nie rozwiązuje sporu o TK, a W2 zapraszał 4 osoby bez rozstrzygającego głosu (Hołownia, Bosak, Zandberg, Kukiz).
- **W4** (Nawrocki, Tusk, Kaczyński) to W5 bez osób, których czynności są potrzebne w drodze D (Marszałek, sędziowie). Arbiter nie mógłby więc uznać pakietu z drogą D, który w przebiegu 1 był częścią porozumienia.
- **W3** (stół sędziowski) zostaje poza planem. Prowadzący może do niego wrócić, jeśli przebiegi W5 pokażą, że blokują sędziowie.

## 2. Zgoda wszystkich nie jest wymagana

Co było w tekstach przed zmianą:
- Instrukcja arbitra miała już właściwą regułę (część 6, warunek c): głos "przeciw" postaci, której głosy i czynności nie są potrzebne, nie blokuje porozumienia.
- Postacie tej reguły nie znały. Widzą instrukcję wariantu i karty, a nie arbiter.md. Instrukcja wariantu mówiła tylko, że "brak porozumienia" jest dozwolony (pkt 4), a polecenie głosowania nie mówiło nic o progach.
- Słowa "jednomyślnie" ani wymogu zgody wszystkich nie było nigdzie. W przebiegu 1 arbiter tak tego nie przedstawiał, ale za pakietem głosowało wszystkie 10 postaci (z81).

Zmiany:
- **Instrukcja wariantu, pkt 4** (część wspólna, ta sama we wszystkich wariantach): "Porozumienie nie wymaga zgody wszystkich osób przy stole: pakiet jest przyjęty, gdy ma wymagane progi głosów i zadeklarowane czynności osób, bez których nie da się go wykonać. Głos 'przeciw' osoby, bez której pakiet nadal ma progi i czynności, nie blokuje go; arbiter zapisuje go jako sprzeciw."
- **Instrukcja arbitra, część 1:** arbiter mówi to w pierwszej wypowiedzi, nie dąży do jednomyślności i nie traktuje takiego głosu "przeciw" jako przeszkody. Część 6 bez zmian.

Zdanie nie mówi, czyje głosy są potrzebne. Rachunek robi arbiter (arbiter.md, część 4, pkt 1: "Nie zakłada z góry, że jakiś klub jest niezbędny"), więc zmiana nie zakotwicza postaci.

## 3. Długość wypowiedzi

Dane z przebiegu 1 (`przebieg-1/zapis.jsonl`, pole `tokeny_tekstu`, czyli tokeny samego tekstu wypowiedzi):
- polski tekst wypowiedzi to średnio 3,6 tokena na słowo;
- w otwarciu i dyskusji (53 wypowiedzi) było średnio 252 słowa; 52 wypowiedzi miały 770-995 tokenów, ucięta została 1 (Hołownia, 1614 tokenów, z31);
- w głosowaniach (20 wypowiedzi) było średnio 299 słów, 948-1248 tokenów; uciętych zostało 9.

Wniosek: limit 250 słów w dyskusji działa. Głosy są dłuższe, bo postacie powtarzają w nich treść pakietu i warunki.

Zmiany:
- **Limit w skrypcie: 1400 tokenów zamiast 1100**, czyli o około jedną czwartą więcej, około 390 słów. Na danych z przebiegu 1 ucięta zostałaby tylko 1 wypowiedź zamiast 10.
- **Wskazówka dla postaci bez zmian: około 250 słów.** W instrukcji wariantu (pkt 6) i u arbitra liczba tokenów jest teraz zgodna ze skryptem.
- **Krótszy format głosu:** najwyżej około 200 słów, bez powtarzania treści pakietu i uzasadnienia, tylko głos, zobowiązania i zastrzeżenia. Zmienione są instrukcja wariantu (pkt 7), arbiter.md (część 2, pkt 3) i zdanie tury głosowania w skrypcie (`TURA.glosowanie`).

Wpływ na koszt:
- Ucięcie nie zmniejsza kosztu generowania, bo model i tak pisze całą odpowiedź. Zmienia tylko długość wątku, który czytają następne wywołania.
- W przebiegu 1 ucięcia skróciły wątek o 430 słów, czyli około 1,5 tys. tokenów. Wyższy limit kosztuje więc najwyżej około 0,2 USD na przebieg.
- Górna granica: gdyby każda wypowiedź dochodziła do 1400 tokenów, przebieg W5 kosztowałby według atrapy 9,4 zamiast 8,1 USD (przed korektą, niżej).

## 4. Koszt i plan przebiegów

### Szacunek kosztu przebiegu W5

Metoda:
1. Pomiar `count_tokens` dla nowych tekstów ([tokeny.json](../../narzedzia/symulacja/tokeny.json)). System postaci z wariantem (b) ma 120 866 tokenów, system arbitra 183 237.
2. Atrapa skryptu z założeniami z przebiegu 1: wypowiedź 200 słów (przy przeliczniku atrapy 4,4 to około 880 tokenów, jak w przebiegu 1), rozumowanie postaci 600 tokenów, arbitra 1200.
3. Korekta. Ta sama atrapa na skryptcie z przebiegu 1 (skład W1, głosowanie po 3. rundzie, głos poza kolejnością w każdej rundzie, czyli przebieg 1 w skrócie) daje 12,81 USD. Zmierzony koszt to 14,50 USD, więc mnożę wyniki atrapy przez 1,13.

| Scenariusz W5 | Wywołania / wypowiedzi postaci | Atrapa | Po korekcie |
|---|---|---|---|
| jak przebieg 1: głosowanie po 3. rundzie, dodatkowa runda, powtórne głosowanie | 53 / 45 | 8,10 USD | **około 9,2 USD** |
| głosowanie po 6. rundzie, dodatkowa runda | 74 / 63 | 10,73 USD | około 12,1 USD |
| 8 rund, głos poza kolejnością w każdej, dodatkowa runda | 94 / 80 | 13,24 USD | około 15,0 USD |
| jak wyżej, wypowiedzi 250 słów, rozumowanie 1500 / 3000 | 94 / 80 | 16,42 USD | około 18,5 USD |
| wszyscy "Pas" w 1. rundzie | 15 / 12 | 3,97 USD | około 4,5 USD |

Dla porównania, W1 w scenariuszu jak przebieg 1 kosztował 14,50 USD, a W5 około 9,2 USD, czyli o około 37% mniej. Koszt nie spada proporcjonalnie do liczby postaci, bo pakiet (około 121 tys. tokenów) każda postać i arbiter zapisują do bufora raz, a arbiter kosztuje podobnie jak w W1. Atrapa sprawdziła też limit kosztu: 120 przebiegów (limity 3-20 USD, scenariusze typowy i maks, z najdroższym ogłoszeniem arbitra i bez niego) nie przekroczyło limitu.

### Plan

Budżet: 100 USD, wydane 14,50 USD (przebieg 1), zostaje 85,50 USD. Zasady:
- każdy przebieg ma limit 18 USD (`--limit-usd 18`, domyślny w skrypcie), żeby długi przebieg zmieścił się bez przerwania (górny scenariusz około 18,5 USD przerwałby się blisko końca);
- gdy do 100 USD zostaje mniej niż 18 USD, limit przebiegu to cała pozostała kwota; przebiegu nie uruchamiamy, gdy zostaje mniej niż 12 USD (scenariusz z głosowaniem po 6. rundzie). Suma nigdy nie przekroczy 100 USD;
- warianty idą na przemian, żeby przerwanie planu przez budżet nie zostawiło jednego wariantu bez przebiegów.

| Nr | Wariant motywacji | Skład | Model | Kolejność otwarcia | Szacunek |
|---|---|---|---|---|---|
| 1 | (b) | W1 | Opus 5.5, wysiłek medium | Nawrocki pierwszy | **14,50 USD, wykonany** |
| 2 | (a) dobro państwa | W5 | ten sam | Nawrocki pierwszy (`--przesuniecie 0`) | 9-15 USD |
| 3 | (c) czysty interes polityczny | W5 | ten sam | Nawrocki pierwszy | 9-15 USD |
| 4 | (b) | W5 | ten sam | Nawrocki pierwszy | 9-15 USD |
| 5 | (a) | W5 | ten sam | Tusk pierwszy (`--przesuniecie 1`) | 9-15 USD |
| 6 | (c) | W5 | ten sam | Tusk pierwszy | 9-15 USD |
| 7 | (b) | W5 | ten sam | Tusk pierwszy | 9-15 USD |
| 8 | (a) | W5 | ten sam | Kaczyński pierwszy (`--przesuniecie 2`) | jeśli zostaje budżet |
| 9 | (c) | W5 | ten sam | Kaczyński pierwszy | jeśli zostaje budżet |
| 10 | (b) | W5 | ten sam | Kaczyński pierwszy | jeśli zostaje budżet |
| K1-K3 | (a), (c), (b) | W5 | inny model przez Codex | jak 2-4 | poza limitem 100 USD |

Ocena wykonawcy, ile się zmieści (wyliczenia z reguł wyżej):
- przy około 9-10 USD na przebieg, jak przebieg podobny do przebiegu 1: 8 przebiegów W5, czyli 2-9;
- przy około 12 USD: 7 przebiegów, czyli 2-8;
- w najgorszym razie, gdy każdy przebieg dochodzi do limitu 18 USD: 5 przebiegów, ostatni z limitem 13,50 USD.

Pełny plan "3 warianty po 3 przebiegi" w W5 (przebiegi 2-10) zmieści się, jeśli przebiegi będą kosztować średnio najwyżej około 9,2 USD, czyli tyle, ile przebieg podobny do przebiegu 1. Przebieg 1 nie liczy się do serii W5, bo miał inny skład.

## 5. Zmienione pliki

| Plik | Co zmienione |
|---|---|
| `etap-2/arbiter.md` | skład W5 i kolejność (część 2), limity długości i liczby wypowiedzi (część 2), reguły liczenia (część 4, pkt 2-5), droga F i C (część 5), porozumienie bez zgody wszystkich (część 1); nagłówek z nową sumą i linkiem do wersji z przebiegu 1 |
| `etap-2/warianty-motywacji.md` | część wspólna, pkt 4 (porozumienie bez zgody wszystkich), 6 (1400 tokenów) i 7 (format głosu); warianty (a), (b), (c) bez zmian |
| `narzedzia/symulacja/symulacja.py` | skład W5; limity 1400 tokenów, 80 wypowiedzi, 8 głosów poza kolejnością; zdanie tury głosowania; domyślny limit kosztu 18 USD; dwie opcje atrapy do szacunku (`--atrapa-glosowanie-po`, `--atrapa-poza-co-runde`); przypadki testowe atrapy przeniesione na postacie z W5 |
| `narzedzia/symulacja/README.md`, `sumy.json`, `tokeny.json` | opis, sumy z trybu `zbuduj`, pomiar z trybu `policz` |

Karty postaci W5 i pakiet wiedzy są bez zmian. Karty nie opisują składu stołu ani reguł arbitra, tylko fakty o osobach, więc usunięcie czterech postaci ich nie zmienia. Karty Morawieckiego, Kosiniaka-Kamysza, Hołowni i Bosaka zostają w repozytorium jako materiał przebiegu 1; skrypt ich nie wysyła.

Sumy SHA-256 tekstów pod linią: `arbiter.md` `6ab2635d59e6b514c2411c925f2ab9f809332f0ae58eb08d1dd9d50b2fb53fae` (wersja z przebiegu 1: `08445af7c3cc107dd34075acf02e233f48116115a8a8b091934531a987adc255`), `warianty-motywacji.md` `7d4f7442a257c1aec524fb0ec6817bd222a1272732d56fc127f9db29e419b70d` (wersja z przebiegu 1: `4497509268a10557c9a7363b504fb21861234b7d11b647ab9f17f7b5c8b3072b`). Sumy gotowych tekstów wysyłanych do modelu są w [sumy.json](../../narzedzia/symulacja/sumy.json).

## 6. Ograniczenia

- Korekta 1,13 pochodzi z jednego przebiegu. Rozrzut między przebiegami nie jest znany.
- Atrapa nie wie, czy mniejszy stół skróci rozmowę. Szacunek podaje więc zakres scenariuszy, a nie jedną liczbę.
- Wybór ścieżek "z szansą" to ocena wykonawcy na podstawie pakietu, nie fakt. Jeśli recenzja uzna ścieżkę B za realną, do stołu wraca Morawiecki.

## Zapis pracy

Przeczytane: issue #46 z komentarzami (polecenie), `AGENTS.md`, `badania/symulacja/etap-1.md`, `badania/symulacja/etap-2/arbiter.md`, `warianty-motywacji.md`, nagłówek i część 1-2 `pakiet-wiedzy.md`, fragmenty kart W5 (wyszukanie odniesień do składu stołu), `narzedzia/symulacja/README.md` i `symulacja.py`, `badania/symulacja/przebieg-1/raport.md`, `zapis.jsonl` i `ustawienia.json` (pomiary długości i kosztu). Raport przebiegu 1 ma część "Porównanie z wcześniejszymi analizami", która streszcza też rekomendacje modeli; przeczytałem ją razem z raportem. Teksty widziane przez postacie nie zawierają z niej niczego. Nie czytałem plików wyłączonych w issue (`badania/rekomendacje-modeli.md`, `badania/rekomendacje/`, `badania/bilans-propozycji.md`, `badania/odpowiedz.md`).

Agent-Role: wykonawca etapu 4 (issue #46). Agent-Model: claude-opus-5-5 (Claude Opus 5.5, agent Claude Code). Agent-Run: niepotwierdzony.
