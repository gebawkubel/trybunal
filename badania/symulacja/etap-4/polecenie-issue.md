# Symulacja negocjacji: zamknięte spotkanie kluczowych graczy sporu o TK

## Pomysł

Symulujemy zamknięte spotkanie osób, od których naprawdę zależy rozwiązanie sporu o TK. Każdą osobę gra osobny agent AI. Wszyscy piszą w jednym wspólnym wątku, po jednej wypowiedzi naraz: po swojej wypowiedzi agent czeka na odpowiedź innych. Zadanie przy stole: wypracować porozumienie. Wynik "brak porozumienia" też jest dozwolony i uczciwy.

To nie jest przewidywanie, co zrobią prawdziwi ludzie. Symulacja sprawdza, które porozumienia w ogóle da się złożyć, gdy każda strona broni swojego interesu i ma realne narzędzia.

## Zasady

- **Skład stołu ustala model w ramach zadania**, nie człowiek. Najpierw analizuje, kto ma realne weto albo wpływ na wynik w każdej ścieżce (zwykła ustawa, zmiana Konstytucji, porozumienie bez ustawy). Zaprasza tylko takie osoby, bez zbędnych gości. Uzasadnienie składu publikujemy. Model może zaproponować różne składy dla różnych wariantów.
- **Prawdziwe nazwiska.** Każda wypowiedź jest podpisana np. "Karol Nawrocki (postać symulowana przez AI)". Każdy zapis zaczyna się informacją, że to symulacja, a nie słowa tych osób. Stanowiska wyjściowe postaci mają źródła z prawdziwych wypowiedzi.
- **Karty postaci.** Jest wspólny pakiet wiedzy dla wszystkich i prywatna karta, którą widzi tylko dana postać. Karta zawiera:
  - kim postać jest i jakimi narzędziami dysponuje;
  - ile ma głosów;
  - czerwone linie;
  - co zyskuje, jeśli porozumienia nie będzie;
  - przed kim odpowiada.
- **Pakiet wiedzy:** historia sporu, propozycje z debaty, siły i głosy, warunki prawne. Bez internetu, ze stanem wiedzy na stały dzień. Bez rekomendacji modeli, bilansu i scenariuszy AI, żeby nie zakotwiczać. Wynik porównamy z nimi dopiero potem.
- **Arbiter.** Osobny agent, który nie negocjuje. Pilnuje kolejności wypowiedzi i sprawdza, czy uzgodniony pakiet ma głosy (231, 276, 307, Senat) i jest zgodny z procedurą.
- **Równe modele** dla wszystkich postaci (np. Claude Opus 5.5). Seria kontrolna na innym modelu sprawdzi, czy wynik nie zależy od modelu.
- **Warianty motywacji**, np.:
  - (a) dobro państwa ponad wszystko;
  - (b) ugraj jak najwięcej dla swojego środowiska i jak najmniej strać, ale ostatecznie kieruj się dobrem państwa;
  - (c) czysty interes polityczny jako punkt odniesienia.
- **Kilka przebiegów na wariant**, bo jeden przebieg to anegdota.

## Budżet

- Limit zatwierdzony 2026.11.04: najwyżej około 100$ z kredytów API. Seria kontrolna na innym modelu przez Codex, poza tym limitem.
- **Najpierw jeden pełny przebieg**, nie skrócona próba: pełny skład, pełne karty, wariant (b), do porozumienia albo jawnego braku porozumienia. Po nim prowadzący decyduje, czy uruchamiamy kolejne, na podstawie tego, czy symulacja działa i ile realnie kosztowała.
- **Lista wszystkich planowanych przebiegów powstaje od razu**, przed pierwszym przebiegiem: wariant motywacji, skład, model, kolejność, szacowany koszt każdego. Docelowo 3 warianty po 3 przebiegi, chyba że analiza składu uzasadni inny plan.
- Szacunek kosztu robi agent, który buduje skrypt: przed próbą z założeniami (liczba postaci i wypowiedzi, kontekst, cache), po próbie z kosztem zmierzonym z `usage` w odpowiedziach API. Na tej podstawie proponuje liczbę przebiegów w limicie.
- Przekroczenie limitu wymaga nowej zgody.

## Przejrzystość

- Jedynym źródłem wytycznych jest ten issue. Agent wykonujący etap dostaje jako polecenie dosłowną treść tego issue (z komentarzami) i krótką wiadomość techniczną: gdzie jest repozytorium, gdzie zapisać wynik. Obie publikujemy razem z wynikiem, z sumami SHA-256.
- Nikt, także prowadzący projekt i koordynator, nie przekazuje agentom wytycznych poza tym issue. Uwaga albo zmiana (np. "dodaj osobę X") trafia najpierw jako publiczny komentarz tutaj, z uzasadnieniem, i dopiero wtedy obowiązuje.
- Wyniki etapów (skład, karty, plan) nie są przez nikogo poprawiane merytorycznie poza jawną recenzją. Poprawki po recenzji robi autor etapu, a raport recenzji jest publiczny.

## Etap 1: skład stołu i plan przebiegów

Wykonawca:
1. Dla każdej ścieżki rozwiązania (zwykła ustawa, ustawa przy wecie Prezydenta, zmiana Konstytucji, porozumienie polityczne bez ustawy, inne wskazane w repozytorium) wypisuje, kto ma w niej weto albo jest niezbędny, z liczbą głosów i podstawą prawną.
2. Wybiera, kto siedzi przy stole i kto reprezentuje dany obóz (z imienia i nazwiska, według repozytorium), z uzasadnieniem dla każdej osoby i dla każdej pominiętej osoby, która mogłaby wydawać się potrzebna.
3. Proponuje skład podstawowy i ewentualne składy wariantowe.
4. Przygotowuje listę wszystkich planowanych przebiegów zgodnie z sekcją "Budżet".
5. Wypisuje luki w repozytorium, które utrudnią karty postaci.

Materiał: repozytorium w wersji podanej w wiadomości technicznej, bez internetu. Wykonawca nie czyta wniosków, które mogłyby zakotwiczyć symulację: `badania/rekomendacje-modeli.md`, `badania/rekomendacje/`, `badania/bilans-propozycji.md`, `badania/odpowiedz.md`. Fakty z nazwą pliku, oceny oznaczone jako oceny. Pisze dla osoby bez wiedzy prawniczej, po polsku, zwykłym łącznikiem.

## Etap 2: pakiet wiedzy i karty postaci

Podstawa: wynik etapu 1 po recenzji (`badania/symulacja/etap-1.md`), skład podstawowy W1. Karty dla składów W2-W4 powstają dopiero, gdy prowadzący zdecyduje o tych przebiegach.

Wykonawca:
1. **Pakiet wiedzy (wspólny dla wszystkich postaci).** Wybiera pliki i fragmenty repozytorium, które postacie dostaną, i zapisuje listę z wersją repozytorium. Pakiet zawiera fakty: historię sporu, propozycje z debaty, siły i głosy, warunki prawne, potrzebne artykuły Konstytucji. Nie zawiera wniosków, które mogłyby zakotwiczyć rozmowę: rekomendacji modeli, bilansu propozycji, odpowiedzi z #38, ocen odpowiedzialności i sekcji "Scenariusze z analiz AI" w `badania/scenariusze-naprawy.md`. Uzasadnia każde wyłączenie i podaje szacowaną wielkość pakietu w tokenach.
2. **Karta postaci (prywatna, osobno dla każdej osoby z W1).** Zawiera:
   - kim postać jest, jaką pełni funkcję i jakie ma realne narzędzia, z podstawą prawną;
   - ilu głosami dysponuje i na kogo realnie może liczyć;
   - stanowisko wyjściowe: dosłowne cytaty z datą i źródłem z repozytorium;
   - interesy i czerwone linie;
   - co zyskuje, jeśli porozumienia nie będzie;
   - przed kim odpowiada (elektorat, partia, koalicja, instytucja).

   Interesy i czerwone linie, których dana osoba nie wypowiedziała publicznie, wykonawca oznacza jako wniosek i podaje, z jakich faktów go wyprowadza. Karta nie zawiera instrukcji, jak postać ma się zachować w rozmowie; robi to tylko wspólna instrukcja wariantu motywacji.
