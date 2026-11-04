> Etap 2 [symulacji negocjacji (issue #46)](https://github.com/gebawkubel/trybunal/issues/46), wersja 2 po jawnej recenzji. Napisał Claude Fable 5.1 (wysoki wysiłek rozumowania, agent Claude Code) na repozytorium w wersji 70b735a (gałąź symulacja-baza-etap-2), według [treści issue](polecenie-issue.md) i [wiadomości technicznej](wiadomosc.md); poprawki według [raportu recenzji](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6629816916) i [wiadomości o poprawce](wiadomosc-poprawka.md). Wersja 1: [commit bd2643c](https://github.com/gebawkubel/trybunal/tree/bd2643ca06f88f370280b4e3bb57a4fa4dedde9e/badania/symulacja/etap-2). Zakazy (internet, zmiany, inne katalogi) były w wiadomościach, nie wymuszone technicznie. To robocze materiały symulacji: oceny i wnioski autora etapu, nie ustalenia projektu; postacie są symulowane przez AI. Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `cca79bc86069701df940aa12042c8d50a06906ecaf2cbba43a43dff18cfa5c62`.

---

# Luki: czego brakuje w repozytorium (wersja 70b735a) dla każdej karty

Etap 2 symulacji negocjacji (issue #46). Lista uzupełnia luki z etapu 1 (`badania/symulacja/etap-1.md`, część 5) o to, co wyszło przy pisaniu kart. Luki z etapu 1, które pozostają aktualne, powtarzam w skrócie; nowe oznaczam "nowa". Każda karta w części 7 ma skróconą wersję swojej listy, żeby postać nie wymyślała brakujących faktów.

## Wspólne dla wszystkich kart

1. **"Przed kim odpowiada":** repozytorium nie opisuje struktur partyjnych, sondaży, nastrojów wyborców ani terminu wyborów 2027 poza "jesienią". Karty wypełniają ten punkt tylko instytucjami (Sejm, Trybunał Stanu, wyborcy) i nazwą partii. Dla wariantu (c) brak miary opłacalności; postacie będą ją szacować same.
2. **"Co zyskuje bez porozumienia":** brak dat końca kadencji sędziów poza Wyrembakiem (2027.01.30); nie wiadomo, co z budżetem TK na 2027 rok, jeśli Sejm nie uchwali części dla TK, ani czy plan ośmiorga trafił do ministra finansów; brak listy spraw zawieszonych w TK i skutków dla obywateli za 2025-2026 poza przykładami.
3. **Prawo:** nierozstrzygnięte, czy Prezydent może skierować zmianę Konstytucji do TK; pełnej opinii Komisji Weneckiej z 2026.10.13 nie odczytano; poprawek Senatu z 2024.07.31 i zarządzenia Prezesa SN z 2026.11.02 (II ZZ 2/26) nie odczytano; przepis ustawy o organizacji TK o pełnym składzie ("co najmniej 11", twierdzenie Boguckiego) i art. 4 ustawy o statusie sędziów TK (ślubowanie i skutki odmowy) nie są skopiowane; brzmienia art. 25-27 ustawy o statusie po 2016 roku nie sprawdzono. Nowa: nie wiadomo, co dzieje się po upływie miesięcznej przerwy z art. 130 u.s.p. (najdłużej miesiąc od 2026.10.30) i czy sąd dyscyplinarny zawiadomiono w 3 dni.
4. **Nowa: zdarzenia z 2026.11.04 i później.** Repozytorium kończy się na wywiadzie Bosaka z rana 2026.11.04; brak odpowiedzi rządu na żądanie z RBN, informacji o spotkaniu Tuska z Nawrockim, reakcji na wywiad Bosaka, komunikatów TK i SN po 2026.11.03.
5. **Nowa: relacje między obozami.** Repozytorium nie opisuje relacji PiS z Prezydentem, PiS z Rozwojem Plus i Konfederacją ani Konfederacji z Prezydentem; karty Nawrockiego, Kaczyńskiego, Morawieckiego i Bosaka muszą to oznaczyć jako nieznane, co może sztucznie usamodzielnić postacie prawicy wobec siebie.

## Nawrocki

- Czy aprobuje plany Konfederacji i Rozwoju Plus (Kancelaria nie potwierdziła); dokumentu Kancelarii o "restarcie" (Bogucki) nie ma; nie wiadomo, czy Rada Nowej Konstytucji zajmuje się TK; brak odpowiedzi na propozycję spotkania "w cztery oczy"; nie ustalono, czy przesłuchano go jako świadka; brak stanowiska wobec wyroków ETPC i TSUE.
- Nowa: brak daty wyboru i wyniku wyborów prezydenckich, więc karta nie może powiedzieć, ile lat kadencji zostało; brak własnych słów Prezydenta po 2026.10.15 poza parafrazą komunikatu z RBN (cytaty z RBN pochodzą z komunikatu Kancelarii, nie z nagrania); dokładne brzmienie wypowiedzi Boguckiego z Radia ZET tylko [media x1].

## Tusk

- Brak odpowiedzi rządu na żądanie z RBN i własnej propozycji treści zmian; stanowisko o ustawie 3/5 tylko od posła Tomczykiewicza [media x1]; treści wykazu 85 nieopublikowanych wyroków w repozytorium nie ma (są trzy sygnatury).
- Nowa: brak dokumentu policji ani MSWiA o obecności w budynku TK, więc karta nie wie, kto formalnie wydał polecenie i na jakiej podstawie; brak stanowiska KO wobec wotum nieufności, skrócenia kadencji i art. 225; brak stanowiska rządu wobec kworum 2026.11.03 poza słowami Żurka [media x1]; struktury KO nieopisane.

## Kaczyński

- Brak funkcji partyjnej; brak oficjalnego stanowiska PiS wobec resetu (jest Wójcik przeciw, Czarnek: niemożliwy bez 2/3); brak jego wypowiedzi o ślubowaniu i ustawie 3/5 poza wezwaniem z 2026.09.29 [media x1]; brak opisu relacji PiS z Rozwojem Plus.
- Nowa: brak stanowiska PiS wobec projektu Rozwoju Plus i wobec stanu spoczynku dla obecnych sędziów; brak stanowiska wobec wniosków o immunitet Prezesa TK za czyny z okresu prokuratorskiego (Pegasus, "Hermes"); zawiadomienie PiS z art. 128 k.k. tylko [media x1]. Karta opiera się w dużej mierze na wypowiedziach posłów (Kaleta, Warchoł, Czarnek, Wójcik) i rzecznika, nie lidera.

## Morawiecki

- Projekt jest [dok], ale nie wiadomo, czy obejmuje stanem spoczynku sędziów z 2026 roku; brak stanowiska wobec ślubowania (jest Szczuckiego [media x1]); druku w Sejmie nie znaleziono; brak historii klubu; nazwisk autorów projektu karta nie podaje. Nowa: karta nie ma żadnego dosłownego cytatu Morawieckiego; jego propozycja wotum jest znana z mowy zależnej mediów, a projekt klubu jest dokumentem bez jego podpisu.
- Nowa: funkcja byłego premiera wynika tylko pośrednio (Płaczek o "dwóch byłych premierach", wypowiedź z 2022 roku); brak stanowiska wobec policji w TK, przerwy w czynnościach i Zgromadzenia z 2026.11.03; brak informacji, czy klub zbiera podpisy pod projektem i czy ma kandydata na premiera poza Markiem Jurkiem; propozycja wotum nieufności tylko [media x3] bez dokumentu klubu.

## Kosiniak-Kamysz

- Brak zapisu funkcji w rządzie (Płaczek o "wicepremierze" bez nazwiska); plan PSL milczy o ślubowaniu, kierownictwie TK, sędziach z 2026 roku i dawnych wyrokach; wariant "wygaszenia TK" Pasławskiej tylko [media x1]; brak informacji, jak PSL głosowałoby przy wotum nieufności.
- Nowa: cytat "Konsekwentnie i od lat proponuję reset konstytucyjny" tylko [media x2], bez nagrania; tekst psl.pl jest bez podpisu autora; brak stanowiska PSL wobec policji w TK, przerwy, Zgromadzenia i żądania z RBN; brak informacji, co Kosiniak-Kamysz mówił u Prezydenta 2026.10.31 poza tytułem relacji; nie wiadomo, czy koło NOWA Polska-Centrum w Senacie jest związane z PSL, Polską 2050 czy z nikim.

## Czarzasty

- Stanowisko tylko z mediów [media x2-x3]; brak stanowiska klubu wobec ustawy 3/5; brak stanowiska Lewicy wobec resetu poza cytatem Czarzastego; nieobecność Lewicy na konsultacjach bez wyjaśnienia [media x1].
- Nowa: komunikat Sejmu z 2026.10.14 nie opisuje formy ślubowania Berka; brak dokumentu Marszałka o odmowie nadania biegu projektowi budżetu Prezesa (tylko media); brak stanowiska Lewicy wobec dawnych wyroków (w tym K 1/20) w kontekście resetu, choć klub głosował w 2024 roku za ich nieważnością; brak opisu roli Marszałka w nocy z 2026.10.30 na 31 i 2026.11.03; brak trybu odwołania Marszałka.

## Hołownia

- Jedna wypowiedź [media x2]; nie wiadomo, kto kieruje partią po 2026.10.24; brak stanowiska wobec ślubowania i wotum nieufności.
- Nowa: relacja RMF24 ma w adresie słowa o "woli ze strony prezydenta", ale repozytorium nie cytuje tej części, więc karta jej nie używa; brak stanowiska klubu wobec policji w TK, przerwy, Zgromadzenia; brak informacji, czy Hołownia pełnił wcześniej funkcję Marszałka Sejmu (repozytorium tego nie zapisuje, więc karta o tym nie mówi); związek koła NOWA Polska-Centrum w Senacie z Polską 2050 nieustalony.

## Centrum (bez postaci)

- Brak nazwiska lidera i jakiegokolwiek stanowiska; znany tylko sposób głosowania w 2026 roku, udział posła Ćwika w komisji 2026.04.28 (Prezydent "popełnia delikt konstytucyjny"?) i nieobecność na konsultacjach 2026.10.31 [media x1]. Reguła arbitra, że Centrum liczy się jak KO, pozostaje założeniem.

## Bosak

- "Konkretny pomysł" z 2026.11.03 nieznany; wpisy Mentzena na X nieodczytane; liczba 46 posłów do losowania tylko z mediów; relacja Konfederacji z PiS i z Prezydentem nieopisana.
- Nowa: obie karty Bosaka (2026.11.03, 2026.11.04) opierają się na napisach automatycznych bez odsłuchu, z błędami w nazwiskach i niepewnym przypisaniem zdań (np. wariant "dwa tygodnie" może pochodzić od prowadzącego); dwa różne stanowiska o ślubowaniu (Marszałek 2026.10.31, Prezydent 2026.11.04) bez wyjaśnienia zmiany; głos Bosaka przy wyborze Święczkowskiego w 2022 roku nie sprawdzony; twierdzenie o egzaminie radcowskim Korwin-Piotrowskiej niezweryfikowane; brak informacji, czy projekt uchwały o skróceniu kadencji powstał.

## Święczkowski

- Brak dat końca kadencji wszystkich piętnaściorga poza Wyrembakiem; brak dnia początku kadencji Święczkowskiego jako sędziego (wybrany 2022.02.08) i daty końca kadencji Prezesa (wyliczenie projektu: 2030.12.09); brak jego wypowiedzi o warunkach stanu spoczynku albo rezygnacji; brak komunikatu TK po wyroku TSUE; nieznany termin i skład w Kpt 1/26; nie wiadomo, czy w grupie siedmiorga są różnice wobec porozumienia.
- Nowa: brak własnych cytatów Święczkowskiego z 2026.10.30-11.04 (są komunikaty TK i relacje mediów o stanowisku "Święczkowski i Stelina"); treści pisma do komisji z 2026.04.28 nie ma; nie wiadomo, kto wniósł zażalenie II ZZ 2/26; nie wiadomo, czy Piskorski i Zielonacki zakończyli kadencje (nie ma ich na liście siedmiorga ani na liście strony TK), więc karta nie wyjaśnia, dlaczego grupa liczy siedmioro; brak przepisu o pełnym składzie; brak informacji, co Prezes robi w czasie przerwy i gdzie orzeka.

## Korwin-Piotrowska

- "Stanowiska wobec scenariuszy nie znaleźliśmy"; odmowa orzekania przez Patyrę tylko [media x2]; przebieg Zgromadzenia z 2026.11.03 tylko z mediów; nie wiadomo, czy ośmioro działa wspólnie; długość aplikacji (decyduje o stażu); brak stanowiska wobec resetu, który oznaczałby także ich odejście.
- Nowa: brak jej własnych słów o rozwiązaniu sporu (cytaty to komunikaty urzędowe i wypowiedź z komisji o prawie); brak informacji, czy czworo nadal jest gotowe ślubować w Pałacu (Dziurda, 2026.04.28) po K 3/26 i po 2026.10.30; nie wiadomo, kto jest zawiadamiającym w zawiadomieniu PiS poza nazwą partii [media x1]; brak informacji o Szostku (nie ma go na liście strony TK mimo ślubowania); brak dokumentu o wejściu od strony KPRM poza jej komunikatem; nie ustalono, czy Zgromadzenie ośmiorga zamierza rozpoznać wnioski o immunitet.

## Luki metodyczne dla etapu 3

1. **Rozmiar pakietu:** 27 100 słów to według pomiaru recenzenta (endpoint `count_tokens`, `claude-opus-5-5`) 118 529 tokenów, a pakiet minimalny (14 100 słów) 64 845 tokenów; to około 4,3 tokena na słowo, ponad trzykrotnie więcej niż 35 tys. tokenów założone w etapie 1 i prawie dwa razy więcej niż mój pierwszy szacunek. Karty prywatne mają 3-8 tys. tokenów zamiast 1,5 tys. Wybór wersji pakietu i liczby przebiegów należy do agenta budującego skrypt po przeliczeniu kosztu od nowa.
2. **Cytaty z mediów:** większość stanowisk polityków w kartach pochodzi z relacji medialnych [media x1-x3] bez nagrań; karty oznaczają jakość źródła przy każdym cytacie, ale postać będzie je traktować jako własne słowa.
3. **Postacie bez własnych słów:** Kaczyński (jedna wypowiedź), Hołownia (jedna), Morawiecki (żadnego dosłownego cytatu), Święczkowski i Korwin-Piotrowska (komunikaty urzędowe) mają karty zbudowane głównie z wypowiedzi otoczenia i dokumentów instytucji; wynik symulacji dla nich będzie w większym stopniu wynikiem modelu niż repozytorium.
4. **Kworum i status osób:** arbiter liczy głosy Sejmu, ale nie rozstrzyga, kto jest Zgromadzeniem Ogólnym TK ani kto jest sędzią; pakiet, który zakłada uchwałę Zgromadzenia (immunitety, kandydaci na Prezesa), arbiter może tylko oznaczyć jako zależny od sporu o skład.

## Zmiany po recenzji (runda 1)

Recenzja: komentarz w issue #46 (https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6629816916), recenzent Claude Opus 5.5. Wersja 2 zapisana w osobnym katalogu; wszystkie 14 plików, także niezmienione.

Blokery:

- **B1 (szacunek tokenów): poprawione.** `pakiet-wiedzy.md` podaje liczby zmierzone przez recenzenta (118 529 i 64 845 tokenów) z metodą, przelicznik 4,4 tokena na słowo dla pozostałych liczb i nowy rachunek stałej części kontekstu; `luki.md` pkt 1 przepisany; limit wypowiedzi w `arbiter.md` i w części wspólnej `warianty-motywacji.md` to 250 słów, czyli 1100 tokenów.
- **B2 (fakt a ocena): poprawione.** Przyjąłem jedną regułę (zasada 1): oznaczone analizy repozytorium o przepisach i stanie spraw zostają wszędzie, a wypadają oceny odpowiedzialności, czyli zdania nazywające czyjeś działanie błędem lub numerujące kroki do kryzysu; w `historia-sporu.md` wypadają cztery takie zdania (2015.12.03, 2021.05.07, 2025.12.18, 2017.10.24), a trzy zostają, i tak samo zostają "Ocena obu analiz" i "Wnioski" w `zgromadzenie-2026-11-03.md`; wiersze 4 i 6 tabeli i tabela wyłączeń uzasadniają to tą regułą.
- **B3 (karta Kaczyńskiego): poprawione.** (a) Wotum nieufności oddzielone od dróg do wcześniejszych wyborów (art. 98 ust. 3, art. 155 ust. 2, art. 225); (b) "307 z 313 pozostałych, można stracić najwyżej 6" w tabeli i w części 4; (c) "6 wniosków z 2026 roku (w tym ponowiony w sprawie Pegasusa), siódmy dotyczy Sochańskiego" w karcie Kaczyńskiego i w częściach 1 i 5 karty Święczkowskiego.
- **B4 (słowa z adresu URL): poprawione.** Usunąłem "alternatywa to chaos" z części 2, 4 i 5 karty Kosiniaka-Kamysza; w części 2 zostaje tylko informacja, że repozytorium ma adres relacji Polsatu bez treści; "To ostatni moment" oznaczone jako słowa z adresu artykułu, nieprzypisane Pasławskiej.
- **B5 (nierówne traktowanie): poprawione.** Każda karta ma w części 3 punkt "Korekty repozytorium do wypowiedzi Twojego obozu" według jednej zasady: Nawrocki (Bogucki nr 3, 5, 7, 13), Tusk (Jaskulski nr 38, Żurek nr 28, 30, 33-34, 36, Karolewska nr 20), Kaczyński (Warchoł nr 47, Kaleta nr 43 i 46, Czarnek), Hołownia (Śliz nr 49-50), Korwin-Piotrowska (nr 23-26, Karolewska), Święczkowski (nr 30, 37), Bosak (bez zmian treści); Czarzasty, Kosiniak-Kamysz i Morawiecki dostają "korekt brak" z uzasadnieniem; dopisek "(żeby postać o tym wiedziała)" usunięty.

Uwagi nieblokujące:

- **1 (cudzysłów przy parafrazach): poprawione.** Usunąłem cudzysłowy albo przywróciłem dosłowne brzmienie w kartach Bosaka ("autyskwalifikacji" jak w napisach), Czarzastego, Korwin-Piotrowskiej (sędzia z Opola), Morawieckiego (dwaj byli premierzy), Święczkowskiego ("oczekuje na stanowisko pana prezydenta", "najbliższym człowiekiem ministra Ziobry"), Nawrockiego ("twardej odpowiedzi", "popełnia delikt konstytucyjny") i w `luki.md`; "TK jest ciałem politycznym" zostaje, bo jest dosłowne ("jest ciałem politycznym", 8:03).
- **2 (data końca kadencji Wyrembaka): poprawione.** Karty Nawrockiego, Kaczyńskiego i Święczkowskiego podają "styczeń 2027" za Komitetem Ministrów i wyliczenie 2027.01.30 z początku kadencji 2018.01.30 (`badania/kierownictwo-2016.md`) i art. 194 ust. 1, jako wyliczenie wykonawcy.
- **3 (źródło cytatu Żurka): poprawione.** Karta Tuska wskazuje `zrodla/okres-2024-2026/spc-149-2026-04-28.md`, linia 456.
- **4 (98 obsadzonych miejsc): poprawione.** `arbiter.md`, część 3.
- **5 (skutek reguły o klubach nieobecnych dla wotum): poprawione.** `arbiter.md`, pkt 4.4 podaje 204, 236, 225 i rzeczywiste 231.
- **6 ("poza gwarancją stołu" dla wszystkich): poprawione.** Reguła dopisana do pkt 8 części wspólnej `warianty-motywacji.md`; karta Tuska odsyła do niej.
- **7 (pozycja PSL): poprawione.** Karta Kosiniaka-Kamysza w częściach 1, 4 i 5 wymienia Lewicę jako drugi klub, który sam domyka 231, oraz Polskę 2050 i Centrum z Razem i niezrzeszonymi.
- **8 (art. 225 i odwołania do etapu 1): poprawione.** Zdanie o art. 225 oznaczone jako wniosek wykonawcy z wyprowadzeniem; w kartach "wyliczenie etapu 1" zastąpione wyliczeniem wykonawcy z `badania/sily-i-glosy.md`, a odwołania do luk etapu 1 zastąpione stwierdzeniem, że repozytorium tego nie zapisuje; `pakiet-wiedzy.md`, `arbiter.md` i `luki.md` nadal wymieniają etap 1, bo nie trafiają do postaci.
- **9 (brak cytatu Morawieckiego): poprawione.** Dopisane w `luki.md` przy Morawieckim i w lukach metodycznych pkt 3.
- **10 (M.P. 2026 poz. 302): poprawione.** Karta Korwin-Piotrowskiej podaje zakres poz. 300-305 bez przypisania nazwisk.
- **11 (droga A, deklaracja Święczkowskiego): poprawione.** Arbiter prosi tylko o czynności Prezesa (skład, termin) i zapisuje wynik sprawy jako nieznany.
- **12 (warunek c): poprawione.** "bez której głosów suma spada poniżej progu".
- **13 (zakresy linii): poprawione.** Art. 135 to linie 730-731; pełne tabele głosowań to 43-305.
- **14 (migawka issue): bez zmian,** recenzent nie wskazał błędu.
