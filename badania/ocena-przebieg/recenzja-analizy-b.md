# Recenzja analizy B: odpowiedzialność za kryzys TK i porównanie rozwiązań

Data: 2026.11.03. Recenzent: agent Claude (model claude-fable-5-1), osobny kontekst, bez wglądu w inne analizy i recenzje w katalogu `ocena`. Podstawa: `analiza-b.md`, `polecenie.md` oraz repozytorium `publiczne`, gałąź `main` (HEAD 880af1a). Przeczytano wszystkie notatki w `badania/`, `metodologia.md` oraz karty w `zrodla/`, na które analiza się powołuje (w tym `konstytucja.md`, art. 8, 87, 98, 122, 125, 144, 145, 158, 190, 194, 196, 235). Nie zmieniano ani analizy, ani repo.

Skala wagi: **[B]** błąd merytoryczny lub twierdzenie sprzeczne z repo, **[N]** nieścisłość albo twierdzenie bez pokrycia w repo, **[S]** uwaga stylistyczna lub strukturalna.

## 1. Pokrycie faktów w repo

Zdecydowana większość faktów ma pokrycie i poprawne odesłania. Sprawdzono każdy punkt części 1 z notatkami i kartami. Poniżej twierdzenia, które są sprzeczne z repo, nieprecyzyjne albo nie mają pokrycia.