3. **Instrukcje wariantów motywacji (a), (b), (c):** wspólny tekst dla wszystkich postaci w danym wariancie, jednakowy dla każdej osoby.
4. **Instrukcja arbitra:** zasady liczenia głosów i procedury z etapu 1, kolejność wypowiedzi, warunki zakończenia (porozumienie z wymaganymi głosami albo jawny brak porozumienia), limit wypowiedzi.
5. **Luki:** czego brakuje w repozytorium dla każdej karty.

Wszystkie teksty, które postacie zobaczą, publikujemy przed pierwszym przebiegiem, z sumami SHA-256. Karty przechodzą jawną recenzję jak etap 1.

## Etap 3: skrypt rozmowy i arbitra

Podstawa: zrecenzowane materiały etapów 1 i 2 (`badania/symulacja/`). Skrypt nie zmienia ich treści; wysyła je modelowi dosłownie.

Wykonawca:
1. **Skrypt** w `narzedzia/symulacja/`, w Pythonie, z oficjalnym SDK Anthropic. Prowadzi jeden wspólny wątek według `arbiter.md`: kolejność wypowiedzi, limit wypowiedzi i długości, warunki zakończenia. Każda postać przy każdej wypowiedzi dostaje: pakiet wiedzy, instrukcję wariantu motywacji, swoją kartę (tylko swoją) i cały dotychczasowy wątek. Arbiter dostaje pakiet, `arbiter.md` i wątek; nie widzi kart.
2. **Równe warunki:** ten sam model i te same ustawienia dla wszystkich postaci i arbitra w przebiegu (domyślnie Claude Opus 5.5, jednakowy poziom wysiłku). Bez automatycznego przełączania na inny model; odmowę odpowiedzi skrypt zapisuje w zapisie przebiegu i stosuje jawną, opisaną regułę (np. pas).
3. **Oznaczenie:** każda wypowiedź w zapisie jest podpisana "Imię Nazwisko (postać symulowana przez AI)", a zapis zaczyna się informacją, że to symulacja, a nie słowa tych osób.
4. **Koszt:**
   - cache'owanie wspólnej części kontekstu;
   - twardy limit kosztu przebiegu w skrypcie (dla pierwszego przebiegu najwyżej 25$), po którym skrypt kończy przebieg i zapisuje stan;
   - koszt liczony z `usage` w odpowiedziach API według cennika sprawdzonego w dniu przebiegu.
5. **Tryb próbny bez kosztów:** przebieg na atrapie modelu (sprawdza kolejność, limity, zapis) oraz pomiar wielkości kontekstu przez liczenie tokenów w API. Na tej podstawie wykonawca podaje szacunek kosztu pierwszego przebiegu.
6. **Zapis przebiegu:** pełny wątek (Markdown i JSONL), dokładne teksty wysłane do modelu albo ich sumy SHA-256, ustawienia, `usage` i koszt każdego wywołania, wynik arbitra.
7. **Bezpieczeństwo:** klucz API tylko ze zmiennej środowiskowej przekazanej jawnie do skryptu, nigdy w kodzie, zapisie ani repozytorium.

Skrypt i szacunek przechodzą jawną recenzję. Pierwszy płatny przebieg uruchamia koordynator dopiero po PASS, w limicie z sekcji "Budżet".

## Etapy

