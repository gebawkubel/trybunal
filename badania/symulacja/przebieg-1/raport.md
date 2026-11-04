# Symulacja negocjacji, przebieg 1: raport

**To symulacja.** Wszystkie wypowiedzi napisał model AI (Claude Opus 5.5) grający prawdziwe osoby. Nie są to słowa tych osób i nie jest to przewidywanie, co zrobią. Symulacja sprawdza, jakie porozumienie da się złożyć przy założeniach z [issue #46](https://github.com/gebawkubel/trybunal/issues/46).

Przebieg odbył się 2026.11.04 w godzinach 14:03-14:29. Przy stole zasiadło 10 postaci w składzie W1 z [etapu 1](../etap-1.md), z wariantem motywacji (b): "ugraj jak najwięcej, ale ostatecznie dobro państwa". Raport napisał koordynator (Claude Opus 5.5) z [zapisu rozmowy](zapis.md). Numery w nawiasach to numery wypowiedzi w zapisie.

## Czy symulacja działa

Tak. Rozmowa przeszła wszystkie fazy przewidziane w skrypcie:
- otwarcie;
- 3 rundy dyskusji, w każdej 1 głos poza kolejnością;
- głosowanie;
- dodatkowa runda;
- powtórne głosowanie.

Skrypt zapisał 81 wywołań modelu, w tym 73 wypowiedzi postaci. Arbiter ogłosił wynik według reguł.

**Koszt:** 14,50 USD, policzony z pola `usage` w odpowiedziach API. Szacunek przed przebiegiem wynosił około 18 USD ([README skryptu](../../../narzedzia/symulacja/README.md)). Większość tokenów to odczyt z bufora, czyli tańsze ponowne użycie tekstu wysłanego już wcześniej do modelu (12,6 mln). Zapis do bufora wyniósł 1,16 mln, a tekst napisany przez model, z rozumowaniem, 131 tys. tokenów.

**Co trzeba poprawić przed kolejnymi przebiegami:**
1. **Ucięte wypowiedzi.** Skrypt ucina wypowiedź po 1100 tokenach tekstu (to reguła skryptu, nie przerwanie przez API). Ucięte zostało 10 wypowiedzi: 1 w dyskusji, 3 w pierwszym głosowaniu i 6 w powtórnym. W dyskusji ucięcie urwało część B pakietu Hołowni (31), więc arbiter udzielił mu głosu poza kolejnością, by ją dokończył (36). W głosowaniach każdy głos "za" padł przed ucięciem, więc wynik się nie zmienia, ale części zastrzeżeń i zobowiązań brakuje. Limit trzeba podnieść albo skrócić wymagany format głosu.
2. **Ryzyko zbyt łatwej zgody.** Zarys porozumienia przyjęły wszystkie postacie już w drugiej rundzie dyskusji (25-34). Ten sam model gra wszystkich i może być zbyt ugodowy. Na przykład Włodzimierz Czarzasty mówił naprawdę 2026.11.02: "Nie poprę żadnego resetu, nie poprę zmiany konstytucji". Jego postać zaczęła od tego samego (7), a po dwóch rundach zmieniła zdanie (30). Rozstrzygną to dopiero kolejne przebiegi, zwłaszcza wariant (c), "czysty interes polityczny", oraz seria kontrolna na innym modelu.
3. **Porozumienie warunkowe.** Tekstu przepisów nie ma. Według pakietu napisze go zespół KO, PiS i Rozwoju Plus, a 2026.11.09 KO i PiS mają go parafować. Arbiter zapisał to jako warunek (81).

## Wynik

Arbiter ogłosił **porozumienie** (81). Wszystkie 10 postaci głosowało "za" pakietem nr 1, który złożył i uzupełniał Szymon Hołownia (31, 66). Każda postać dodała zastrzeżenia.

**Część A, zmiana Konstytucji:**
- 15 sędziów wybieranych przez Sejm większością 3/5 na 9 lat. Kandydatów zgłasza klub albo 15 posłów.
- 4 lata karencji, czyli przerwy przed wyborem na sędziego, dla polityków, także z Kancelarii Prezydenta.
- **Wszyscy obecni sędziowie przechodzą w stan spoczynku**, z zachowanym statusem i uposażeniem zapisanymi w Konstytucji.
- **Ośmioro wybranych w 2026 roku wchodzi do nowego składu z mocy przepisu przejściowego**, a nie na podstawie uchwał Sejmu z 2026 roku. Pozostałe 7 miejsc Sejm obsadza większością 3/5, a gdy w 60 dni nie ma wyboru, rozstrzyga losowanie. Kadencje całego pierwszego składu losuje publicznie PKW.
- Ślubowanie przed Prezydentem w 21 dni. Jeśli Prezydent pisemnie odmówi, Sejm wybiera ponownie większością 3/5, a ślubowanie odbywa się w 7 dni.
- Składy pięcioosobowe. Do uznania przepisu za niezgodny z Konstytucją w pełnym składzie potrzeba 2/3 głosów, w zamkniętym katalogu spraw. Katalog nie obejmuje praw jednostki.
- Prezesa powołuje Prezydent spośród kandydatów Zgromadzenia Ogólnego, na 3 lata. Wyroki ogłasza sam Trybunał.
- Bez przepisu o dawnych wyrokach. Działa tylko zwykła skarga i zwykłe pytanie prawne do nowego Trybunału, bez list i adnotacji.
- Postępowania dyscyplinarne wszczęte w sporze od 2026.04.01 umarza się, symetrycznie dla obu stron.

**Część B, 2026.11.10, bez zmiany prawa:**
- rano policja wychodzi z TK, Anna Korwin-Piotrowska uchyla zarządzenie o przerwie, a budynek i Straż Trybunalska wracają pod kierownictwo Prezesa Święczkowskiego;
- w południe czworo sędziów objętych środkiem tymczasowym ETPC ślubuje w Pałacu;
- tego samego dnia Prezes dopuszcza tę czwórkę do orzekania, a rząd ogłasza zaległe wyroki;
- KO i PiS składają projekt zmiany Konstytucji.

**Ustawa towarzysząca** wpływa do Sejmu najpóźniej 2026.11.17, a głosowania nad obiema ustawami odbywają się w lutym 2027 roku. Arbiter policzył 443 głosy w Sejmie przy wymaganych 307 i 91 w Senacie przy wymaganych 50. Przy klubach Trzeciej Drogi i Lewicy w Senacie to deklaracja przedstawiciela, a nie senatorów.

**Bezpieczniki:**
- jeśli 2026.11.10 ktoś nie wykona swojej czynności, pozostali odzyskują swobodę głosowania, a to, co już wykonano, zostaje;
- dopisanie przepisu o nieważności dawnych wyroków albo słów "zrzeczenie się urzędu" oznacza wycofanie głosów.

Poza gwarancją stołu zostały m.in. prokuratura, immunitety, PKW, ETPC, senatorowie oraz sędziowie, którzy nie siedzieli przy stole (81).

## Jak doszło do porozumienia

1. **Otwarcie.** Reset w jakiejś postaci proponowali Morawiecki (5), Kosiniak-Kamysz (6), Hołownia (8) i Bosak (9), a Prezydent popierał go pod trzema warunkami (2). Tusk wykluczył reset, "który wymaże wybór dokonany legalnie przez Sejm w 2026 roku" (3). Czarzasty odrzucił reset i zmianę Konstytucji w ogóle (7), a Korwin-Piotrowska wygaszenie kadencji wybranych na wolne miejsca (11).
2. **Pomost.** Kosiniak-Kamysz zaproponował, żeby ośmioro z 2026 roku trafiło z mocy Konstytucji na listę głosowaną łącznie większością 3/5 (17). Czarzasty chciał, żeby zostali bez ponownego głosowania, z kadencją od dnia wyboru (18). Hołownia połączył oba stanowiska. Ośmioro wchodzi z mocy przepisu przejściowego Konstytucji, uchwalonego także głosami PiS, ale z kadencjami losowanymi jak u wszystkich (19). Tak "nikt nie jest wymazany i nikt nie dostaje przywileju".
3. **Zgoda KO.** Tusk przyjął reset pod warunkiem wariantu Hołowni (26). Prezydent odrzucił kadencje liczone od wyboru w 2026 roku (25), a Czarzasty z nich zrezygnował (30).
4. **Cena PiS.** Kaczyński zauważył, że ośmioro z piętnaściorga to większość Trybunału, i zażądał progu 2/3 pełnego składu do stwierdzenia niezgodności (27). Kosiniak-Kamysz zawęził ten próg do wniosków organów i polityków (29; Czarzasty przyjął to w 30), a Bosak przyjął go, "bo bez niego ośmioro byłoby większością" (32). W pakiecie próg objął zamknięty katalog spraw, bez praw jednostki.

## Porównanie z wcześniejszymi analizami

Pakiet wiedzy postaci nie zawierał rekomendacji modeli, bilansu propozycji ani scenariuszy z analiz AI ([issue #46](https://github.com/gebawkubel/trybunal/issues/46)). Porównujemy je dopiero teraz.

**Co jest nowe.** Żadna znana nam propozycja z debaty nie łączy wprost stanu spoczynku obecnych sędziów z pozostawieniem w składzie ośmiorga wybranych w 2026 roku ([propozycje z debaty](../../propozycje-na-stole.md), tabela "Porównanie"):
- Konfederacja, Klub Jagielloński, HFPC i Razem: sędziowie z 2026 roku odchodzą jak wszyscy;
- Fundacja Batorego: ci, którzy orzekają, przechodzą w stan spoczynku, a pozostali mogą tylko ponownie kandydować;
- PSL i Rozwój Plus: los sędziów z 2026 roku jest niejasny.

Rekomendacje Fable i Astry odrzucały reset w ogóle ([rekomendacje modeli](../../rekomendacje-modeli.md)).

**Dlaczego to ważne.** Wcześniej [wnioskowaliśmy](../../odpowiedz.md), że zmiana Konstytucji nie przejdzie bez KO, a KO traci w każdym konkretnym projekcie resetu. Ten wariant omija ten problem: KO nie traci sędziów wybranych w 2026 roku. Koszt ponoszą obie strony. KO zgadza się na zmianę Konstytucji, losowanie kadencji i ślubowanie przed Prezydentem. PiS zgadza się, że w stan spoczynku przechodzą także sędziowie wybrani jego głosami, "w tym Prezes" (15), w zamian za próg 2/3, nowy tryb ślubowania i brak przepisu o dawnych wyrokach.

**Co było już wcześniej:**
- 15 sędziów, 3/5 i losowanie przy blokadzie: Konfederacja;
- próg 2/3: Klub Jagielloński (pełnego składu) i Rozwój Plus (składu orzekającego);
- losowane kadencje pierwszego składu: Konfederacja, Klub Jagielloński (losowanie przez PKW) i Bosak ([wywiad z 2026.11.04](../../bosak-2026-11-04.md));
- 3-letnia kadencja Prezesa: Fundacja Batorego;
- stan spoczynku z zachowaniem statusu: PSL, Rozwój Plus, Batory i Klub Jagielloński;
- kroki z 2026.11.10: Bosak oraz kompromis z Prezydentem z rekomendacji modeli;
- nieruszanie dawnych wyroków: zgodne z rekomendacjami modeli, odmienne od propozycji Klubu Jagiellońskiego.

Wariant dopisaliśmy do [scenariuszy naprawy](../../scenariusze-naprawy.md#scenariusze-z-symulacji-negocjacji).

**Czego ten przebieg nie pokazuje.** Jeden przebieg to anegdota. Nie wiadomo, czy ten sam wariant pojawi się przy innej motywacji, innej kolejności albo innym modelu. Nikt nie sprawdził też poprawności prawnej pakietu. Arbiter liczył tylko głosy i drogi według reguł z [etapu 2](../etap-2/arbiter.md).

## Pliki

- [zapis.md](zapis.md): zapis rozmowy. Jedyna zmiana względem oryginału: 12 półpauz w wypowiedziach modelu zamieniliśmy na łączniki, bo wymaga tego walidator repozytorium.
- `zapis.jsonl`: ten sam zapis bez zmian, z polem `usage`, kosztem i sumą SHA-256 zapytania przy każdym wywołaniu.
- `ustawienia.json`, `wynik.json`, `stan.json`, `techniczne.json`: ustawienia, wynik, stan końcowy i stałe teksty techniczne skryptu.
- `sumy.txt`: sumy SHA-256 oryginałów, także tekstów wysłanych do modelu (system postaci, system arbitra, karty). Sumy kart są takie same jak sumy kart z etapu 2 (`badania/symulacja/etap-2/`) w historii prac. Teksty systemowe skrypt składa z repozytorium (tryb `zbuduj`), więc ich nie kopiujemy. Sumy ich części (pakiet wiedzy, wariant (b), instrukcja arbitra, karty źródeł) i suma skryptu w `ustawienia.json` są takie same jak w [sumach skryptu](../../../narzedzia/symulacja/sumy.json).