| Nr | Miejsce w analizie | Problem | Źródło w repo |
|---|---|---|---|
| 1 | Cz. 1 pkt 2, "Kto": "Prezydent odebrał ślubowanie od czterech z nich 2015.12.03, w przeddzień ogłoszenia K 34/15" | **[B]** Repo podaje, że ślubowanie czworga i wyrok K 34/15 przypadły tego samego dnia, 2015.12.03; godziny ślubowania komunikat Prezydenta nie podaje. "W przeddzień" nie ma pokrycia. Jeżeli autor miał na myśli ogłoszenie w Dzienniku Ustaw, trzeba to napisać wprost | `badania/piec-miejsc.md`, tabela (wiersze 2015.12.03) i zdanie "Godziny ślubowania z 2015.12.03 komunikat Prezydenta nie podaje" |
| 2 | Cz. 1 pkt 9, "Ocena sądów": "KM RE przyjął uchwałę z 2024 r. jako element wykonania wyroków ETPC"; w tabeli "KM za" | **[N]** Repo mówi, że to rząd przedstawił uchwałę KM jako część wykonania. KM "z zadowoleniem przyjął zmianę stanowiska władz" i odnotował prace; nie ma w repo oceny KM, że uchwała Sejmu jest środkiem wykonania. Zdanie przypisuje KM stanowisko rządu | `badania/wyroki-europejskie.md`, "2024-2026"; `zrodla/okres-2024-2026/km-xero-flor-2024-2026.md`, decyzja 2024.09 pkt 3 i DH-DD(2026)435 |
| 3 | Cz. 2 wariant 1, K1: "ustawowy wymóg ślubowania 'wobec Prezydenta' (art. 6 ust. 1)" | **[B]** Art. 6 ust. 1 ustawy o organizacji TK określa skład Zgromadzenia Ogólnego (sędziowie, którzy złożyli ślubowanie wobec Prezydenta). Sam obowiązek złożenia ślubowania wobec Prezydenta wynika z art. 4 ust. 1 ustawy o statusie sędziów TK; ten przepis badał K 3/26 i dotyczy go Kpt 1/26. Odesłanie jest pomylone | `badania/zgromadzenie-2026-11-03.md`, "Co mówią przepisy"; `zrodla/okres-2024-2026/k-3-26.md`; `zrodla/okres-2024-2026/kpt-1-26.md` |
| 4 | Cz. 1 pkt 5, "Kto": "trzy ustawy grudniowe" | **[N]** Dwie ustawy (o organizacji i trybie oraz o statusie sędziów) uchwalono 2016.11.30; tylko przepisy wprowadzające są z 2016.12.13. Poprawnie: "trzy ustawy z końca 2016 r." | `badania/okres-2016-2019.md`, pkt 6-7 |
| 5 | Cz. 1 pkt 4, "Ocena": "Komisja Europejska za niezgodne z podziałem władzy" | **[N]** KE uznała za niezgodną z praworządnością kontrolę legalności wyroku przez organ publikujący (2016/1374 pkt 19-21); zarzut naruszenia podziału władzy dotyczył oznaczania wyroków jako wydanych z naruszeniem przepisów (2017/146 pkt 17). Analiza łączy dwa zarzuty w jeden | `zrodla/okres-2016-2019/zalecenia-ke-2016.md` |
| 6 | Cz. 1 pkt 4, "Kto": "Podstawą były kolejno: stanowisko rządu, art. 19 przepisów wprowadzających i ustawa z 2018.04.12" | **[N]** Pominięto art. 89 ustawy z 2016.07.22, który był podstawą publikacji 21 wyroków 2016.08.16 i według rządu wyłączał K 47/15 | `badania/publikacja-wyrokow.md`, "Przepisy w kolejnych okresach", pkt 2 |
| 7 | Cz. 1 pkt 4, "Odpowiedzialność": "ETPC w sprawie A.R. potępił opóźnioną publikację" | **[N]** Repo: ETPC "dodał, że opóźniona publikacja wywołała niepewność prawa" (§§ 117-120). "Potępił" jest mocniejsze niż źródło | `badania/wyroki-europejskie.md`, A.R. |
| 8 | Cz. 1 pkt 3, "Ocena sądów (F)": "ETPC i TSUE nie oceniały samego niedopuszczenia, ale potwierdziły jego przesłankę" | **[N]** To wniosek autora, nie fakt z repo. Powinien być oznaczony jako **O** | `badania/okres-2016-2019.md`; `zrodla/xero-flor.md` |
| 9 | Cz. 1 pkt 10, "Ocena sądów (F)": "To odwrotność pkt 5 K 34/15" | **[N]** Porównanie dwóch wyroków jest oceną autora (trafną), ale stoi w bloku **F**. Repo zestawia oba wyroki jako argumenty stron, nie jako "odwrotność" | `badania/zgromadzenie-2026-11-03.md`, "Wnioski" pkt 5 |
| 10 | Cz. 1 pkt 8, odesłanie składu K 3/21 do `wyroki-europejskie.md` | **[S]** Skład K 3/21 (Muszyński, Piskorski, Wyrembak) jest w `okres-2020-2023-uzupelnienie.md`, tabela składów, nie w notatce o wyrokach europejskich | `badania/okres-2020-2023-uzupelnienie.md`, sekcja 1 |
| 11 | Cz. 1 pkt 6: "Żaden sąd krajowy powołania nie unieważnił" | **[N]** Repo tego nie stwierdza wprost; to wniosek z braku dokumentu. Należy zapisać jako "repo nie odnotowuje" | `badania/kierownictwo-2016.md`, "Czego nie ustalono" |
| 12 | Luki, pkt 4: "Repo nie opisuje roli Prezydenta Komorowskiego (podpis ustawy z 2015.06.25)" | **[N]** Co do podpisu prawda, ale repo odnotowuje, że projekt ustawy (druk 1590) wpłynął z pismem Prezydenta z 2013.07.10, czyli był inicjatywą prezydencką. Analiza pomija to w pkt 1 części 1 ("kto działał"), choć to element odpowiedzi | `badania/skad-art-137.md`, tabela "Co potwierdziliśmy" |
| 13 | Cz. 2 wariant 3, K5: "nie ma druku" | **[N]** Sprzeczne z K3 tej samej sekcji, gdzie analiza powołuje druk Senatu nr 55 z 2024.03.06 (projekt zmiany Konstytucji z wygaszeniem kadencji). Repo: brak druku sejmowego dla wariantów z 2026 r., ale druk senacki istnieje | `badania/scenariusze-naprawy.md`, scen. 3, tabela i "Stan"; `badania/okres-2024-2026.md`, ostatnia sekcja |
| 14 | Cz. 2 wariant F, K1: "Ma oparcie w art. 46 Konwencji i art. 260 TFUE" | **[N]** Art. 260 TFUE to podstawa działań Komisji wobec państwa (kary), nie podstawa działania Polski. Jako oparcie dla planu wykonania wyroków pasuje art. 46 Konwencji i sam wyrok TSUE | `badania/wyroki-europejskie.md`, "Po wyroku TSUE" |
| 15 | Cz. 1 pkt 4, cytat Szydło z 2016.03.08 i pkt 11, wnioski immunitetowe | **[S]** Repo oznacza te informacje jako [media x1]. Analiza przy Szydło nie zaznacza, że to jeden artykuł bez nagrania; przy immunitetach zaznacza "według mediów", co wystarcza | `badania/publikacja-wyrokow.md`; `badania/scenariusze-naprawy.md`, "Najważniejsze fakty" |

