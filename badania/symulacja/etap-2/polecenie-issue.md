> Treść issue #46 z komentarzami, pobrana z GitHuba w chwili zlecenia etapu 2 i przekazana wykonawcy jako polecenie. Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `5cd0d4836fdbbbb2e0cd21f90e5b8c04849923f420eaa221eb96fe6e969bdbe5`.

---

# Issue #46: Symulacja negocjacji: zamknięte spotkanie kluczowych graczy sporu o TK

Pobrano z https://github.com/gebawkubel/trybunal/issues/46 (treść i komentarze, stan na chwilę zlecenia).

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

## Etapy

- [ ] Analiza składu stołu i wariantów (model), z recenzją
- [ ] Pakiet wiedzy i karty postaci ze źródłami (w tym materiał z #45), z recenzją
- [ ] Skrypt prowadzący rozmowę i arbitra
- [ ] Lista wszystkich planowanych przebiegów z szacunkiem kosztu
- [ ] Jeden pełny przebieg; raport: czy działa, koszt zmierzony z `usage`, co poprawić
- [ ] Decyzja prowadzącego o kolejnych przebiegach
- [ ] Pozostałe przebiegi z listy, w limicie budżetu
- [ ] Publikacja zapisów z kartami, poleceniami i sumami kontrolnymi; porównanie wyników z rekomendacjami modeli i bilansem (#38)





## Komentarze

**gebawkubel, 2026-11-04T10:47:50Z:**

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


**gebawkubel, 2026-11-04T10:56:55Z:**

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


**gebawkubel, 2026-11-04T11:01:18Z:**

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


**gebawkubel, 2026-11-04T11:03:14Z:**

## Recenzja etapu 1, runda 4: PASS

Recenzowany commit: `99f86f9a7946152d11876d9c2d58826b033a2236` (wersja 4). Recenzent: Claude Opus 5.5, ten sam co w rundach 1-3.

R3-B1 usunięty w ścieżce F i w sekcji zmian (214; 225; 225 i 236). Nowych błędów brak. Nagłówek, sumy (v4 d72d7bde..., wiadomość 7b5375e3...), linki do wersji 1-3 i do raportów, historia prac, walidator, typografia i tożsamość w porządku. Blokerów i uwag brak.
