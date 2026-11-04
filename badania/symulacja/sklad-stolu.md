> Analiza składu stołu do [symulacji negocjacji (issue #46)](https://github.com/gebawkubel/trybunal/issues/46). Napisał Claude Fable 5.1 (wysoki wysiłek rozumowania, agent Claude Code) według [polecenia](polecenie-sklad.md), na repozytorium w wersji 78e9e45, bez internetu. Zakazy (internet, zmiany, wskazane pliki z wnioskami) były w poleceniu i wiadomości zlecającej, nie wymuszone technicznie. Model zgłosił, że jedno wyszukiwanie w katalogu `badania/` zwróciło przypadkiem pojedyncze linie z plików, których miał nie czytać (rekomendacje modeli, bilans propozycji); według niego nie otwierał ich i nie użył ich treści. To ocena modelu, nie ustalenie projektu; fakty sprawdził osobny recenzent (zob. [historia prac](../../historia-prac.md#symulacja-negocjacji-skład-stołu-issue-46)). Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `b2f7bf75e2d58ef262d23a708de7d6254f48f2d69c113648489c7c02e084a67f`.

---

# Skład stołu do symulacji negocjacji o TK

Stan repozytorium: 2026.11.04. Źródła: `historia-sporu.md`, `badania/sily-i-glosy.md`, `badania/warunki-rozwiazan.md`, `badania/propozycje-na-stole.md`, `badania/scenariusze-naprawy.md` (fakty, scenariusze, indeks stron), `badania/okres-2024-2026.md`, `badania/zgromadzenie-2026-11-03.md`, `zrodla/konstytucja.md` i karty z `zrodla/okres-2024-2026/`. Plików z rekomendacjami i bilansem nie czytałem. Liczby przy pełnej sali (460 posłów, 99 senatorów). Zdania od "Ocena:" to moja ocena, nie fakt z repozytorium.

Zasada doboru: przy stole siedzi tylko ten, kto sam albo w małej grupie może zablokować rozwiązanie, albo bez kogo nie da się go wykonać. Arbiter nie negocjuje; liczy głosy według progów z części 1.

## 1. Ścieżki rozwiązania i kto ma w nich weto

Sejm (`badania/sily-i-glosy.md`): KO 156, PiS 147, Rozwój Plus 40, PSL 32, Lewica 21, Konfederacja 17, Polska 2050 15, Centrum 15, niezrzeszeni 7, Razem 4, Korona 3, Demokracja Bezpośrednia 3. Koalicja (KO, PSL, Lewica, Polska 2050, Centrum) ma 239. Senat (`zrodla/okres-2024-2026/senat-sklad-2026-11.md`): KO 42, PiS 31, Lewica 8, Trzecia Droga 8, NOWA Polska-Centrum 6, Rozwój Plus 2, niezrzeszeni 2; kluby koalicji mają 58 z 99.

### A. Zwykła ustawa (np. nowa ustawa o TK z wyborem 3/5)

- **Sejm: 231** (art. 120). Koalicja ma 239, zapas 8. Bez PSL 207, bez Lewicy 218, bez Polski 2050 albo Centrum 224. Każdy klub koalicji ma weto arytmetyczne.
- **Senat:** może odrzucić lub poprawić, Sejm odrzuca to bezwzględną większością (art. 121 ust. 3). Koalicja ma 58 z 99, więc Senat nie blokuje.
- **Prezydent:** podpisuje, wetuje albo kieruje do TK; nie może zrobić obu rzeczy naraz (art. 122 ust. 3-5). Weto realne.
- **TK pod Prezesem Święczkowskim:** może uznać ustawę za niekonstytucyjną w całości, jak w Kp 3/24; wtedy Prezydent odmawia podpisu i żadna większość tego nie zmienia (art. 122 ust. 4). Wniosek może złożyć też 50 posłów (art. 191), więc PiS sam uruchamia tę blokadę nawet po podpisie. Weto pośrednie, realne.
- **Marszałek Sejmu:** bez formalnego weta, ale prowadzi obrady i proces (art. 110, 122 ust. 1). Ocena: wpływ na tempo i porządek, nie na wynik.

Niezbędni: Premier, Prezydent, Prezes TK (brak wyroku blokującego). Dodatkowo każdy lider klubu koalicji.

### B. Ustawa przy wecie Prezydenta

- **276** (art. 122 ust. 5). Koalicja i Rozwój Plus: 279. Koalicja i PiS: 386. Wszyscy poza PiS i Rozwojem Plus: 273, o 3 za mało. Blokada to 185 przeciw: PiS z Rozwojem Plus (187) blokuje, PiS z Konfederacją (164) nie.
- Po odrzuceniu weta Prezydent nie może już kierować ustawy do TK (art. 122 ust. 5), ale 50 posłów może. TK zostaje wetem pośrednim.

Niezbędni: cała koalicja (przy 279 nie wolno stracić nawet 4 głosów) oraz Morawiecki albo Kaczyński.

### C. Zmiana Konstytucji (reset, nowe zasady wyboru, likwidacja TK)

- **Inicjatywa:** 92 posłów, Senat albo Prezydent (art. 235 ust. 1). Pierwsze czytanie najwcześniej 30. dnia (ust. 3).
- **Sejm: 307** (ust. 4). Koalicja z PiS: 386. Bez PiS: koalicja, Rozwój Plus, Konfederacja i Razem to 300, trzeba jeszcze 7 z 13 posłów niezrzeszonych, Korony i Demokracji Bezpośredniej.
- **Blokada: 154.** KO sama (156) blokuje. PiS sam (147) nie, ale blokuje z Rozwojem Plus (187), z Konfederacją (164) albo z 7 z tych samych 13 posłów. Ocena: w wariancie bez PiS decyduje 13 posłów, których stanowisk repozytorium nie zna.
- **Senat:** bezwzględna większość (ust. 4); koalicja ma 58 z 99, nie blokuje, ale ma 60 dni (ust. 2).
- **Prezydent:** "podpisuje ustawę w ciągu 21 dni" (ust. 7). Czy może skierować ją do TK, repozytorium nie rozstrzyga (`badania/warunki-rozwiazan.md`, pkt 2). Ocena: bez weta, ale z głosem przez inicjatywę i przez TK.

Niezbędni: Tusk oraz Kaczyński albo pakiet Morawiecki, Konfederacja, Zandberg i 7 z 13 posłów. Lewica (21) nie ma weta arytmetycznego, ale Marszałek Czarzasty, który odrzuca zmianę Konstytucji (2026.11.02), prowadzi proces.

### D. Porozumienie polityczne bez ustawy

Treść według scenariuszy 1 i 2: Prezydent odbiera ślubowanie od pięciorga sędziów z 2026 roku albo Sejm uznaje ślubowanie wobec Prezydenta za jedyną drogę; Prezes TK dopuszcza sędziów i zwołuje Zgromadzenie; Korwin-Piotrowska cofa przerwę w czynnościach Prezesa i Wiceprezesa; rząd wycofuje policję i publikuje wyroki; Prokurator Generalny wstrzymuje wnioski o immunitety.

Niezbędni: Prezydent (ślubowanie, prerogatywa według K 3/26), Prezes Święczkowski (dopuszczenie, zwołanie Zgromadzenia, art. 7 ust. 2 ustawy o TK), Korwin-Piotrowska i sędziowie z 2026 roku (przerwa, zarządzenia, kworum), Premier (policja, Dziennik Ustaw, podległy mu Prokurator Generalny Żurek), Marszałek Sejmu (ślubowania w Sejmie, uchwały). Posłowie opozycji formalnie zbędni.

### E. Inne ścieżki z repozytorium

- **Skrócenie kadencji Sejmu:** zawsze 307 z ustawowej liczby (art. 98 ust. 3). Bez KO niemożliwe. Zapowiedź Bosaka (2026.10.31) bez druku.
- **Konstruktywne wotum nieufności:** 231 (art. 158). Opozycja prawicowa, Razem i niezrzeszeni to najwyżej 221, więc potrzebny klub koalicji, najprościej PSL (32). Pomysł Morawieckiego (2026.10.31).
- **Czekanie do wyborów 2027** (Prezydent, 2026.10.15): nie wymaga nikogo. To domyślny wynik "brak porozumienia".

## 2. Kandydaci

| Kandydat, stanowisko z datą | Zaprosić | Dlaczego | Gdy go zabraknie |
|---|---|---|---|
| **Karol Nawrocki**, Prezydent. Reset po 2027 roku, ślubowanie tylko wobec niego, "twarda odpowiedź" (2026.10.15); RBN 2026.11.03: termin dla premiera przed 11 listopada; Bogucki 2026.11.03: "ostatecznie tak" dla restartu, "nie z Donaldem Tuskiem" | tak | weto w A, ślubowanie w D, inicjatywa w C, powołuje Prezesa TK (art. 194 ust. 2) | zostaje tylko B (276) albo C; pięcioro sędziów nadal bez ślubowania |
| **Donald Tusk**, Premier, KO (156). "Bez zmian w Konstytucji" (2026.11.02), apel o dopuszczenie sędziów i oferta spotkania w cztery oczy (2026.11.03) | tak | jedyna osoba, która sama blokuje każdą ścieżkę ustawową: 231 i 307 (156 > 154); rząd kontroluje budynek, publikację wyroków i prokuraturę | żadna ustawa ani wykonanie D |
| **Jarosław Kaczyński**, PiS (147, Senat 31). Partia: scenariusze 2 i 5; wobec resetu brak oficjalnego stanowiska, Wójcik przeciw (2026.10.27), Czarnek: dymisja rządu (2026.11.02). Kaczyński 2026.09.29 pod TK wezwał do oporu społecznego. Repozytorium nie mówi, kto formalnie kieruje PiS; przyjmuję jedynego lidera z własną wypowiedzią | tak | z PiS ścieżki B i C są proste (386); bez PiS C wisi na 7 z 13 posłów; PiS z Rozwojem Plus blokuje B i C | symulacja testuje tylko wąską ścieżkę "wszyscy przeciw PiS" |
| **Mateusz Morawiecki**, Rozwój Plus (40, Senat 2). Projekt zmiany Konstytucji (2026.10.07), wotum nieufności i rząd Jurka (2026.10.31). Szczucki jest współautorem projektu, klubem kieruje Morawiecki | tak | jedyny klub opozycji, który z koalicją daje 276; z PiS blokuje B i C; jedyny obóz z gotowym tekstem | B wymaga PiS; stół traci jedyny konkretny projekt opozycji |
| **Władysław Kosiniak-Kamysz**, PSL (32, Trzecia Droga w Senacie 8). "Od 2024 roku lider PSL konsekwentnie postuluje reset konstytucyjny" (psl.pl, 2026.11.03); plan Pasławskiej 2026.11.02: wygaszenie kadencji, wybór 3/5. Wybieram lidera, bo tekst PSL przypisuje linię jemu | tak | bez PSL koalicja ma 207; jedyny koalicjant z planem resetu; klucz do wotum nieufności | nie wiadomo, czy koalicja ma 231 i czy reset ma most do koalicji |
| **Włodzimierz Czarzasty**, Marszałek Sejmu, Lewica (21). "Nie poprę żadnego resetu, nie poprę zmiany konstytucji" (2026.11.02); odmówił biegu projektowi budżetu TK od Święczkowskiego | tak | dwie funkcje: 21 głosów (koalicja bez Lewicy 218) i Marszałek prowadzący ustawę, zmianę Konstytucji i ślubowania w Sejmie | nie wiadomo, czy projekt trafi pod obrady; w D brak organu od ślubowań w Sejmie |
| **Szymon Hołownia**, szef klubu Polska 2050 (15). TK "zlikwidowany albo odbudowany", bez planu (2026.10.31). Kto kieruje partią po 2026.10.24, nie ustalono | tak | koalicja bez Polski 2050 ma 224: weto w A i B; jedyny głos za likwidacją TK | arbiter zakłada lojalność klubu bez karty |
| **Centrum** (15). Lidera i stanowiska brak (`badania/sily-i-glosy.md`) | nie w składzie podstawowym | weto arytmetyczne jak Polska 2050, ale karty nie da się napisać bez zmyślania | arbiter liczy Centrum z koalicją; po uzupełnieniu luki 9. osoba w wariancie ustawowym |
| **Krzysztof Bosak**, wicemarszałek Sejmu, Konfederacja (17). Reset 3/5 z losowaniem (2026.10.31), projekt skrócenia kadencji "jeśli nie będzie skłonności do porozumienia", po RBN "wyborcy muszą pomóc" (2026.11.03). Alternatywa: Mentzen ("wyzerować", 2026.10.31; kworum, 2026.11.03). Ocena: Bosak, bo reprezentował Konfederację na RBN | tak | w C bez PiS niezbędny; z PiS blokuje C (164); Mentzen w 2026.04 dopuszczał ślubowanie przed Prezydentem, możliwy most w D | C bez PiS znika; brak obozu, który grozi rozwiązaniem Sejmu |
| **Adrian Zandberg**, Razem (4). Reset zabezpieczony w Konstytucji, "wszyscy do stołu", "ci drudzy nie znikną" (2026.10.31, 2026.11.03) | tylko wariant konstytucyjny | 4 głosy bez weta, ale w C bez PiS potrzebne; jedyny z deklarowaną rolą pośrednika | w C bez PiS brakuje 4 głosów |
| **Małgorzata Kidawa-Błońska**, Marszałek Senatu. Z 2024 roku projekt resetu (druk 55); z 2026 roku brak | nie | Senat ma 58 głosów koalicji, decyzje zapadają w klubach reprezentowanych przez Tuska i Kosiniaka-Kamysza; Senat nie blokuje A, B ani C | arbiter: Senat głosuje jak kluby w Sejmie |
| **Bogdan Święczkowski**, Prezes TK. K 3/26, niedopuszczenie pięciorga sędziów, bojkot Zgromadzenia (2026.11.03), własny projekt budżetu TK | tylko wariant bez ustawy | w D bez niego nie ma dopuszczenia ani Zgromadzenia; w A i B jego TK to weto pośrednie, które arbiter odwzorowuje regułą (linia Kp 3/24, K 3/26), nie krzesłem, bo sędzia nie negocjuje ustaw | w D porozumienie nie ma wykonawcy po stronie TK |
| **Anna Korwin-Piotrowska** i sędziowie z 2026 roku. Stanowiska wobec scenariuszy nie znaleziono; działania: przerwa (2026.10.30), Zgromadzenie ośmiorga (2026.11.03), odmowa uznania kompetencji SN | tylko wariant bez ustawy | przerwa, zarządzenia i kworum zależą od niej; rząd ją popiera, ale formalnie nie wiąże; ETPC dał środek tymczasowy czworgu | w D nie ma kto cofnąć przerwy |
| Żurek, Bogucki, Bochenek, Czarnek | nie | podlegli lub rzecznicy obecnych stron; ich słowa idą do kart Tuska, Nawrockiego i Kaczyńskiego | - |
| Kukiz, Braun, 7 niezrzeszonych (13) | nie | realni tylko w C bez PiS; stanowisk brak poza Kukizem (2/3); 13 kart nie da się napisać | reguła arbitra: 7 z 13 głosuje "za" tylko, gdy projekt ma próg 2/3 albo losowanie |
| Pierwszy Prezes SN, RPO, Komisja Wenecka, ETPC, TSUE, Batory, HFPC, Klub Jagielloński, Iustitia | nie | bez weta; ich opinie i wyroki to materiał do kart i reguł arbitra | - |

## 3. Skład podstawowy i warianty

**Skład podstawowy (8 osób):** Nawrocki, Tusk, Kaczyński, Morawiecki, Kosiniak-Kamysz, Czarzasty, Hołownia, Bosak. Arbiter poza stołem.

Dlaczego nie mniej: każdy ma samodzielne albo dwuosobowe weto w A, B lub C. Tusk i Nawrocki w A; Kosiniak-Kamysz, Czarzasty i Hołownia przez 231; Kaczyński i Morawiecki przez 276 i 307; Bosak przez jedyną ścieżkę 307 bez PiS. Usunięcie dowolnej osoby zamyka co najmniej jedną ścieżkę przed startem.

Dlaczego nie więcej: Centrum, Razem, Senat, sędziowie i 13 posłów spoza klubów nie mają weta w A, B ani w C z PiS. Ich wpływ arbiter odwzorowuje regułami (Centrum i Senat głosują z koalicją; TK pod Święczkowskim uchyla ustawę, która unieważnia wyroki albo narzuca Prezydentowi ślubowanie, jak w Kp 3/24). Osiem osób to też granica czytelności wątku, w którym każdy mówi po kolei.

**Wariant K (ścieżka konstytucyjna, 9 osób):** skład podstawowy plus Zandberg. W C bez PiS Razem jest potrzebne arytmetycznie i jako jedyne żąda, by "wszyscy usiedli do stołu". Reguła dla 13 posłów obowiązuje. Po uzupełnieniu luki o Centrum dochodzi dziesiąta osoba.

**Wariant D (porozumienie bez ustawy, 5 osób):** Nawrocki, Tusk, Czarzasty, Święczkowski, Korwin-Piotrowska. W D nie liczy się głosów, tylko czynności: ślubowanie (Prezydent), dopuszczenie i Zgromadzenie (Prezes TK), cofnięcie przerwy (Korwin-Piotrowska), policja, publikacja i prokuratura (Premier), Sejm (Marszałek). Nacisk Kaczyńskiego, Morawieckiego i Bosaka na Prezydenta arbiter podaje jako tło w karcie Nawrockiego. Ocena: najtańszy przebieg i najbliższy temu, co dzieje się między 2026.10.30 a 11 listopada.

## 4. Warianty symulacji (9-12 przebiegów)

Motywacje: (a) dobro państwa ponad wszystko; (b) ugraj jak najwięcej, strać jak najmniej, ostatecznie dobro państwa; (c) czysty interes polityczny. Arbiter liczy 231, 276, 307, 154, 185 i 58 z 99 w Senacie i po każdej deklaracji ogłasza, która ścieżka jest otwarta.

| Nr | Skład | Motywacje | Po co |
|---|---|---|---|
| 1 | podstawowy | wszyscy (b) | linia bazowa: czy cokolwiek się domyka i którą ścieżką |
| 2 | podstawowy | wszyscy (c) | kontrola dolna: oczekiwany brak porozumienia; sprawdza, czy karty i arbiter nie "dopychają" zgody |
| 3 | podstawowy | wszyscy (a) | kontrola górna: najlepszy możliwy wynik; czy istnieje ścieżka bez zmiany Konstytucji |
| 4 | D | (b) | czy spór o budynek, ślubowania i immunitety da się wygasić bez opozycji |
| 5 | D | (c) | czy w D ktokolwiek ma interes w ustępstwie; czy termin "przed 11 listopada" cokolwiek zmienia |
| 6 | K | (b) | czy reset ma 307 z PiS, czy bez PiS; test reguły 13 posłów |
| 7 | K | Kaczyński (c), reszta (b) | najważniejszy test asymetryczny: czy C bez PiS jest realne, gdy PiS gra na blokadę |
| 8 | podstawowy | Nawrocki (c), reszta (b) | czy sam Prezydent zamyka wszystko poza 276 i 307 |
| 9 | podstawowy | Tusk (c), reszta (b) | czy sam Tusk blokuje reset (156 > 154) |
| 10 | K | (a) | czy przy dobrej woli reset ma treść do przyjęcia przez obie strony (sędziowie z 2026 roku, dawne wyroki) |
| 11 | podstawowy | (b), inny seed | powtórzenie 1: stabilność wyniku |
| 12 | wariant, który się domknął | (c) | czy porozumienie przeżywa zmianę motywacji na czysto polityczne |

Kolejność: 1, 2, 4, 7, 6, 3, 8, 9, 5, potem 10-12, jeśli budżet pozwoli. Najpierw linia bazowa i dolna kontrola, potem tani wariant D, potem test 7, bo repozytorium wskazuje, że bez PiS albo Rozwoju Plus nie ma trwałego rozwiązania (`badania/sily-i-glosy.md`, "Wniosek z rachunku").

Reguły wspólne: brak porozumienia to dozwolony wynik; karty cytują tylko wypowiedzi z repozytorium z datą; arbiter nie dopisuje stanowisk, których nie ma, tylko ogłasza "brak danych" i wymaga od postaci decyzji uzasadnionej w jej logice.

## 5. Czego nie wiemy

- **PiS:** brak oficjalnego stanowiska wobec resetu; nie wiadomo, kto formalnie kieruje partią ani kto negocjowałby.
- **Centrum:** brak lidera, stanowiska i głosowań poza uchwałą z 2026.03.13. Dlatego bez krzesła.
- **Polska 2050:** nie wiadomo, kto kieruje partią po 2026.10.24; plan Hołowni to jedno zdanie.
- **Konfederacja:** kto rozmawia w imieniu partii (Mentzen czy Bosak) i czym jest "konkretny pomysł" z 2026.11.03.
- **Prezydent:** brak technicznej propozycji; słowa Boguckiego o "restarcie" nie są dokumentem Kancelarii; aprobata dla projektów Konfederacji i Rozwoju Plus niepotwierdzona; nierozstrzygnięte, czy może skierować zmianę Konstytucji do TK.
- **Sędziowie:** brak stanowiska ośmiorga z 2026 roku i siedmiorga sprzed 2026 roku wobec scenariuszy, stanu spoczynku i prawa ponownego kandydowania; niepewne, czy Korwin-Piotrowska ma najdłuższy staż (`badania/zgromadzenie-2026-11-03.md`, pkt 4).
- **13 posłów spoza klubów:** stanowisk brak poza Kukizem; nie wiadomo, czy kluby głosują jednolicie.
- **Senat:** stanowisko Marszałek Senatu z 2026 roku i los druku 55 nieznane; mandat po Różańskim nieobsadzony.
- **Treść porozumienia:** żadna propozycja poza Klubem Jagiellońskim nie mówi, co z dawnymi wyrokami; PSL i Rozwój Plus nie mówią, czy wygaszenie obejmuje sędziów z 2026 roku.
- **Proces:** nie wiadomo, czy po 2026.10.26 złożono jakikolwiek projekt (wykaz druków może być opóźniony) ani czy doszło do spotkania Tuska z Nawrockim w cztery oczy.
- **Komisja Wenecka 2026:** odczytano tylko pkt 96-98.
- **Issue #46:** w kopii repozytorium nie ma jego treści; skład oparłem na opisie z polecenia.
