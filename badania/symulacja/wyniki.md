# Symulacja negocjacji: czy politycy grani przez AI się dogadają?

**To symulacja.** Wszystkie wypowiedzi napisał model AI (Claude Opus 5.5) grający prawdziwe osoby. Nie są to słowa tych osób i nie jest to przewidywanie, co zrobią. To był eksperyment: chcieliśmy sprawdzić, czy postacie w ogóle się dogadają i co wymyślą, a przy okazji wyłonić nowe pomysły na rozwiązanie sporu. Wytyczne są w [issue #46](https://github.com/gebawkubel/trybunal/issues/46).

Zestawienie napisał koordynator (Claude Opus 5.5) z zapisów przebiegów, 2026.11.04. Pełne rozmowy i materiały przygotowawcze są w części "Szczegóły".

## W skrócie

**Plan i założenia.**
- Modele AI zagrały osoby, od których naprawdę zależy rozwiązanie sporu o TK, przy jednym stole i w jednym wspólnym wątku. Każda postać dostała ten sam pakiet faktów ze stanem na 2026.11.04 i własną kartę z prawdziwymi wypowiedziami.
- Arbiter, osobny agent, pilnował kolejności i liczył głosy według Konstytucji. Porozumienie zapadało, gdy pakiet miał wymagane głosy w Sejmie i Senacie i zgodę osób, które muszą coś wykonać. Zgoda wszystkich nie była potrzebna.
- Postacie grały w trzech wariantach motywacji: (a) dobro państwa, (b) ugraj jak najwięcej, ale ostatecznie dobro państwa, (c) czysty interes polityczny.
- Skład, karty, reguły i skrypt przygotowały osobne agenty według jawnych wytycznych z issue #46. Każdy etap przeszedł recenzję.

**Co przeprowadziliśmy.**
- 10 rozmów: 1 przy stole z 10 postaciami i 9 przy stole z 6 postaciami (Nawrocki, Tusk, Kaczyński, Czarzasty, Święczkowski, Korwin-Piotrowska). Mniejszy stół powstał po uwadze prowadzącego, że nie trzeba zapraszać osób, których głos niczego nie rozstrzyga.
- 420 wywołań modelu: 357 wypowiedzi postaci (w tym 11 głosów poza kolejnością) i 63 wypowiedzi arbitra. Razem około 106 tys. słów.
- Około 2 godzin samej rozmowy, od 10 do 25 minut na przebieg.
- Koszt: 56,35 USD z budżetu 100 USD (od 3,81 do 14,50 USD na przebieg).
- Ucięte po limicie długości: 10 wypowiedzi w przebiegu 1. Po podniesieniu limitu w przebiegach 2-10 ucięte zostały już tylko 2 wypowiedzi.

**Wynik i wnioski.**
- Wszystkie 10 rozmów skończyło się porozumieniem i nikt nie głosował przeciw.
- Za każdym razem powtarza się ten sam zestaw kroków "na teraz", bez ustawy:
  - czworo sędziów wybranych w 2026 roku ślubuje przed Prezydentem;
  - policja wychodzi z TK, a Prezes i Wiceprezes wracają;
  - Anna Korwin-Piotrowska cofa swoje zarządzenia;
  - zaprzysiężeni zostają dopuszczeni do orzekania;
  - rząd publikuje zaległe wyroki.
- Żaden pakiet nie usuwa sędziów wybranych w 2026 roku. Sprawa Macieja Berka zwykle zostaje otwarta albo trafia do osobnej procedury.
- Rozwiązanie na dalszy czas się różni:
  - 3 razy zmiana Konstytucji, w tym raz reset ze stanem spoczynku obecnych sędziów;
  - 4 razy zwykła ustawa z wyborem sędziów większością 3/5;
  - 3 razy nic poza krokami "na teraz".
- Trzeba to czytać ostrożnie. Jednomyślność także przy "czystym interesie" może oznaczać, że model gra postacie zbyt ugodowo. Prowadzący zrezygnował z serii kontrolnej na innym modelu (K1-K3), przewidzianej w issue #46 i w planie etapu 1, bo symulacja miała być tylko eksperymentem.
- Nowe pomysły trafiły do [scenariuszy naprawy](../scenariusze-naprawy.md#scenariusze-z-symulacji-negocjacji) i do [bilansu propozycji](../bilans-propozycji.md) jako propozycja 15 (reset z zachowaniem sędziów z 2026 roku). Warianty zmiany Konstytucji bez resetu bilans opisał przy propozycji 16, a ustawę 3/5 z krokami "na teraz" zaliczył do częściowych wariantów propozycji 12 (część "Dobór scenariuszy spoza debaty").

## Ustawienia

- **Przebieg 1:** skład W1, 10 postaci ([etap 1](etap-1.md)), limit 1100 tokenów na wypowiedź, repozytorium b95bd28.
- **Przebiegi 2-10:** skład W5, 6 postaci: Nawrocki, Tusk, Kaczyński, Czarzasty, Święczkowski i Korwin-Piotrowska ([etap 4](etap-4.md)). Limit 1400 tokenów, repozytorium 20270d2.
- **Wspólne:** model `claude-opus-5-5`, wysiłek `medium`, adaptacyjne rozumowanie.
- **Warianty motywacji** ([warianty](etap-2/warianty-motywacji.md)):
  - (a) dobro państwa;
  - (b) ugraj jak najwięcej, ale ostatecznie dobro państwa;
  - (c) czysty interes polityczny.
- **Kolejność otwarcia** (przesunięcie): 0 zaczyna Nawrocki, 1 zaczyna Tusk, 2 zaczyna Kaczyński.

## Zestawienie

Skróty: "3/5" to większość trzech piątych głosów w Sejmie; "Kpt 1/26" to wniosek Prezydenta do TK w sporze o ślubowania z Sejmem. Drogi według [arbitra](etap-2/arbiter.md):
- A: zwykła ustawa;
- C: zmiana Konstytucji;
- D: porozumienie bez ustawy, czyli same czynności osób.

| Nr | Wariant | Zaczyna | Pakiet złożył | Drogi | Co poza krokami "na teraz" | Koszt USD | Ucięte |
|---|---|---|---|---|---|---|---|
| [1](przebieg-1/raport.md) | (b) | Nawrocki | Hołownia | C, D, A | Reset: obecni sędziowie w stanie spoczynku, ośmioro z 2026 roku w nowym składzie z mocy Konstytucji, 3/5, próg 2/3 w TK | 14,50 | 10 |
| [2](przebieg-2/zapis.md) | (a) | Nawrocki | Nawrocki | D, C, A | Zmiana Konstytucji bez resetu: 3/5, losowanie przy impasie, odmowa ślubowania tylko na piśmie w 30 dni, ośmioro z 2026 roku imiennie zachowuje kadencje, wznowienie postępowań na wniosek strony | 6,89 | 0 |
| [3](przebieg-3/zapis.md) | (c) | Nawrocki | Tusk | D, A | Ustawa: 3/5 i karencja, bez terminu na ślubowanie i bez przepisów o dawnych wyrokach | 5,34 | 0 |
| [4](przebieg-4/zapis.md) | (b) | Nawrocki | Święczkowski | D | Nic: ustawy nie uzgodniono, bo Prezydent odrzucił mechanizm wyjścia z impasu, a Lewica uzależniła od niego poparcie | 5,17 | 0 |
| [5](przebieg-5/zapis.md) | (a) | Tusk | Tusk | D, A | Ustawa: 3/5, karencja, ślubowanie przed Prezydentem z odmową tylko na piśmie, wznowienie na wniosek bez nieważności | 3,81 | 1 |
| [6](przebieg-6/zapis.md) | (c) | Tusk | Tusk | D | Nic: zasady wyboru sędziów zostały otwarte | 3,96 | 0 |
| [7](przebieg-7/zapis.md) | (b) | Tusk | Tusk | D, A | Ustawa 3/5; PiS uzależnia głosy od publikacji wyroków przed trzecim czytaniem | 3,98 | 0 |
| [8](przebieg-8/zapis.md) | (a) | Kaczyński | Tusk | D, C | Zmiana Konstytucji bez resetu: 3/5, losowanie po 3 miesiącach, ślubowanie w 30 dni albo spór przed TK, wyroki publikuje TK, ponowne badanie dawnych spraw z mocą na przyszłość | 4,69 | 1 |
| [9](przebieg-9/zapis.md) | (c) | Kaczyński | Tusk | D | Nic poza wzajemnymi zobowiązaniami Marszałka i Prezydenta: ślubowanie albo pisemna przeszkoda w 30 dni | 3,95 | 0 |
| [10](przebieg-10/zapis.md) | (b) | Kaczyński | Tusk, współpodpis Kaczyński | D, A | Ustawa 3/5 bez wznowień i bez zmiany kierownictwa TK; Marszałek nie przeprowadza wyborów zwykłą większością do 2027.03.31 | 4,07 | 0 |

"Ucięte" to wypowiedzi, które skrypt uciął po limicie długości. Głosowania w przebiegach 2-10 skończyły się wynikiem 6 do 0, w przebiegu 1 wynikiem 10 do 0. W przebiegu 5 ucięta została wypowiedź Tuska z treścią pakietu, a arbiter poddał pod głosowanie tekst bez uciętej części.

## Co z tego wynika

1. **Kroki "na teraz" są stabilne.** Wymianę "ślubowanie czworga przed Prezydentem za wyjście policji, powrót Prezesa i publikację wyroków" postacie uzgadniały za każdym razem, niezależnie od motywacji i kolejności. Jest to bliskie "kompromisowi pakietowemu z Prezydentem" z analiz AI w [scenariuszach naprawy](../scenariusze-naprawy.md), choć tamten zakłada w zamian zmianę zasad wyboru, której w przebiegach 4, 6 i 9 nie było.
2. **Rozwiązanie na przyszłość jest niestabilne.** Liczymy najdalej idący element pakietu (w przebiegach 1 i 2 obok zmiany Konstytucji była też ustawa). Zmiana Konstytucji pojawiła się 3 razy (1, 2, 8), zwykła ustawa 4 razy (3, 5, 7, 10), a 3 razy (4, 6, 9) nie uzgodniono niczego poza krokami "na teraz". Reset ze stanem spoczynku pojawił się tylko raz, w przebiegu 1, przy większym stole.
3. **Między wariantami widać różnicę, ale może być przypadkowa.** Przy "czystym interesie" (c) dwa z trzech przebiegów (6, 9) skończyły się samymi krokami "na teraz", a trzeci (3) wąską ustawą bez terminu na ślubowanie i bez przepisów o dawnych wyrokach. Przy "dobru państwa" (a) dwa z trzech przebiegów (2, 8) dały zmianę Konstytucji, a trzeci (5) ustawę. W wariancie (b) na stole 6 postaci jeden przebieg (4) skończył się bez ustawy, a dwa (7, 10) z ustawą. Przy 3 przebiegach na wariant, granych przez jeden model, to może być przypadek.
4. **Mniejszy stół jest tańszy, ale inny.** Przebiegi na 6 postaciach kosztowały 3,81-6,89 USD, a przebieg 1 na 10 postaciach 14,50 USD. W przebiegu 1 pomost dla sędziów z 2026 roku zaproponował Kosiniak-Kamysz, a stanowiska połączył Hołownia, których przy mniejszym stole nie ma. Tylko jeden przebieg na większym stole nie pozwala ocenić, czy to skład zmienia wynik.
5. **Te same sporne sprawy wracają w każdym przebiegu, a pakiety rozstrzygają je różnie albo zostawiają otwarte:**
   - **status Macieja Berka:** w 2 i 8 pakiet przewiduje ślubowanie Berka po przedstawieniu dokumentów albo stanowisku Prezydenta (w 2 Berek jest też wymieniony w przepisie przejściowym zmiany Konstytucji); w pozostałych przebiegach osobna procedura (dokumenty, decyzja Prezydenta) bez przesądzenia wyniku;
   - **Kpt 1/26** (wniosek Prezydenta do TK w sporze o ślubowania z Sejmem): Prezydent deklaruje cofnięcie w 1, 2, 5, 7 (częściowe), 8, 9 i 10, w 4 tylko zawężenie stanowiska, a w 3 i 6 sprawa zostaje otwarta;
   - **dawne wyroki:** wznowienie postępowań albo ponowne badanie bez nieważności w 2, 5 i 8, wprost bez wznowień w 10, w pozostałych bez przepisu albo otwarte;
   - **mechanizm na wypadek, gdy Sejm nie zbierze 3/5:** losowanie w 1, 2 i 8, gwarancja Marszałka do 2027.03.31 w 10, ustawa wprost bez trybu zapasowego w 3; w 4 i 9 spór o mechanizm zostaje otwarty (w 4 zablokował ustawę); w 5, 6 i 7 wynik arbitra go nie wymienia.

## Ograniczenia

- Wszystkie postacie i arbitra gra ten sam model. Zgoda może wynikać z jego skłonności do ugody, a nie z interesów stron. Serii kontrolnej na innym modelu nie przeprowadziliśmy.
- Na stole W5 głosy PSL, Polski 2050 i Centrum arbiter liczył tak, jak zadeklarował Tusk ([etap 4](etap-4.md)). To założenie, a nie fakt. Tam, gdzie pakiet wymagał progu, suma bez tej reguły też go spełniała. W przebiegu 10 Tusk nie zadeklarował tych klubów, więc reguła nie dała żadnego głosu.
- Powrót Wiceprezesa Sochańskiego, który nie siedzi przy stole, arbiter w części przebiegów (6, 9) wpisał jako "poza gwarancją stołu".
- Nikt nie sprawdził poprawności prawnej pakietów. Arbiter liczył tylko głosy i drogi.
- W przebiegach 2-10 Korwin-Piotrowska mówi także w imieniu pozostałych sędziów z 2026 roku. Arbiter za każdym razem zaznaczał, że ta grupa nie jest jednolita.

## Szczegóły

**Rozmowy.** Każdą można przeczytać w całości, wypowiedź po wypowiedzi:
- [przebieg 1](przebieg-1/zapis.md), z [raportem](przebieg-1/raport.md): 10 postaci, wariant (b);
- [przebieg 2](przebieg-2/zapis.md), [3](przebieg-3/zapis.md), [4](przebieg-4/zapis.md): zaczyna Nawrocki, warianty (a), (c), (b);
- [przebieg 5](przebieg-5/zapis.md), [6](przebieg-6/zapis.md), [7](przebieg-7/zapis.md): zaczyna Tusk, warianty (a), (c), (b);
- [przebieg 8](przebieg-8/zapis.md), [9](przebieg-9/zapis.md), [10](przebieg-10/zapis.md): zaczyna Kaczyński, warianty (a), (c), (b).

**Przygotowanie.** Każdy etap przygotował osobny agent AI według treści issue, a osobny recenzent go sprawdził:
1. [Etap 1](etap-1.md): kto siedzi przy stole i dlaczego, plan przebiegów.
2. Etap 2: [pakiet wiedzy](etap-2/pakiet-wiedzy.md) wspólny dla wszystkich, karty postaci: [Nawrocki](etap-2/karta-nawrocki.md), [Tusk](etap-2/karta-tusk.md), [Kaczyński](etap-2/karta-kaczynski.md), [Morawiecki](etap-2/karta-morawiecki.md), [Kosiniak-Kamysz](etap-2/karta-kosiniak-kamysz.md), [Czarzasty](etap-2/karta-czarzasty.md), [Hołownia](etap-2/karta-holownia.md), [Bosak](etap-2/karta-bosak.md), [Święczkowski](etap-2/karta-swieczkowski.md), [Korwin-Piotrowska](etap-2/karta-korwin-piotrowska.md), [warianty motywacji](etap-2/warianty-motywacji.md), [reguły arbitra](etap-2/arbiter.md), [luki w wiedzy](etap-2/luki.md).
3. Etap 3: [skrypt prowadzący rozmowę](../../narzedzia/symulacja/README.md).
4. [Etap 4](etap-4.md): mniejszy stół, porozumienie bez zgody wszystkich, dłuższe wypowiedzi.

Polecenia dla agentów, raporty recenzji i sumy kontrolne są w [historii prac](../../historia-prac.md).

## Pliki

W każdym `zapis.md` półpauzy z wypowiedzi modelu zamieniono na łączniki, bo wymaga tego walidator repozytorium. Liczba zamian w przebiegach 2-10: 0, 4, 10, 0, 15, 17, 0, 2, 0. Pliki `zapis.jsonl` są bez zmian. Oryginalne sumy wszystkich plików, także tekstów wysłanych do modelu, są w `sumy.txt` w katalogu każdego przebiegu.