Pozostałe sprawdzone twierdzenia (głosowania 2015, 20-4-1 w komisji, 145-272 i 261 za, 232-236 głosów, daty ślubowań, 818/663/575 dni, umorzenie 2017.02.10 i podjęcie 2025.01.29, składy K 3/21, K 6/21, K 7/21, kworum i staż z 2026.11.03, treść K 3/26, Kp 3/24, U 5/24, uchwała Kolegium SN, 239 i 210 posłów, progi 307 i 276, art. 144 ust. 3 pkt 21, art. 196) mają pokrycie w repo.

## 2. Ocena sądu a wina osoby

Analiza wyraźnie deklaruje tę zasadę na początku i konsekwentnie jej przestrzega. Nigdzie nie przypisuje winy osobistej bez orzeczenia; przy premier Szydło opiera się na relacjach HFPC i oznacza je jako media, przy Rzeplińskim pisze o tropie medialnym, przy Korwin-Piotrowskiej odnotowuje brak postępowania. Zdanie "Odpowiedzialności osobistej nie poniósł nikt" jest zgodne z repo.

Dwie uwagi:

- **[N]** Wniosek części 1 ("niezgodność z prawem stwierdzona przez sąd dotyczy przede wszystkim Sejmu VIII kadencji, Prezydenta (2015) i rządu") pomija, że ten sam typ rozstrzygnięcia istnieje wobec Sejmu X kadencji: TK w U 5/24 uznał uchwałę z 2024.03.06 za niekonstytucyjną, a w K 3/26 zakwestionował wykładnię, na której opiera się obecna praktyka Sejmu. Analiza w innych miejscach traktuje K 1/17 i K 3/26 jako orzeczenia (np. "Za wariantem: K 3/26 i K 1/17"), więc powinna je uwzględnić także w podsumowaniu albo wyjaśnić, dlaczego je pomija (sporny skład TK). Bez tego wniosek jest jednostronny.
- **[S]** "W praktyce podatników" w tym samym wniosku to retoryka; repo podaje tylko 3418 EUR zapłacone i dwie niesprawdzone kwoty.

## 3. Równowaga argumentów

Ogólnie rzetelna: przy każdym działaniu jest blok "Obrona działania" z argumentami strony broniącej, a stanowiska są przypisane imiennie. Uwagi:

- **Działania prezesa Rzeplińskiego (pkt 3):** obrona i krytyka są obecne (TK za Rzeplińskiego i RPO z jednej strony; Sejm VIII kadencji, Informacja TK 2016 i K 1/17 z drugiej). Brakuje argumentu Prezydenta Dudy, że prezes TK nie dopuścił trzech sędziów także do Zgromadzenia z 2016.11.30, przez co uchwała zapadła przy 9 sędziach (`kierownictwo-2016.md`, "Stanowiska stron"). To ważny punkt dla oceny pkt 3 i 6.
- **Uchwały Sejmu 2024 i 2026 (pkt 9):** krytyka ograniczona do "uchwała nie jest źródłem prawa". Repo daje więcej: U 5/24 jako wyrok przeciw uchwale (jest w "Ocenie"), zastrzeżenie, że uchwała z 2024 r. pomija powierzenie obowiązków z 2016.12.20 (`kierownictwo-2016.md`, "Skąd różnica o jeden dzień") oraz fakt, że uchwała uznaje także uchwały z 2015.11.25 o Hauserze, Jakubeckim i Ślebzaku za pozbawione mocy, nie rozstrzygając ich statusu. Po stronie obrony brakuje odesłania do orzeczeń SN i NSA, na które uchwała z 2026 r. się powołuje (`uchwala-sejmu-2026-299.md`, wstęp pkt 2).
- **Działania z 2026.10.30-2026.11.03 (pkt 11):** obrona Korwin-Piotrowskiej jest oddana dobrze (art. 12 ust. 4, uchwała Sejmu pkt 3, "urzędujący", obowiązek udziału). Brakuje natomiast opisu działań innych uczestników, które repo odnotowuje: rząd (premier: "obowiązek władzy wykonawczej", zapewnienie warunków pracy; wejście sędziów do TK od strony KPRM; obecność policji, którą Prezydent przypisuje premierowi) oraz zarzut premiera wobec Prezydenta o "siłowe wkroczenie na teren TK" (`premier-2026-11-03.md`, `rbn-2026-11-03.md`, `okres-2024-2026.md` pkt 11). Kolumna "Kto" w tabeli wymienia "Prezydent", ale w tekście działanie Prezydenta sprowadza się do zwołania RBN. Polecenie wymagało opisu działań i argumentów obu stron; tu obraz jest niepełny po stronie rządu i Prezydenta.
- **Odmowa ślubowań 2026 (pkt 10):** obrona jest oddana (KPRP, Przydacz, wymóg stażu Berka). Można dodać podstawę z K 3/26, czyli art. 126 Konstytucji (Prezydent czuwa nad przestrzeganiem Konstytucji), bo to rdzeń argumentu Prezydenta (`k-3-26.md`).
- **Kadencja prezes (pkt 7):** jedyny punkt bez bloku "Obrona działania". Argumenty obu stron są w "Ocenie", więc treściowo jest równowaga, ale struktura jest niespójna.
- **Odmowa publikacji (pkt 4):** obrona oddana (Szydło, KPRM, wnioskodawcy 2018). Warto dodać uzasadnienie umorzenia z 2017 r. ("ochrona interesu publicznego"), bo to jedyny dokument organu po stronie obrony (`publikacja-wyrokow.md`, "Odpowiedzialność prawna").

## 4. Część 2: kryteria, dominacje, przepisy

### Oceny według kryteriów

- **[B] Wariant 1 i 2, K5 (wykonalność):** niesymetryczne. Wariant 1: "już realizowany". Wariant 2: "wymaga zgody większości sejmowej, której nie ma". Oba warianty są dziś praktyką jednej strony (repo: wariant 2 to "praktyka Prezydenta od 2026.04") i oba nie kończą sporu bez zgody drugiej strony. Albo oba trzeba ocenić "realizowany, bez uznania drugiej strony", albo oba "wymaga zgody drugiej strony".
- **[B] Wariant 3, K5:** niepełne. Analiza wymienia tylko przeciwników (Czarzasty, Żurek, Tusk, Wójcik), a pomija zwolenników: PSL (Kosiniak-Kamysz, Pasławska), Polska 2050 (Hołownia), Razem, Konfederacja, HFPC zarząd, Fundacja Batorego, senatorowie koalicji (druk 55). Koalicja jest w tej sprawie podzielona, co dla kryterium "głosy w Sejmie" jest kluczowe (`scenariusze-naprawy.md`, tabela wariantów i indeks stron).
- **[N] Niepełne kryteria.** Polecenie wymaga oceny każdego z sześciu kryteriów dla każdego wariantu. Braki: G (brak K3, K5), H (brak K2, K3, K4, K6), J (brak K2, K3, K6), K (brak K2, K4), 4 i 7 (K2-K4 "nieznane" lub "nie da się ocenić", co jest dopuszczalne, ale należało to uzasadnić odesłaniem do repo).
- **[N] Wariant B, "Koszt: budżet TK zablokowany":** repo mówi, że rządowy projekt budżetu na 2027 r. nie ma części dla TK, a o budżecie zdecyduje Sejm; "zablokowany" jest skrótem. Brakuje też wskazania, że obie strony mają ten sam problem z kworum (`zgromadzenie-2026-11-03.md`, pkt 5).
- **[S] Wariant 8, K3:** "28 sędziów bojkotowało" pochodzi z mediów [media x2]; wypada to oznaczyć.
- Pozostałe oceny (K1 dla 3, 5, 6, E, I; K2 dla 6 i F; K4 dla A; K6 dla 4) mają uzasadnienie w repo.

### Dominacje

Polecenie definiuje dominację jako "gorsze we wszystkim od innego". Sprawdzenie według ocen samej analizy:

- **8 zdominowane przez E:** zgodne z ocenami (ta sama większość, E lepsze lub równe w K2-K6). Prawidłowe.
- **I zdominowany przez E:** w K1 większości są różne (2/3 ustawowej liczby członków Zgromadzenia Narodowego vs 2/3 głosów w Sejmie i bezwzględna większość w Senacie), ale obie dziś nieosiągalne; w K2-K6 E lepsze. Dopuszczalne, z zastrzeżeniem, że I nie jest wariantem naprawy TK, tylko odpowiedzialności, więc porównanie jest nieco sztuczne.
- **B zdominowane przez 1:** zgodne z ocenami. Warto jednak zaznaczyć, że repo traktuje B jako trwający element praktyki z wariantu 1 ("Stan: od 2026.10.30 trwa spór o to, kto kieruje TK"), więc wybór między nimi nie jest w pełni niezależny.
- **[B] 4 "słabo zdominowany" przez 3:** niezgodne z własnymi ocenami analizy. W K5 wariant 4 oceniono "formalnie wykonalny, bo nic nie wymaga teraz", a wariant 3 "niska". W K6 wariant 4 "wysokie", wariant 3 "średnie". Skoro 4 jest lepszy w K5, nie jest zdominowany. Argument "wykonalność 3 po wyborach byłaby co najmniej taka sama" jest spekulacją bez oparcia w repo. "Słaba dominacja" nie jest pojęciem z polecenia.
- **[N] 7 "praktycznie zdominowana" przez E:** dla 7 analiza napisała "K2-K4: nie da się ocenić", więc dominacji nie da się stwierdzić. Należało to umieścić wśród wyborów niemożliwych do rozstrzygnięcia z braku treści, nie wśród dominacji.
- **[N] Pominięte kandydatury:** według ocen analizy H (referendum: "niczego nie rozstrzyga", K6 "dalsza polaryzacja") wydaje się zdominowane przez C (K1 zgodne z prawem, K5 samoczynnie, K6 niskie, K2-K4 tak samo nic nie rozwiązuje). Podobnie A wobec C: C to A plus upływ kadencji, który i tak następuje; analiza łączy je potem w jednym wyborze "C i A", co sugeruje, że dostrzega podobieństwo, ale nie wyciąga wniosku.

### Przepisy

- Art. 235 ust. 4 i 7, art. 122 ust. 3-5, art. 98 ust. 3, art. 145 ust. 2, art. 158 ust. 1, art. 125 ust. 2, art. 144 ust. 3 pkt 21, art. 196, art. 87, art. 8 ust. 2: opisane poprawnie względem `zrodla/konstytucja.md`.
- **[N] "Ustawę o zmianie Konstytucji Prezydent podpisuje bez prawa weta (art. 235 ust. 7)":** przepis mówi tylko, że Prezydent podpisuje ustawę w 21 dni. Brak weta jest wnioskiem z braku odesłania do art. 122 ust. 5, nie treścią przepisu. Należy to oznaczyć jako wykładnię (powszechnie przyjmowaną), nie cytat. Analiza słusznie zaznacza, że repo nie analizuje skierowania takiej ustawy do TK.
- "Rozdział o TK nie podlega referendum zatwierdzającemu": poprawne, art. 235 ust. 6 dotyczy rozdziałów I, II i XII, a TK jest w rozdziale VIII.
- Art. 6 ust. 1: błędne odesłanie, opisane w tabeli (pkt 3).

### Brakujące warianty i kryteria

Wszystkie 8 scenariuszy z debaty i 11 z analiz AI (A-K) są uwzględnione. Wariant 3 ma w repo kilka odmiennych podwariantów (Zalasiński 7/5/3 między Sejm, Senat i Prezydenta; Szczucki 12 sędziów na 12 lat od następnej kadencji), których analiza nie rozróżnia, choć różnią się istotnie w K3 i K5 (wariant Szczuckiego od następnej kadencji zbliża się do wariantu 4). Dodatkowe kryterium, którego brakuje przy wariantach 1, 2 i B: czas do uzyskania pełnego składu TK (repo podaje daty końca kadencji, np. Wyrembak 2027.01.30), bo to realnie różnicuje warianty C, 1 i 4.

## 5. Czytelność i styl