- [x] Analiza składu stołu i wariantów (model), z recenzją - #50 ([wynik](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/etap-1.md))
- [x] Pakiet wiedzy i karty postaci ze źródłami (w tym materiał z #45), z recenzją - #52 ([pakiet](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/etap-2/pakiet-wiedzy.md), [arbiter](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/etap-2/arbiter.md))
- [x] Skrypt prowadzący rozmowę i arbitra - #53 ([skrypt](https://github.com/gebawkubel/trybunal/blob/main/narzedzia/symulacja/README.md))
- [x] Lista wszystkich planowanych przebiegów z szacunkiem kosztu - #50 (część 4 etapu 1; szacunek w tokenach do sprawdzenia przy budowie skryptu)
- [x] Jeden pełny przebieg; raport: czy działa, koszt zmierzony z `usage`, co poprawić - #54 ([raport](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/przebieg-1/raport.md))
- [ ] Decyzja prowadzącego o kolejnych przebiegach
- [ ] Pozostałe przebiegi z listy, w limicie budżetu
- [ ] Publikacja zapisów z kartami, poleceniami i sumami kontrolnymi; porównanie wyników z rekomendacjami modeli i bilansem (#38)









## Komentarze

### gebawkubel, 2026-11-04T10:47:50Z

## Recenzja etapu 1, runda 1: FAIL

Recenzowany commit: `57463fe13de56d0ba7110bb1a080520fe4d6f055` (gałąź symulacja-etap-1). Recenzent: Claude Opus 5.5, osobny kontekst, bez dostępu do przebiegu pracy autora. Blokery i uwagi podane w brzmieniu recenzenta; sekcje bez blokerów skrócił koordynator.

Co przeszło: większość faktów zgadza się z plikami repo. Zgadzają się funkcje osób, cytaty z datami, artykuły Konstytucji (98, 120-122, 125, 145, 155, 158, 191, 225, 235), sygnatury i liczby wniosków o immunitet (6+1). Przejrzystość, walidator i metadane też są w porządku. Blokery to błędy arytmetyczne w ocenach, kto jest "niezbędny", i dwa fakty podane niezgodnie z repo.

### Blokery

**B1. Inicjatywa zmiany Konstytucji: 57 posłów to za mało.**
- Miejsce: część 1, ścieżka C, wiersz "Inicjatywa".
- Cytat: "koalicja, PiS i Rozwój Plus z Konfederacją (57) też".
- Problem: próg to 92 posłów (1/5 z 460, art. 235 ust. 1). 40 + 17 = 57, a 57 < 92.
- Poprawka: usunąć "Rozwój Plus z Konfederacją (57)" z listy podmiotów, które same mogą złożyć projekt.

**B2. PSL nie jest jedynym klubem koalicji, który sam przechyla wotum nieufności.**
- Miejsce: ścieżka F, zdanie "Niezbędni"; skład, pkt 5 (Kosiniak-Kamysz).
- Cytaty: "PSL jest kluczem (jedyny klub koalicji, który sam wystarcza)" oraz "PSL jako jedyny klub koalicji sam wystarcza, by przechylić konstruktywne wotum nieufności".
- Problem, według liczb z `badania/sily-i-glosy.md`:
  - opozycja prawicowa 210 + Lewica 21 = 231, czyli dokładnie próg;
  - 221 (z Razem i niezrzeszonymi) + Polska 2050 15 = 236;
  - 221 + Centrum 15 = 236;
  - KO tym bardziej wystarcza.
  - Ta sama tabela F podaje "221", więc wniosek przeczy rachunkowi z tego samego wiersza.
- Poprawka: przeliczyć i wymienić wszystkie kluby koalicji, które same domykają 231, z założeniem (sama opozycja prawicowa albo z Razem i niezrzeszonymi). Zmienić opis roli PSL w ścieżce F i w uzasadnieniu pkt 5.

**B3. PSL nie jest niezbędny do 307, gdy głosuje PiS.**
- Miejsce: tabela "Podsumowanie", wiersz PSL, kolumna C.
- Cytat: "niezbędny w obu wariantach".
- Problem: koalicja z PiS ma 386. Bez PSL zostaje 354, a to więcej niż 307. PSL jest niezbędny tylko w wariancie bez PiS (z 313 można stracić 6).
- Poprawka: "niezbędny bez PiS".

**B4. "Cała koalicja" nie jest niezbędna w ścieżce B ani w regułach arbitra.**
- Miejsca:
  - ścieżka B: "Niezbędni w ścieżce B: koalicja w całości i Rozwój Plus (Mateusz Morawiecki) albo PiS";
  - tabela podsumowania, kolumna B: "niezbędny" przy PSL, Lewicy, Polsce 2050 i Centrum;
  - reguła arbitra: "231 wymaga całej koalicji; 276 wymaga koalicji i Rozwoju Plus albo PiS".
- Problem: według własnej definicji autora ("bez kogo próg głosów nie wychodzi") to nieprawda:
  - koalicja z PiS ma 386 przy progu 276, więc żaden z mniejszych klubów koalicji nie jest wtedy niezbędny;
  - z Rozwojem Plus (279) brak Polski 2050 albo Centrum (264) wyrównuje Konfederacja: 264 + 17 = 281;
  - brak PSL: 247 + 17 + 4 + 13 = 281;
  - w regule arbitra (liczą się kluby obecne przy stole) brak dowolnego małego klubu koalicji przy 231 wyrównuje Rozwój Plus albo PiS (np. 207 + 40 = 247).
  - Reguły arbitra trafią do skryptu, więc błąd przeniesie się do przebiegów.
- Poprawka: albo zapisać jawnie założenie, przy którym to prawda (np. "gdy PiS, Rozwój Plus i Konfederacja głosują przeciw", "w wariancie z Rozwojem Plus, zapas 3"), albo poprawić wnioski i reguły arbitra. To samo zastrzeżenie dopisać do kolumny A tabeli: przy samej koalicji brak Polski 2050 albo Centrum (224) wyrównują Razem i niezrzeszeni (224 + 4 + 7 = 235). Tekst ścieżki A ma to zastrzeżenie ("koalicja sama"), tabela już nie.

**B5. Kto głosował za uchwałami i wyborem sędziów (ścieżka E).**
- Cytat: "uchwały z 2024.03.06 i 2026.03.13 oraz wybory ośmiorga sędziów przeszły głosami KO, PSL, Centrum, Polski 2050 i Lewicy, przy wstrzymaniu się Razem (`zrodla/glosowania-tk-2015-2026.md`)".
- Problem, według przywołanej karty:
  - 2024.03.06: głosowały KO, PSL-TD, Polska2050-TD i Lewica; klubu Centrum wtedy nie ma;
  - 2026.03.13, uchwała (G1): Razem było nieobecne, nie wstrzymało się;
  - 2026.09.04, Berek (G4): Razem 3 "przeciw wszystkim", 1 nieobecny.
  - Wstrzymanie się Razem dotyczy tylko G2 (2026.03.13, sześć wyborów) i G3 (2026.06.11).
- Poprawka: rozpisać głosowania zgodnie z kartą.

**B6. Kto nie był na konsultacjach u Prezydenta 2026.10.31 (W2).**
- Miejsce: część 3, W2.
- Cytat: "Odwzorowuje konsultacje z 2026.10.31, w których nie uczestniczyły KO i Lewica".
- Problem: `badania/scenariusze-naprawy.md` podaje, że "Lewica i klub Centrum w nich nie uczestniczyły". O KO mówi tylko, że według TVP Info przed spotkaniem "nie zamierzała wysłać przedstawicieli" [media x1]. Wypadł brak Centrum, ważny dla reguły arbitra, a nieobecność KO podano jako pewną.
- Poprawka: przepisać zgodnie z repo.

### Zgodność z issue

Punkty 1-5 etapu 1 są wykonane. Plan zgadza się z sekcją "Budżet": pierwszy pełny przebieg wariantu (b) w W1, potem decyzja prowadzącego; lista wszystkich przebiegów od razu; docelowo 3 warianty po 3; W2-W4 warunkowo; seria kontrolna poza limitem; szacunek z założeniami. Rachunek tokenów się zgadza. W tekście nie ma treści dostępnych tylko w zakazanych plikach.

### Logika składu

Kryterium stosowane jest w zasadzie konsekwentnie: pominięcie Centrum wynika z braku nazwiska i stanowiska w repo, pominięcie Razem z arytmetyki. Reguła "Centrum głosuje z koalicją" ma oparcie w G1-G4. Sama reguła liczenia (kluby nieobecne przy stole są niedostępne) to propozycja autora i tak jest opisana; jej skutki liczbowe trzeba poprawić (B4).

### Przejrzystość, kontrole, metadane

Sumy SHA-256 zgodne; `etap-1.md` i `etap-1-polecenie-issue.md` bajt w bajt identyczne z oryginałami, `etap-1-wiadomosc.md` różni się tylko ujawnioną zamianą ścieżki. Treść issue #46 zgadza się z migawką. Wpis o PR #47 prawdziwy. Walidator, typografia, autor i committer w porządku.

### Uwagi nieblokujące

1. Koszt: przy 10-15$ za przebieg 9 przebiegów W1 to 90-135$. Zdanie "mieści się w 100$ ... przy niższym cenniku" jest prawdziwe tylko dla dolnej granicy. Warto to napisać wprost.
2. W2: wariant wotum "Polska 2050 z Centrum" kłóci się z regułą arbitra (Centrum liczy się z koalicją, a KO i Lewica głosują przeciw). Trzeba ustalić, jak arbiter liczy Centrum w W2.
3. Ścieżka G i W3 (dobrowolne odejścia, Trybunał Stanu, Kpt 1/26 i ETPC jako rozjemca) pochodzą z sekcji "Scenariusze z analiz AI" w `badania/scenariusze-naprawy.md`. Etap 1 mógł ją czytać, ale issue wyklucza "scenariusze AI" z pakietu wiedzy, więc etap 2 musi je pominąć.
4. Żurek jest pominięty jako członek rządu, choć autor zastrzega, że prokuratura działa formalnie niezależnie. Warto rozważyć, czy jego narzędzia (immunitety, śledztwa) można wiarygodnie powierzyć karcie Tuska.
5. Szczucki jako "współautor projektu": karta `rozwoj-plus-trybunal-2026.md` podaje, że projekt przedstawili Morawiecki, Szczucki i Jabłoński, a "Nazwisk autorów w odczytanym tekście nie znaleźliśmy". Lepiej "współprezentujący".
6. Luka 3: `badania/skutki-dla-obywateli.md` podaje liczbę 85 nieopublikowanych wyroków z lat 2024-2026 (22/41/22). Lista istnieje poza repo, brakuje tylko jej treści.
7. `historia-prac.md`: sumy dotyczą oryginałów, w nawiasach są ścieżki w repo z innymi sumami; dopisać "oryginał". Przy c274b85 dać stały link (AGENTS.md).
8. Senat: 99 miejsc, ale jedno jest puste (`warunki-rozwiazan.md`). Nie zmienia wniosku.


### gebawkubel, 2026-11-04T10:56:55Z

## Recenzja etapu 1, runda 2: FAIL

Recenzowany commit: `0624cb0b65dc956403ec0861cabfc6f2d21bb968` (wersja 2). Recenzent: Claude Opus 5.5, ten sam co w rundzie 1. Blokery i uwagi podane w brzmieniu recenzenta; sekcje bez blokerów skrócił koordynator.

**Stan blokerów z rundy 1:** B1-B6 usunięte. Sprawdzone liczby (m.in. 92, 93, 366, 242, 231, 225, 253, 236, 354, 365, 157, 304, 264, 296, 281, 275, 286, 235, 229, 218, 240) się zgadzają. Ścieżka E i W2 zgodne z kartą głosowań i ze scenariuszami.

### Nowe blokery

**R2-B1. Ścieżka C: brakujące głosy to 11 z 17, nie 7 z 17.**
- Miejsce: ścieżka C, zdanie "Niezbędni w ścieżce C"; tabela podsumowania, wiersz "Razem, Korona, Demokracja Bezpośrednia, niezrzeszeni (17)", kolumna C.
- Cytaty: "co najmniej 7 z 17 głosów Razem, Korony, Demokracji Bezpośredniej i niezrzeszonych" oraz "co najmniej 7 z nich bez PiS".
- Problem: koalicja, Rozwój Plus i Konfederacja to 296, więc do 307 brakuje 11 z tych 17 głosów (296 + 7 = 303). Liczba 7 z `badania/sily-i-glosy.md` dotyczy 13 posłów (niezrzeszeni, Korona, Demokracja Bezpośrednia) i to już po doliczeniu Razem (300 + 7 = 307).
- Poprawka: "co najmniej 11 z 17" albo "Razem i co najmniej 7 z 13".

**R2-B2. Reguły W2: Kukiz policzony podwójnie, błędne 232.**
- Miejsce: część 3, W2, zasady arbitra.
- Cytat: "231 w W2 wychodzi z opozycji prawicowej bez Korony (207) plus PSL (239) albo plus Polska 2050, Razem i Kukiz (207 + 15 + 4 + 3 = 229, za mało; z Koroną 232, ale Korona jest nieobecna)".
- Problem: 207 to opozycja prawicowa bez Korony, a więc już z Demokracją Bezpośrednią (3, w tym Kukiz); dodanie "Kukiz 3" liczy te głosy drugi raz. Poprawnie: 207 + 15 + 4 = 226; z Koroną 210 + 15 + 4 = 229, czyli także za mało. Zapis "z Koroną 232" sugeruje, że z Koroną wotum by przeszło, a nie przejdzie. Ta reguła trafi do skryptu arbitra.
- Poprawka: 226, a z Koroną 229, za mało w obu przypadkach. Wniosek "W2 testuje, czy PSL przejdzie na drugą stronę" pozostaje prawdziwy.

**R2-B3. Ścieżka F: "opozycja prawicowa w komplecie" nie jest niezbędna.**
- Miejsce: ścieżka F, zdanie "Niezbędni".
- Cytat: "w wotum nieufności opozycja prawicowa w komplecie (bez PiS albo bez Rozwoju Plus nie ma 231 nawet z PSL: 170 albo 63 plus 32)".
- Problem:
  - bez Korony i Demokracji Bezpośredniej (6): 204 + PSL 32 = 236, więc te koła nie są niezbędne przy PSL;
  - bez Konfederacji: 193 + 32 = 225 przy samym PSL, ale z Razem i niezrzeszonymi 236, więc Konfederacja jest niezbędna tylko przy założeniu "sam PSL";
  - "w komplecie" prawdziwe jest tylko wtedy, gdy przechodzi sama Lewica (210 + 21 = 231 dokładnie);
  - liczby w nawiasie podano w odwrotnej kolejności niż w zdaniu: bez PiS jest 63, bez Rozwoju Plus 170.
- Poprawka: niezbędne zawsze PiS i Rozwój Plus; Konfederacja przy samym PSL albo Lewicy bez Razem i niezrzeszonych; Korona i Demokracja Bezpośrednia tylko w wariancie z Lewicą; kolejność liczb w nawiasie poprawić.

**Przejrzystość i kontrole:** sumy SHA-256 zgodne, tekst pod linią identyczny z oryginałem v2, wpis w historii prac prawdziwy, sekcja "Zmiany po recenzji" obejmuje B1-B6 i uwagi 1-8 (decyzje "zostawione" przy 4 i 7 uzasadnione), walidator, typografia i tożsamość w porządku.

### Uwagi nieblokujące

1. W ścieżce F i w tabeli (KO: "sam domyka 231", pkt 5 "obok KO i Lewicy") KO jest liczona jako klub, który może domknąć wotum nieufności wobec własnego premiera. Arytmetycznie to prawda, ale politycznie nie ma sensu. Lepiej KO pominąć albo dopisać, że to tylko rachunek.
2. Pkt 2 (Tusk): "bez którego nie ma 231" jest prawdziwe tylko przy założeniu, że za głosuje sama koalicja (bez KO wszyscy pozostali mają 304). Warto dopisać to założenie, jak w tabeli.
3. E, G1: wśród głosujących przeciw (197) brakuje 2 niezrzeszonych (176 + 14 + 2 + 3 = 195). W G4 suma 184 obejmuje 1 niezrzeszonego. Drobiazg.
4. W `historia-prac.md` przy commicie c274b85 (PR #47) nadal nie ma stałego linku. To plik koordynatora.


### gebawkubel, 2026-11-04T11:01:18Z

## Recenzja etapu 1, runda 3: FAIL

Recenzowany commit: `066697b41ca049505c591c6838b2a46a9ebe1268` (wersja 3). Recenzent: Claude Opus 5.5, ten sam co w rundach 1-2. Bloker w brzmieniu recenzenta; sekcje bez blokerów skrócił koordynator.

**Stan blokerów z rundy 2:**
- R2-B1 usunięty: 296, do 307 brakuje 11 z 17.
- R2-B2 usunięty: 207, 239, 226, a z Koroną 229.
- R2-B3 częściowo: liczby 63, 170, 95, 202, 225, 214, 236 i 231 się zgadzają, ale zostało jedno zdanie (R3-B1).

Pozostałe zmiany są bez błędów: 83, 366, G1 197, G4 184. Sumy, nagłówki, linki do wersji 1-2 i do c274b85, walidator, typografia i tożsamość są w porządku.

### R3-B1. Przy Lewicy Konfederacja jest niezbędna zawsze, także z Razem i niezrzeszonymi

- Miejsce: ścieżka F, akapit "Niezbędni w wotum nieufności" (i odpowiednik w sekcji "Zmiany po recenzji (runda 2)").
- Cytat: "Konfederacja jest niezbędna tylko wtedy, gdy przechodzi sam PSL albo sama Lewica bez Razem i niezrzeszonych".
- Problem: zdanie sugeruje, że Lewica z Razem i niezrzeszonymi poradzi sobie bez Konfederacji. Tymczasem bez Konfederacji jest 193 + 21 + 11 = 225, czyli mniej niż 231. Konfederacja jest niezbędna przy samej Lewicy zawsze, a przy samym PSL tylko bez Razem i niezrzeszonych. Takie samo nieprecyzyjne sformułowanie było w propozycji poprawki recenzenta z rundy 2; autor je przejął.
- Poprawka: "Konfederacja jest niezbędna zawsze, gdy z koalicji przechodzi sama Lewica (bez niej najwyżej 193 + 21 + 11 = 225), a przy samym PSL tylko bez Razem i niezrzeszonych (225; z nimi 236)".

**Uwaga nieblokująca:** w "Zmianach po recenzji (runda 2)" uwaga 4 ma status "zostawione, poza zakresem"; koordynator wykonał ją w historia-prac.md. Status jest prawdziwy dla dokumentu autora i może zostać.


### gebawkubel, 2026-11-04T11:03:14Z

## Recenzja etapu 1, runda 4: PASS

Recenzowany commit: `99f86f9a7946152d11876d9c2d58826b033a2236` (wersja 4). Recenzent: Claude Opus 5.5, ten sam co w rundach 1-3.

R3-B1 usunięty w ścieżce F i w sekcji zmian (214; 225; 225 i 236). Nowych błędów brak. Nagłówek, sumy (v4 d72d7bde..., wiadomość 7b5375e3...), linki do wersji 1-3 i do raportów, historia prac, walidator, typografia i tożsamość w porządku. Blokerów i uwag brak.

### gebawkubel, 2026-11-04T11:49:09Z

## Recenzja etapu 2, runda 1: FAIL

Recenzowany commit: `bd2643ca06f88f370280b4e3bb57a4fa4dedde9e` (PR #52). Recenzent: Claude Opus 5.5, osobny kontekst. Blokery i uwagi w brzmieniu recenzenta; część "co przeszło" skrócił koordynator.

**Co przeszło.** Pełne sprawdzenie kart Nawrockiego, Tuska, Kaczyńskiego, Święczkowskiego i Korwin-Piotrowskiej; w pozostałych cytaty i liczby. Cytaty w częściach 3 dosłowne, z właściwą datą i plikiem (sprawdzone skryptem). Przepisy Konstytucji przywołane poprawnie. Liczby głosów zgodne z `badania/sily-i-glosy.md` i etapem 1. Warianty motywacji jednakowe i zgodne z issue. Arbiter wiernie przenosi reguły etapu 1; limit 130 wypowiedzi wynika z rachunku. Zakresy linii pakietu i wycięta sekcja "Scenariusze z analiz AI" się zgadzają. Pliki bajt w bajt zgodne z oryginałami, sumy, walidator, typografia i tożsamość w porządku. Autor pracował na 70b735a; `git diff 70b735a 18d7752` zmienia tylko `historia-prac.md`.

### Blokery

**B1. Szacunek tokenów pakietu jest zaniżony mniej więcej o połowę.**
- Miejsce: `pakiet-wiedzy.md`, części 2 i 3; `luki.md`, "Luki metodyczne", pkt 1.
- Cytaty: "**około 60-70 tys. tokenów** (przyjmuję 65 tys.)" oraz "**około 31-37 tys. tokenów**".
- Problem: pakiet podstawowy sklejony według podanych zakresów linii, policzony endpointem `count_tokens` API dla `claude-opus-5-5`, ma 118 529 tokenów przy 27 372 słowach; pakiet minimalny 64 845 tokenów przy 14 143 słowach. To około 4,3-4,6 tokena na słowo, a nie 2,2-2,6. Karta Nawrockiego ma 7668 tokenów (etap 1 zakładał 1,5 tys. na kartę).
- Skutek: zaniżony szacunek przenosi się na koszt i liczbę przebiegów w limicie 100$, a także na limit wypowiedzi w `arbiter.md` ("do około 250 słów (skrypt ustawia około 400 tokenów)"): 250 słów to około 1000 tokenów, więc limit 400 tokenów uciąłby wypowiedź po około 100 słowach.
- Poprawka: podać szacunek zmierzony albo przeliczony na nowo, z metodą; poprawić pkt 1 w `luki.md`; uzgodnić limit słów z limitem tokenów, także w części wspólnej `warianty-motywacji.md` (pkt 6).

**B2. Niespójna granica między faktem a oceną w pakiecie.**
- Miejsce: `pakiet-wiedzy.md`, zasada 1, wiersze 4 i 6 tabeli, tabela wyłączeń.
- Cytaty: "Pakiet zawiera wyłącznie fakty..."; z `historia-sporu.md` wypadają zdania "Według naszej analizy" z uzasadnieniem "to oceny odpowiedzialności", a `zgromadzenie-2026-11-03.md` (1-80) zostaje, bo "analiza A" i "analiza B" to "analizy prawne jednego zdarzenia".
- Problem: trzy z siedmiu wyciętych zdań (2025.07.29, 2026.05.12, 2026.11.03) nie oceniają odpowiedzialności. Zdanie z 2026.11.03 ("Według naszej analizy przepisy dają tym krokom słabą podstawę") zostaje w pakiecie w pełniejszej formie: `zgromadzenie-2026-11-03.md`, linia 38 ("**Ocena obu analiz:** przerwa w czynnościach Prezesa ma słabą podstawę"), "Wnioski" 1-3, karty Święczkowskiego i Korwin-Piotrowskiej. To ocena prawna działań jednej strony, z analiz dwóch modeli, którą widzą wszystkie postacie. W pakiecie zostają też inne oznaczone wnioski projektu ("Nasz wniosek" w `skutki-dla-obywateli.md`, `wyroki-europejskie.md`, `bosak-2026-11-04.md`; "Nasza analiza" w `warunki-rozwiazan.md`). Zasada 1 jest więc nieprawdziwa, a uzasadnienie cięć nie pasuje do części z nich.
- Poprawka: przyjąć i zapisać jedną regułę. Albo oznaczone oceny projektu i modeli zostają wszędzie (z uzasadnieniem i poprawioną zasadą 1), albo wypadają wszędzie, w tym "Ocena obu analiz", "Wnioski" w `zgromadzenie-2026-11-03.md` i odpowiednie zdania w kartach. Cięcia w `historia-sporu.md` uzasadnić zgodnie z tą regułą.

**B3. Karta Kaczyńskiego: błąd prawny i dwa błędy liczbowe.**
- (a) Część 4: "Wybory przed 2027 rokiem wymagają 307 (skrócenie kadencji) albo 231 z klubem koalicji (wotum)". Konstruktywne wotum nieufności (art. 158) zmienia premiera, a nie skraca kadencji Sejmu. Wybory przed terminem dają tylko art. 98 ust. 3 (307) oraz art. 155 ust. 2 i art. 225, które uruchamia Prezydent.
- (b) Część 1, tabela, i część 4: "bez PiS 307 wymaga 313 pozostałych". Poprawnie: bez PiS trzeba 307 z 313 pozostałych (można stracić najwyżej 6).
- (c) Część 5: "Prezes TK jest objęty 7 wnioskami o immunitet". Według `badania/postepowania-wobec-osob.md` (wiersze 43 i 49) z 2026 roku jest 6 wniosków wobec Święczkowskiego i 1 wobec Sochańskiego; wniosek z 2025.09.30 odrzucono, a jego sprawę obejmuje ponowiony wniosek w sprawie Pegasusa. Ta sama niejasność w `karta-swieczkowski.md`, część 5.
- Poprawka: (a) oddzielić wotum (zmiana rządu) od dróg do wcześniejszych wyborów; (b) "307 z 313"; (c) "6 wniosków z 2026 roku (w tym ponowiony w sprawie Pegasusa), siódmy dotyczy Sochańskiego", tak samo w karcie Święczkowskiego.

**B4. Karta Kosiniaka-Kamysza przypisuje mu słowa odtworzone z adresu URL.**
- Miejsce: `karta-kosiniak-kamysz.md`, części 2, 4 i 5.
- Cytaty: "Polsat News zatytułował relację 'Kosiniak-Kamysz ma pomysł na TK, wtórują mu inni, alternatywa to chaos'"; "'alternatywa to chaos' (tytuł Polsatu z Twoich słów)"; "według Twoich słów 'chaos'".
- Problem: repo nie zawiera tego tytułu ani takiej wypowiedzi, jest tylko adres URL w `badania/scenariusze-naprawy.md`, linia 66. "Z Twoich słów" to domysł podany jako czerwona linia wypowiedziana publicznie. Podobnie "To ostatni moment" pochodzi tylko z adresu artykułu WP (`badania/propozycje-na-stole.md`, linia 17).
- Poprawka: usunąć "alternatywa to chaos" z części 4 i 5; jeśli tytuł zostaje w części 2, oznaczyć go jako odczytany z adresu URL, bez przypisania słów postaci. To samo zastrzeżenie przy "To ostatni moment".

**B5. Nierówne traktowanie: tylko Bosak dostaje listę swoich błędów.**
- Miejsce: `karta-bosak.md`, część 3, ostatni punkt.
- Cytat: "Gdzie według repozytorium się mylisz (żeby postać o tym wiedziała): rząd Tuska ogłosił 9 wyroków TK do 2024.03.04, więc 'ani jednego' jest nieprawdą...".
- Problem: repo sprawdza tak samo wypowiedzi innych stron (`badania/komisja-2026-04-28.md`), ale tylko karta Bosaka ma taki punkt. Przykłady: Bogucki w imieniu Prezydenta (nr 7, "nie są publikowane żadne orzeczenia", "Częściowo"; nr 3, "trzydziestodniowy termin", "Częściowo"), PiS (nr 28, odszkodowanie w Xero Flor, "Częściowo"), Jaskulski z KO (nr 38, Trybunał Stanu, "Błędne"). Karty Nawrockiego, Kaczyńskiego i Tuska tych korekt nie mają. Dopisek "(żeby postać o tym wiedziała)" jest bliski wskazówce dla postaci.
- Poprawka: jedna zasada dla wszystkich kart: albo każda karta podaje korekty repo do wypowiedzi swojego obozu (u Nawrockiego nr 3 i 7, u Kaczyńskiego nr 28, u Tuska nr 38), albo żadna, a korekty zna tylko arbiter z pakietu. Usunąć dopisek w nawiasie.

### Uwagi nieblokujące

1. Cudzysłów przy parafrazach w częściach 4-7 kart i w `luki.md` (np. Bosak "dokonały autodyskwalifikacji" wobec "dokonał autyskwalifikacji", "TK jest ciałem politycznym"; Czarzasty "autodyskwalifikacja"; Korwin-Piotrowska "sędzią z Opola"; Morawiecki "dwóch byłych premierach"; Święczkowski "oczekujesz na stanowisko pana prezydenta", "człowiek Ziobry"; Nawrocki "twarda odpowiedź", "delikcie konstytucyjnym"; `luki.md` "niemożliwy bez 2/3", "Centrum głosuje z KO"). Cudzysłów tylko przy tekście dosłownym.
2. Data końca kadencji Wyrembaka (2027.01.30) przypisana `badania/wyroki-europejskie.md`, gdzie jest tylko "stycznia 2027"; dokładna data jest w repo tylko w wyłączonej sekcji "Scenariusze z analiz AI". Lepiej wyprowadzić ją z `badania/kierownictwo-2016.md` (kadencja od 2018.01.30) i art. 194 ust. 1, jako wyliczenie.
3. Cytat Żurka w karcie Tuska pochodzi z `zrodla/okres-2024-2026/spc-149-2026-04-28.md` (linia 456), nie z `badania/komisja-2026-04-28.md`.
4. `arbiter.md`: "przy 99 obsadzonych miejscach" - obsadzonych jest 98; próg 50 bez zmian.
5. `arbiter.md`, pkt 4.4: brakuje skutku reguły o klubach nieobecnych dla wotum nieufności (przy stole opozycja ma 204, bez Korony i Demokracji Bezpośredniej; z PSL 236, z Lewicą tylko 225, a w rzeczywistości dokładnie 231, jak piszą karty Czarzastego i Tuska).
6. Reguły arbitra ("poza gwarancją stołu") zna tylko karta Tuska; jeśli postacie mają je znać, to wszystkie jednakowo, w części wspólnej.
7. Karta Kosiniaka-Kamysza przecenia pozycję PSL ("Twoje 32 głosy decydują ... czy opozycja ma 231", "rozstrzygające w obie strony"): Lewica też sama domyka 231, a Polska 2050 albo Centrum z Razem i niezrzeszonymi.
8. Karta Nawrockiego: "Art. 225 daje Ci dźwignię ... (ocena wykonawcy etapu 1, powtórzona tu jako fakt o przepisie...)" to ocena; oznaczyć jako wniosek. Karty kilka razy przywołują oceny etapu 1, choć pakiet wyłącza etap 1.
9. W karcie Morawieckiego nie ma żadnego jego dosłownego cytatu; dopisać to w `luki.md` obok Kaczyńskiego i Hołowni.
10. "M.P. 2026 poz. 302" w karcie Korwin-Piotrowskiej: repo podaje tylko zakres 300-305 bez przypisania nazwisk.
11. Arbiter, droga A: "deklaracja Święczkowskiego, jak TK orzeknie" każe sędziemu zapowiedzieć wyrok; przeformułować na czynności Prezesa (skład, termin).
12. Arbiter, warunek (c): "postaci, której ... głosy są wymagane" niejasne; lepiej "bez której głosów suma spada poniżej progu".
13. Drobne zakresy: art. 135 (730-733) obejmuje nagłówek art. 136; "Pełne tabele (43-306)", a plik ma 305 linii.
14. `polecenie-issue.md` to poprawna migawka z chwili zlecenia (później zaznaczono w issue dwa pola). Nie jest to błąd.


### gebawkubel, 2026-11-04T11:59:41Z

## Recenzja etapu 2, runda 2: FAIL

Recenzowany commit: `62f5e272ab4a9224af1e6bd540e77fcbdc01124a` (wersja 2). Recenzent: Claude Opus 5.5, ten sam co w rundzie 1. Bloker i uwagi w brzmieniu recenzenta; część o stanie blokerów skrócił koordynator.

**Stan blokerów z rundy 1:** B1-B5 usunięte.
- B1: pomiar 118 529 i 64 845 tokenów z metodą; limit 250 słów i 1100 tokenów spójny w arbiter.md i warianty-motywacji.md; pomiar kontrolny v2 (karta Hołowni 2989 tokenów, arbiter 7714, warianty 2653).
- B2: jedna reguła o ocenach, stosowana wszędzie; wycięte tylko zdania przypisujące winę.
- B3: wotum oddzielone od dróg do wyborów, "307 z 313", 6 wniosków plus siódmy wobec Sochańskiego.
- B4: "alternatywa to chaos" usunięte, "To ostatni moment" oznaczone jako słowa z adresu.
- B5: wszystkie karty mają korekty repo do wypowiedzi swojego obozu według jednej zasady. Recenzent koryguje własny raport: nr 28 wygłosił Żurek wobec PiS, więc trafnie trafił do karty Tuska.

Uwagi z rundy 1 poprawione poza uwagą 1 (niżej). Pliki bajt w bajt zgodne z oryginałami, sumy, nagłówki, historia prac, walidator, typografia, tożsamość w porządku.

### Nowy bloker

**R2-B1. Arbiter: zdanie "231 wychodzi tylko z PSL albo z KO" jest nieprawdziwe.**
- Miejsce: `arbiter.md`, część 4, pkt 4 (zdanie dopisane w v2).
- Cytat: "opozycja obecna przy stole (PiS, Rozwój Plus, Konfederacja) ma 204, więc 231 wychodzi tylko z PSL (236) albo z KO; z Lewicą jest 225, za mało".
- Problem: przy stole wotum ma też Lewica razem z Polską 2050: 204 + 21 + 15 = 240. Centrum liczy się jak KO, więc nie wchodzi do tego rachunku. Słowo "tylko" w instrukcji, która trafi do skryptu arbitra, może sprawić, że arbiter odrzuci prawidłowy rachunek.
- Poprawka: np. "z jednego klubu koalicji 231 dają tylko PSL (236) albo KO; sama Lewica daje 225, za mało; Lewica z Polską 2050 daje 240".

### Uwagi nieblokujące

1. Uwaga 1 z rundy 1 (cudzysłów przy parafrazach) poprawiona tylko częściowo, choć `luki.md` podaje "poprawione". Nadal niedosłowne: Bosak "żeby uniknąć obstrukcji prezydenta" (źródło: "żeby uniknąć ewentualnej obstrukcji ze strony prezydenta"), "nie wykluczamy, że złamał prawo", "TK jest ciałem politycznym" (dosłowne tylko "jest ciałem politycznym"); Korwin-Piotrowska "nie pełni obowiązków Prezesa", "osobie nieuprawnionej"; Nawrocki "przedstawicieli premiera", "rezygnacją z objęcia urzędu". Nowe w v2: Kaczyński "dwóch sprzecznych wobec siebie śledztwach" (źródło: "dwa sprzeczne wobec siebie śledztwa"), "skręcanych"; Tusk i Święczkowski "najbliższym człowieku ministra Ziobry" (źródło: "najbliższym człowiekiem").
2. Karta Tuska, korekta do nr 28: "ETPC odszkodowania nie przyznał" wychodzi poza repo; lepiej "repozytorium zna tylko zasądzone 3418 EUR kosztów".
3. Karta Nawrockiego, punkt korekt: "nie rozkładaniem kadencji" niejasne i bez źródła; usunąć.
4. Karta Kaczyńskiego, część 4: "231 bez PSL albo Lewicy" pomija drogę z Polską 2050 albo Centrum przy wsparciu Razem i niezrzeszonych.
5. Cięcie w `historia-sporu.md`, punkt 2015.12.03: po "Według naszej analizy..." stoi zdanie "To był pierwszy błąd, ale sam w sobie dotyczył tylko 2 z 15 miejsc."; liczba 2130 słów wskazuje cięcie do końca punktu. Napisać to wprost w tabeli ("od zdania 'Według naszej analizy' do końca punktu").


### gebawkubel, 2026-11-04T12:03:23Z

## Recenzja etapu 2, runda 3: PASS

Recenzowany commit: `c699dd9647652af5ad219de6cad6f0998a34014a` (wersja 3, PR #52). Recenzent: Claude Opus 5.5, ten sam co w rundach 1-2.

R2-B1 usunięty: arbiter podaje teraz PSL (236), KO (360), samą Lewicę (225, za mało) i Lewicę z Polską 2050 (240); liczby przeliczone. Uwagi z rundy 2: poprawione cytaty dosłowne (sprawdzone skryptem), parafrazy bez cudzysłowu; przy Xero Flor autor miał rację (`badania/wyroki-europejskie.md`, linia 9: "Odszkodowania 18 488 EUR nie przyznał"), recenzent się mylił; uwagi 3-5 wprowadzone. Pliki bajt w bajt zgodne z oryginałami, sumy, historia prac, walidator, typografia i tożsamość w porządku. Blokerów brak.

### gebawkubel, 2026-11-04T12:05:47Z

**Uzupełnienie techniczne do etapu 3 (prośba prowadzącego, 2026.11.04):** zapis przebiegu w Markdown ma być dopisywany na bieżąco, po każdej wypowiedzi, żeby rozmowę dało się śledzić na żywo w trakcie przebiegu. Nie zmienia to treści, którą dostają postacie ani arbiter.

### gebawkubel, 2026-11-04T12:37:23Z

## Recenzja etapu 3 (skrypt), runda 1: FAIL

Recenzowany commit: `d060ba12f360c80bdb3f14748d36f82e2f3a6c05` (PR #53; commit wykonawcy `0af82c6`). Recenzent: Claude Opus 5.5, osobny kontekst; tylko `count_tokens`, bez generowania. Blokery, decyzje i uwagi w brzmieniu recenzenta; część "co przeszło" skrócił koordynator.

**Co przeszło.**
- `zbuduj` zgodny bajt w bajt z `sumy.json`.
- Pakiet z 70b735a zgodny z zakresami i cięciami z `pakiet-wiedzy.md`.
- `policz` daje identyczne liczby jak `tokeny.json`.
- Tryb próbny: typowy 114 wywołań i 14,82 USD; maks 141 i 18,21 USD; pas 23. Limit nie przekroczony w atrapie przy limitach 4-30 USD.
- Zgodność z wytycznymi etapu 3:
  - jeden wątek, tylko własna karta, arbiter bez kart postaci;
  - równe ustawienia, bez `fallbacks`, odmowa jako jawne "Pas";
  - podpisy, zapis na żywo z `fsync`;
  - klucz tylko ze zmiennej.
- Wywołania SDK (anthropic 2.4.0) poprawne dla Opus 5.5.
- Koszt liczony z `usage`. Cennik zgodny z platform.claude.com (2026.11.04): 4 / 5 / 8 / 0,20 / 20 USD za mln.
- Reguły arbitra zgodne z `arbiter.md`.
- Pliki koordynatora, walidator, typografia i tożsamość w porządku.

### Blokery

**B1. Zmienny schemat odpowiedzi arbitra unieważnia jego bufor; szacunek kosztu jest zaniżony.**
- Miejsce: `symulacja.py`, `schemat_arbitra()` i `Api.arbiter()`. `output_config.format` jest budowany przy każdym wywołaniu z bieżących list dozwolonych wartości.
- Problem: dokumentacja structured outputs mówi: "Changing the `output_config.format` parameter will invalidate any prompt cache for that conversation thread".
  - Pomiar `count_tokens` dla "Test." daje 11 tokenów bez schematu oraz 199, 347, 553 i 285 dla różnych schematów skryptu.
  - Schemat zmienia się w przebiegu kilka razy. Każda zmiana to ponowny zapis do bufora ponad 183 tys. tokenów prefiksu arbitra, czyli 1,5-2,3 USD.
  - Atrapa tego nie modeluje. Z dodaną zależnością bufora od schematu: typowy przebieg 23,54 USD zamiast 14,82, maks 29,39 zamiast 18,21. Przy wyższych założeniach typowy przebieg kończy się na limicie 25 USD, bez pełnego przebiegu.
- Poprawka:
  - jeden stały schemat dla wszystkich wywołań arbitra, z pełnymi, stałymi listami wartości;
  - to, co dozwolone w danej chwili, podawać w zdaniu tury i sprawdzać w skrypcie;
  - do atrapy dodać zależność bufora od schematu;
  - przeliczyć szacunek w README i w `historia-prac.md`.

**B2. Limit kosztu nie rezerwuje kwoty na ogłoszenie przerwania po wywołaniu arbitra.**
- Miejsce: `_sprawdz_limit()` i `arbitruj()`.
- Problem:
  - przed wywołaniem arbitra rezerwa obejmuje tylko jedno wywołanie, więc kolejne `przerwanie` nie jest nią objęte;
  - drugie podejście arbitra po błędnej odpowiedzi też nie jest sprawdzane.
- Odtworzenie: atrapa z modelem bufora z B1, scenariusz maks, limit 28 USD. Wynik 28,45 USD. Bez B1 nadwyżka jest mniejsza (około 0,2 USD), ale możliwa.
- Poprawka:
  - przed wywołaniem arbitra rezerwować dwa wywołania;
  - przed drugim podejściem wywołać `_sprawdz_limit`;
  - do atrapy dodać przypadek z kosztownym ostatnim wywołaniem arbitra.

### Decyzje wymagające zgody prowadzącego

1. **Kolejność kontekstu postaci.**
   - `pakiet-wiedzy.md`, część 6: wariant, pakiet, karta, wątek.
   - Skrypt domyślnie: wariant i pakiet w `system`, wątek, potem karta i zdanie o kolejce w wiadomości `role: system` po wątku.
   - Oszczędza około 3,3 USD na przebieg. Kolejność z etapu 2 jest dostępna opcją `--uklad etap2`.
   - Nie narusza równych warunków ani zasady "tylko swoja karta". Model może jednak traktować kartę po wątku jako polecenie operatora o wyższej wadze.
2. **Głos poza kolejnością udzielany po rundzie, nie w jej trakcie.** Limity są dotrzymane i nikt nie jest wyróżniony, ale zmienia to dynamikę wymiany zdań.

Decyzje 3 (głosowanie jedną wypowiedzią) i 4 (karty źródeł dla arbitra) są zgodne z `arbiter.md` i `pakiet-wiedzy.md` i nie wymagają zgody.

### Uwagi nieblokujące

1. Błąd w trakcie strumienia nie jest ponawiany (SDK ponawia tylko przed rozpoczęciem odpowiedzi), a trybu wznowienia nie ma. Warto dodać jedno ponowienie strumienia objęte limitem albo wznowienie z `zapis.jsonl`.
2. Pole `pakiety` z decyzji arbitra nie trafia do wątku, a tura głosowania odsyła do "ostatniej wypowiedzi" arbitra. Kazać arbitrowi wymienić pakiety w `tekst` albo wstawić listę do zdania tury.
3. `sha256_zapytania` nie obejmuje `thinking` ani `output_config`, a schemat arbitra nie jest zapisywany. Objąć sumą pełne ciało zapytania.
4. Podwójny podpis w wątku: postać podpisuje się sama, a skrypt dodaje podpis drugi raz. Kosmetyka.
5. Głos poza kolejnością wykonywany także po decyzji `glosowanie`. Dopuszczać go tylko przy `dalej`.
6. Rezerwa w limicie (1,5 razy najdroższe z 10 ostatnich wywołań) to oszacowanie, nie górna granica. README to zaznacza.
7. Po poprawce B1 zaktualizować szacunek w `historia-prac.md`.


### gebawkubel, 2026-11-04T12:47:59Z

**Rozstrzygnięcia prowadzącego do etapu 3 (2026.11.04), w odpowiedzi na "decyzje wymagające zgody" z recenzji rundy 1:**

1. **Kolejność kontekstu postaci: jak w zrecenzowanym etapie 2** (wariant, pakiet, karta, wątek; opcja `--uklad etap2` jako domyślna dla przebiegów). Powód: zgodność z tym, co przeszło recenzję, i uniknięcie wpływu położenia karty na zachowanie postaci; koszt około 3,3 USD więcej na przebieg.
2. **Głos poza kolejnością: zostaje uproszczenie skryptu** (arbiter udziela go po rundzie, wypowiedź liczy się do tej rundy, limity z arbiter.md bez zmian).

### gebawkubel, 2026-11-04T13:02:31Z

## Recenzja etapu 3 (skrypt), runda 2: PASS

Recenzowany commit: `f2b1aac9035923863ce8c5e6738e0d9579fe0dd1` (PR #53; wykonawca 39a0e8a). Recenzent: ten sam co w rundzie 1; tylko `count_tokens`.

- B1 usunięty: jeden stały schemat arbitra (664 tokeny), walidacja w skrypcie; tylko pierwsze wywołanie arbitra zapisuje prefiks.
- B2 usunięty: rezerwa na ogłoszenie przerwania przed każdym wywołaniem i ponowieniem; 112 przebiegów atrapy (limity 3-30 USD, także z drogim ogłoszeniem) bez przekroczenia limitu, najmniejszy zapas 0,27 USD.
- Rozstrzygnięcia prowadzącego wprowadzone (układ etap2 domyślny, głos poza kolejnością po rundzie).
- Ścieżka płatna bez błędów (pełna suma zapytania, jedno ponowienie strumienia sprawdzone wstrzykniętym błędem).
- Szacunek w atrapie: typowy 18,16 USD, maks 22,54 USD.
- Pliki koordynatora, sumy, walidator i tożsamość w porządku.

**Uwagi nieblokujące:**
1. Przy długich wypowiedziach i dużym rozumowaniu pierwszy przebieg może skończyć się na limicie 25 USD, zanim padnie wynik merytoryczny.
2. Po podwójnym błędzie sieci przebieg kończy się bez ogłoszenia arbitra.
3. Granica limitu nie obejmuje wygaśnięcia bufora; README to zastrzega.

### gebawkubel, 2026-11-04T15:09:46Z

**Przebieg 1 zakończony** (2026.11.04, 14:03-14:29): wariant (b), skład W1, `claude-opus-5-5`, wysiłek `medium`. Koszt z `usage`: **14,50 USD** (szacunek około 18 USD), 81 wywołań, 73 wypowiedzi postaci. Wynik według arbitra: **porozumienie**, 10 głosów "za" z zastrzeżeniami.

Do poprawienia przed kolejnymi przebiegami: 11 wypowiedzi uciętych po limicie 1100 tokenów (głosy padły przed cięciem); możliwa zbyt łatwa zgoda postaci granych przez jeden model.

Prowadzący poprosił o podsumowanie przebiegu i dopisanie wynikowego wariantu ("reset z zachowaniem sędziów z 2026 roku": stan spoczynku obecnych sędziów, ośmioro z 2026 roku wchodzi do nowego składu z mocy przepisu przejściowego z losowanymi kadencjami) do scenariuszy naprawy. Robi to koordynator w PR do tego issue, z recenzją. Decyzja o kolejnych przebiegach należy do prowadzącego.


### gebawkubel, 2026-11-04T15:14:15Z

Sprostowanie do komentarza o przebiegu 1: skrypt uciął **10** wypowiedzi, nie 11 (1 w dyskusji, 3 w pierwszym głosowaniu, 6 w powtórnym). Błąd wskazał recenzent PR #54.

### gebawkubel, 2026-11-04T15:18:41Z

## Etap 4: poprawki przed kolejnymi przebiegami (uwagi prowadzącego po przebiegu 1)

Uwagi prowadzącego, dosłownie (2026.11.04):

> co do kolejnych prob to nie wiem czy az tylu trzeba zaprasszac - po drugie czy wszyscy musza sie zgodzic? absolutnie nie - chodzi o wypracowanie jakiegos rozwiazania, ale nie do kazdego rozwiazania potrzebni sa wszyscy. ci ktorzy nie maja zadnego decydujacego glosu bo ich glos praktycznie nic nie znaczy to po co ich zapraszac.

> popraw dlugosc ale nie przesadzaj z nia

Zakres etapu 4 (wykonuje agent, nie koordynator; wynik przechodzi jawną recenzję):

1. **Skład stołu.** Ponownie ocenić skład W1 i plan przebiegów z etapu 1 w świetle uwagi prowadzącego: zapraszamy tylko osoby, których głos albo czynność realnie rozstrzyga o wyniku na ścieżce, która ma szansę. Osoby, których głos praktycznie nic nie zmienia, nie siedzą przy stole. Skład i liczbę postaci nadal ustala model z analizy, nie prowadzący. Uzasadnić, kogo i dlaczego usunąć albo zostawić, i zaktualizować listę przebiegów z szacunkiem kosztu (przebieg 1 kosztował 14,50 USD przy 10 postaciach).
2. **Zgoda wszystkich nie jest wymagana.** Porozumienie to pakiet, który ma wymagane progi i czynności. Sprawdzić, czy reguły arbitra, warianty motywacji i polecenia rundy tego nie zaciemniają (np. czy nie sugerują postaciom, że muszą się zgodzić wszyscy) i w razie potrzeby to doprecyzować.
3. **Długość wypowiedzi.** W przebiegu 1 skrypt uciął 10 wypowiedzi po limicie 1100 tokenów, głównie w głosowaniach ([raport](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/przebieg-1/raport.md)). Podnieść limit umiarkowanie, bez przesady, albo skrócić wymagany format głosu; uzgodnić liczby w skrypcie i w tekstach, które widzą modele; podać wpływ na koszt.

Karty nowych postaci, jeśli skład się zmieni, powstają według zasad etapu 2. Kolejne przebiegi uruchamia koordynator dopiero po PASS recenzji.

