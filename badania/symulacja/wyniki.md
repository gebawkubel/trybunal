# Symulacja negocjacji: wyniki przebiegów 1-10

**To symulacja.** Wszystkie wypowiedzi napisał model AI (Claude Opus 5.5) grający prawdziwe osoby. Nie są to słowa tych osób i nie jest to przewidywanie, co zrobią. Symulacja sprawdza, jakie porozumienie da się złożyć przy założeniach z [issue #46](https://github.com/gebawkubel/trybunal/issues/46).

Zestawienie napisał koordynator (Claude Opus 5.5) z zapisów przebiegów, 2026.11.04. Każdy przebieg ma katalog `badania/symulacja/przebieg-N/` z zapisem rozmowy (`zapis.md`), surowym zapisem (`zapis.jsonl`), ustawieniami i sumami SHA-256.

## W skrócie

Wszystkie 10 przebiegów skończyło się porozumieniem i nikt nie głosował przeciw. Łączny koszt wyniósł 56,35 USD z budżetu 100 USD.

W każdym przebiegu powtarza się ten sam zestaw kroków "na teraz", bez ustawy:
- czworo sędziów wybranych w 2026 roku ślubuje przed Prezydentem;
- policja wychodzi z TK, a Prezes i Wiceprezes wracają;
- Anna Korwin-Piotrowska cofa swoje zarządzenia;
- zaprzysiężeni zostają dopuszczeni do orzekania;
- rząd publikuje zaległe wyroki.

Sędziowie wybrani w 2026 roku we wszystkich przebiegach zostają w Trybunale. Różni się to, co postacie uzgodniły na dalszy czas: od braku jakiejkolwiek ustawy po zmianę Konstytucji z resetem.

Trzeba to czytać ostrożnie. Jednomyślność we wszystkich 10 przebiegach, także przy motywacji "czysty interes polityczny", może oznaczać, że model gra postacie zbyt ugodowo. Sprawdzi to seria kontrolna na innym modelu, przewidziana w issue.

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

Drogi według [arbitra](etap-2/arbiter.md):
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

"Ucięte" to wypowiedzi, które skrypt uciął po limicie długości. Głosowanie wszystkich 10 przebiegów skończyło się wynikiem 6 do 0 (w przebiegu 1: 10 do 0).

## Co z tego wynika

1. **Kroki "na teraz" są stabilne.** Wymianę "ślubowanie czworga przed Prezydentem za wyjście policji, powrót Prezesa i publikację wyroków" postacie uzgadniały za każdym razem, niezależnie od motywacji i kolejności. W [scenariuszach naprawy](../scenariusze-naprawy.md) odpowiada to "kompromisowi pakietowemu z Prezydentem" z analiz AI.
2. **Rozwiązanie na przyszłość jest niestabilne.** Zmiana Konstytucji pojawiła się 3 razy (1, 2, 8), zwykła ustawa 4 razy (3, 5, 7, 10), a 3 razy (4, 6, 9) nie uzgodniono niczego poza krokami "na teraz". Reset ze stanem spoczynku pojawił się tylko raz, w przebiegu 1, przy większym stole.
3. **Motywacja ma widoczny wpływ.** Przy "czystym interesie" (c) dwa z trzech przebiegów (6, 9) skończyły się samymi krokami "na teraz", a trzeci (3) wąską ustawą bez terminu na ślubowanie i bez przepisów o dawnych wyrokach. Przy "dobru państwa" (a) dwa z trzech przebiegów (2, 8) dały zmianę Konstytucji, a trzeci (5) ustawę.
4. **Mniejszy stół jest tańszy, ale inny.** Przebiegi na 6 postaciach kosztowały 3,81-6,89 USD, a przebieg 1 na 10 postaciach 14,50 USD. W przebiegu 1 pomost dla sędziów z 2026 roku zaproponowali Kosiniak-Kamysz i Hołownia, których przy mniejszym stole nie ma. Tylko jeden przebieg na większym stole nie pozwala ocenić, czy to skład zmienia wynik.
5. **Sporne sprawy wracają w każdym przebiegu:**
   - status Macieja Berka;
   - sprawa Kpt 1/26;
   - dawne wyroki;
   - mechanizm na wypadek, gdy Sejm nie zbierze 3/5.

   Za każdym razem arbiter wpisał je jako otwarte albo "poza gwarancją stołu".

## Ograniczenia

- Wszystkie postacie i arbitra gra ten sam model. Zgoda może wynikać z jego skłonności do ugody, a nie z interesów stron. Seria kontrolna na innym modelu jeszcze się nie odbyła.
- Na stole W5 głosy PSL, Polski 2050 i Centrum arbiter liczył tak, jak zadeklarował Tusk ([etap 4](etap-4.md)). To założenie, a nie fakt. Arbiter podawał też sumy bez tej reguły, które za każdym razem spełniały wymagany próg.
- Nikt nie sprawdził poprawności prawnej pakietów. Arbiter liczył tylko głosy i drogi.
- W przebiegach 2-10 Korwin-Piotrowska mówi także w imieniu pozostałych sędziów z 2026 roku. Arbiter za każdym razem zaznaczał, że ta grupa nie jest jednolita.

## Pliki

W każdym `zapis.md` półpauzy z wypowiedzi modelu zamieniono na łączniki, bo wymaga tego walidator repozytorium. Liczba zamian w przebiegach 2-10: 0, 4, 10, 0, 15, 17, 0, 2, 0. Pliki `zapis.jsonl` są bez zmian. Oryginalne sumy wszystkich plików, także tekstów wysłanych do modelu, są w `sumy.txt` w katalogu każdego przebiegu.