- Brak em dash i en dash, brak typograficznych apostrofów, daty w formacie yyyy.mm.dd. Zgodne z zasadami.
- **[S] Długość:** 4107 słów przy limicie "do ok. 3000". Przekroczenie o około jedną trzecią.
- **[S] Skróty dla laika:** KM RE, KW, KE, PG, SG RE, KPRM, RCL, HFPC pojawiają się bez rozwinięcia przy pierwszym użyciu (KM RE i KW rozwinięte są tylko w polecieniu, nie w analizie). Polecenie wymaga pisania dla laika; potrzebna krótka legenda albo rozwinięcia.
- **[S] Pojęcia bez wyjaśnienia:** "kontrasygnata", "prerogatywa", "środek tymczasowy", "spór kompetencyjny", "sąd ustanowiony ustawą", "art. 52 Konwencji", "dominacja". Repo przy podobnych pojęciach daje jednozdaniowe wyjaśnienia; analiza robi to tylko przy vacatio legis.
- **[S] Format tabeli zbiorczej:** zwarta i czytelna, ale wpisy typu "K 39/16 (pośrednio za nim)" i "KM za" bez wyjaśnienia są trudne dla laika.
- Odesłania do repo mają formę pliku i sekcji, zgodnie z poleceniem; w kilku miejscach brakuje nazwy sekcji (np. pkt 1 "piec-miejsc.md, tabela" jest w porządku, ale pkt 5 odsyła ogólnie do "okres-2016-2019.md").

## 6. Braki do uzupełnienia (poza wyżej wymienionymi)

1. Cz. 1 pkt 1: inicjatywa prezydencka (druk 1590, pismo Prezydenta z 2013.07.10) jako element "kto działał".
2. Cz. 1 pkt 8: oznaczyć wprost, że wnioskodawcami byli premier (K 3/21) i Prokurator Generalny (K 6/21) jako organy, a repo nie wymienia nazwisk; dla K 7/21 repo faktycznie nie podaje wnioskodawcy (sprawdzono, zgodne z analizą).
3. Cz. 1 pkt 11: zażalenie II ZZ 2/26 oraz stanowisko Korwin-Piotrowskiej, że SN nie ma kompetencji wobec TK (`okres-2024-2026.md`, pkt 11), należą do "Obrony działania".
4. Cz. 2: brak odesłania do `metodologia.md`, która jest wskazaną w poleceniu podstawą kryteriów.
5. Luki: trafnie wymienione (10 pozycji). Można dodać brak składu Senatu jako warunku dla wariantów 3 i E (jest w pkt 6) oraz brak informacji, czy plan budżetu z 2026.11.03 trafił do ministra finansów.

## 7. Ocena ogólna

Analiza jest solidnie osadzona w repo: niemal każdy fakt ma odesłanie, a sprawdzenie wykazało dwa błędy faktyczne (data ślubowania względem K 34/15; odesłanie do art. 6 ust. 1 zamiast art. 4 ust. 1) oraz kilkanaście nieścisłości, głównie w przypisaniu stanowisk (KM a uchwała Sejmu) i w oznaczaniu własnych wniosków jako faktów. Rozdzielenie oceny sądu od winy osobistej jest konsekwentne i jest mocną stroną tekstu.

Najpoważniejsze słabości są w części 2 i w podsumowaniu części 1: niesymetryczna ocena wykonalności wariantów 1 i 2, pominięcie zwolenników resetu w koalicji, dominacja 4 przez 3 sprzeczna z własnymi ocenami, nieuzasadniona "dominacja" wariantu 7 oraz brak U 5/24 i K 3/26 we wniosku o tym, kogo dotyczą orzeczenia o niezgodności z prawem. Równowaga w części 1 jest zachowana w większości punktów, ale opis działań z 2026.10.30-2026.11.03 pomija rolę rządu i zarzut premiera wobec Prezydenta.

Tekst jest za długi o około jedną trzecią i używa skrótów bez rozwinięcia, co utrudnia lekturę laikowi.

Wynik: **do poprawy przed użyciem**. Po usunięciu dwóch błędów [B] z tabeli, naprawieniu czterech uwag [B] z części 2, uzupełnieniu wniosku części 1 i skróceniu tekstu analiza będzie zgodna z poleceniem.
