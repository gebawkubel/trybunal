> Etap 1 [symulacji negocjacji (issue #46)](https://github.com/gebawkubel/trybunal/issues/46): skład stołu i plan przebiegów, wersja 3 po dwóch rundach jawnej recenzji. Napisał Claude Fable 5.1 (wysoki wysiłek rozumowania, agent Claude Code) na repozytorium w wersji 78e9e45. Polecenie: [treść issue #46](etap-1-polecenie-issue.md) i [wiadomość techniczna](etap-1-wiadomosc.md); poprawki według raportów recenzji ([runda 1](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6628753608), [runda 2](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6628905883)) i wiadomości o poprawkach ([1](etap-1-wiadomosc-poprawka.md), [2](etap-1-wiadomosc-poprawka-2.md)). Poprzednie wersje: [1](https://github.com/gebawkubel/trybunal/blob/57463fe13de56d0ba7110bb1a080520fe4d6f055/badania/symulacja/etap-1.md), [2](https://github.com/gebawkubel/trybunal/blob/0624cb0b65dc956403ec0861cabfc6f2d21bb968/badania/symulacja/etap-1.md). Zakazy (internet, zmiany, inne katalogi) były w wiadomościach, nie wymuszone technicznie. To ocena modelu, nie ustalenie projektu. Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `e1ba02aec6254e1fc461974ebb3271d78cf98685ff32f286bed7766a406f6a74`.

---

# Etap 1: skład stołu i plan przebiegów symulacji negocjacji o TK (wersja 3, po dwóch rundach recenzji)

Wykonane na polecenie z issue #46 (plik `issue-46.md`). Materiał: repozytorium w wersji 78e9e45, bez internetu. Nie czytałem plików `badania/rekomendacje-modeli.md`, `badania/rekomendacje/`, `badania/bilans-propozycji.md` ani `badania/odpowiedz.md`. W `badania/scenariusze-naprawy.md` pominąłem wiersz tabeli, który streszcza rekomendacje modeli. Wersja 2 poprawiła blokery B1-B6 z recenzji (runda 1), wersja 3 poprawia blokery R2-B1 do R2-B3 (runda 2); wykaz zmian jest na końcu.

Oznaczenia: fakt ma w nawiasie nazwę pliku, z którego pochodzi. Zdania oznaczone "ocena wykonawcy" to moje wnioski z tych faktów, nie ustalenia repozytorium. Liczby głosów to stan z `badania/sily-i-glosy.md` na 2026.11.04: Sejm 460 posłów, koalicja (KO 156, PSL-Trzecia Droga 32, Lewica 21, Polska 2050 15, Centrum 15) 239, PiS 147, Rozwój Plus 40, Konfederacja 17, Razem 4, Konfederacja Korony Polskiej 3, Demokracja Bezpośrednia 3, niezrzeszeni 7. Opozycja prawicowa (PiS, Rozwój Plus, Konfederacja, Korona, Demokracja Bezpośrednia) to 210. Senat ma 99 miejsc, z których jedno jest puste po śmierci Mirosława Różańskiego; kluby koalicji mają 58 (`badania/warunki-rozwiazan.md`). Wszystkie progi liczę przy pełnej sali, jak repozytorium.

Słowniczek: "weto" to prawo zablokowania drogi; "niezbędny" to ktoś, bez kogo próg głosów nie wychodzi przy podanym założeniu o tym, kto głosuje za, albo bez kogo rozwiązanie nie zadziała w praktyce. Niezbędność zależy od założenia, dlatego przy każdym wniosku o głosach podaję, kogo liczę jako "za".

## 1. Ścieżki rozwiązania: kto ma weto, kto jest niezbędny

### Ścieżka A: zwykła ustawa o TK (bez zmiany Konstytucji)

| Krok | Próg lub podstawa | Kto decyduje | Stan w repozytorium |
|---|---|---|---|
| Uchwalenie w Sejmie | zwykła większość przy obecności co najmniej 230 posłów; przy pełnej sali 231 (art. 120 Konstytucji, `zrodla/konstytucja.md`) | koalicja ma 239, czyli 8 głosów zapasu. Gdy za głosuje tylko koalicja: bez PSL (207), bez Lewicy (218), bez Polski 2050 (224) albo bez Centrum (224) nie ma 231. Gdy do koalicji dołączą Razem i niezrzeszeni (11), brak Polski 2050 albo Centrum daje 235, czyli wystarcza; brak Lewicy daje 229, za mało (`badania/sily-i-glosy.md`; różnice to moje wyliczenia) | przy samej koalicji każdy z pięciu klubów ma faktyczne weto; przy wsparciu Razem i niezrzeszonych weto mają tylko KO, PSL i Lewica (ocena wykonawcy) |
| Senat | może odrzucić albo poprawić; Sejm odrzuca stanowisko Senatu bezwzględną większością (art. 121 ust. 3) | Senat nie ma weta, bo koalicja ma w Sejmie bezwzględną większość, a w Senacie 58 z 99 | brak odrębnego weta |
| Prezydent | w 21 dni podpisuje, kieruje do TK (art. 122 ust. 3) albo wetuje (art. 122 ust. 5); nie może zrobić obu rzeczy naraz | Karol Nawrocki | ma weto; przejście do ścieżki B |
| TK | gdy Prezydent skieruje ustawę do TK i TK uzna ją za niezgodną, Prezydent odmawia podpisu i żadna większość tego nie zmienia (art. 122 ust. 4) | TK pod kierunkiem Prezesa Bogdana Święczkowskiego; tak upadł pakiet z 2024 roku (Kp 3/24, `zrodla/okres-2024-2026/kp-3-24.md`) | drugie weto, uruchamiane przez Prezydenta |
| Po podpisaniu | wniosek do TK może złożyć m.in. Prezydent, 50 posłów, Prokurator Generalny (art. 191) | PiS ma 147 posłów, więc sam może zaskarżyć ustawę już obowiązującą | kontrola następcza; nie jest w repozytorium analizowana dla tej ścieżki (ocena wykonawcy) |

Niezbędni w ścieżce A: 231 głosów (przy samej koalicji wszystkie jej kluby) i Prezydent (podpis). TK jest wetem warunkowym, zależnym od tego, czy Prezydent skieruje ustawę. Stanowiska: Tusk i Czarzasty chcą rozwiązania bez zmiany Konstytucji; poseł KO Tomczykiewicz mówi o powrocie do projektu z wyborem 3/5; Bogucki (szef Kancelarii Prezydenta) mówi o ustawie jako pierwszym kroku, ale "chyba nie z Donaldem Tuskiem" (`badania/scenariusze-naprawy.md`, `badania/propozycje-na-stole.md`).

### Ścieżka B: ustawa po wecie Prezydenta

| Krok | Próg | Kto ma głosy |
|---|---|---|
| Odrzucenie weta | 3/5 przy obecności co najmniej połowy posłów; przy pełnej sali 276 (art. 122 ust. 5) | wszyscy poza PiS i Rozwojem Plus to 273, o 3 za mało. Koalicja z Rozwojem Plus ma 279. Koalicja z PiS ma 386 (`badania/sily-i-glosy.md`) |
| Blokada | 185 głosów przeciw | PiS z Rozwojem Plus (187) blokuje; PiS z Konfederacją (164) nie blokuje (`badania/sily-i-glosy.md`) |
| Po odrzuceniu weta | Prezydent podpisuje w 7 dni i nie może już kierować ustawy do TK (art. 122 ust. 5) | kontrola następcza na wniosek 50 posłów nadal możliwa (art. 191; ocena wykonawcy) |

Niezbędni w ścieżce B, według założenia (wyliczenia własne z liczb w `badania/sily-i-glosy.md`):

- zawsze: PiS albo Rozwój Plus, bo bez obu jest najwyżej 273; KO jest niezbędna, gdy PiS głosuje przeciw (bez KO i PiS zostaje 157), ale gdy PiS głosuje za, wszyscy bez KO mają 304;
- gdy za głosuje koalicja z PiS (386): żaden mniejszy klub koalicji nie jest niezbędny;
- gdy za głosuje koalicja z Rozwojem Plus, a PiS i Konfederacja przeciw (279, zapas 3): niezbędne są wszystkie kluby koalicji, bo brak najmniejszego (15) daje 264;
- gdy do koalicji z Rozwojem Plus dołączy Konfederacja (296): brak Polski 2050 albo Centrum (281) wystarcza, brak Lewicy (275) nie, brak PSL (264) nie; z Razem i niezrzeszonymi (307) nawet brak PSL (275) nie wystarcza, brak Lewicy (286) tak.

Rozwój Plus jest jedynym klubem opozycji, który razem z koalicją daje 3/5 (`badania/sily-i-glosy.md`). Przy nieobecnościach próg spada, ale repozytorium nie zakłada nieobecności.

### Ścieżka C: zmiana Konstytucji (reset konstytucyjny i warianty)

| Krok | Próg lub podstawa | Kto ma głosy |
|---|---|---|
| Inicjatywa | co najmniej 1/5 ustawowej liczby posłów, czyli 92, Senat albo Prezydent (art. 235 ust. 1) | sam KO (156) albo sam PiS (147); Rozwój Plus, PSL, Konfederacja i Razem razem mają 93 (`zrodla/okres-2024-2026/kj-29-warunkow.md`, pkt 7); Senat większością koalicji; sam Prezydent. Rozwój Plus z Konfederacją (57) nie wystarczą |
| Sejm | 2/3 przy obecności co najmniej połowy posłów; przy pełnej sali 307 (art. 235 ust. 4) | koalicja z PiS 386. Bez PiS: koalicja, Rozwój Plus, Konfederacja i Razem to 300, więc trzeba jeszcze 7 z 13 posłów niezrzeszonych, Korony i Demokracji Bezpośredniej; wszyscy poza PiS to 313 (`badania/sily-i-glosy.md`) |
| Blokada w Sejmie | 154 głosów przeciw | PiS sam (147) nie blokuje; PiS z Rozwojem Plus (187) albo z Konfederacją (164) blokuje. Ocena wykonawcy: Lewica (21) z PiS (168) też blokuje, a KO (156) blokuje sama |
| Senat | bezwzględna większość przy obecności co najmniej połowy senatorów, w 60 dni od Sejmu (art. 235 ust. 2 i 4) | kluby koalicji 58 z 99 (jedno miejsce puste); barierą jest Sejm, nie Senat (`badania/warunki-rozwiazan.md`) |
| Referendum zatwierdzające | tylko dla rozdziałów I, II i XII (art. 235 ust. 6) | przepisy o TK są w rozdziale VIII, więc referendum nie jest wymagane (ocena wykonawcy na podstawie `zrodla/konstytucja.md`) |
| Prezydent | podpisuje w 21 dni (art. 235 ust. 7); sporne, czy może skierować zmianę do TK | dwa odczytania, nierozstrzygnięte (`badania/warunki-rozwiazan.md`, cz. 2) |
| Terminy | pierwsze czytanie nie wcześniej niż 30 dni od złożenia (art. 235 ust. 3) | droga trwa co najmniej kilka miesięcy (ocena wykonawcy) |

Niezbędni w ścieżce C: KO, bo bez niej nie ma 307 (460 minus 156 to 304); PiS, chyba że za zmianą zagłosują niemal wszyscy inni (z 313 można stracić tylko 6 głosów). Gdy głosuje PiS z koalicją (386), żaden mniejszy klub nie jest niezbędny (bez PSL 354, bez Lewicy 365). W wariancie bez PiS niezbędne są PSL, Lewica, Polska 2050, Centrum, Rozwój Plus, Konfederacja (razem 296) i co najmniej 11 z 17 głosów Razem, Korony, Demokracji Bezpośredniej i niezrzeszonych, czyli na przykład Razem i co najmniej 7 z pozostałych 13. Lewica zapowiedziała sprzeciw wobec każdego resetu ("Nie poprę żadnego resetu, nie poprę zmiany konstytucji", Czarzasty, `badania/scenariusze-naprawy.md`). Ocena wykonawcy: w praktyce ta ścieżka wymaga zgody Tuska i Kaczyńskiego albo Tuska i całej reszty Sejmu łącznie z Lewicą; obie te zgody są dziś zaprzeczone w cytowanych wypowiedziach.

Za resetem w jakiejś formie są: PSL, Polska 2050, Rozwój Plus, Konfederacja, Razem, Fundacja Batorego, HFPC, Klub Jagielloński; Bogucki mówi o "restarcie" "ostatecznie"; Prezydent mówi o resecie po wyborach 2027. Przeciw: Tusk, Czarzasty, Żurek, posłowie KO, poseł PiS Wójcik; Komisja Wenecka w 2024 roku nie poparła wygaszenia wszystkich kadencji (`badania/scenariusze-naprawy.md`, `badania/propozycje-na-stole.md`, `badania/warunki-rozwiazan.md`).

### Ścieżka D: porozumienie polityczne bez ustawy

Nie ma progu głosów. Liczy się, kto kontroluje fakty, które druga strona chce zmienić. Z repozytorium wynika, że są to:

| Kto | Co kontroluje | Źródło |
|---|---|---|
| Prezydent Nawrocki | odbieranie ślubowania od pięciorga wybranych (odmawia od 2026.04); wniosek Kpt 1/26 (mógłby go cofnąć); zaproszenia na RBN i konsultacje; termin "przed Świętem Niepodległości" dla premiera | `badania/okres-2024-2026.md`, `zrodla/okres-2024-2026/rbn-2026-11-03.md`, `zrodla/okres-2024-2026/kpt-1-26.md` |
| Premier Tusk i rząd | policja przy TK, wejście do TK od strony KPRM, publikacja wyroków TK w Dzienniku Ustaw (85 nieopublikowanych wyroków z lat 2024-2026 według wykazu na stronie TK), projekt budżetu na 2027 rok bez części dla TK | `badania/okres-2024-2026.md`, `badania/skutki-dla-obywateli.md`, `badania/zgromadzenie-2026-11-03.md` |
| Minister sprawiedliwości i Prokurator Generalny Żurek | 7 wniosków o uchylenie immunitetu Święczkowskiego i Sochańskiego, śledztwa, przeszukanie w TK | `badania/postepowania-wobec-osob.md` |
| Marszałek Sejmu Czarzasty | uchwały Sejmu, ślubowanie w Sejmie, wręczanie uchwał o wyborze, odmowa nadania biegu projektowi budżetu TK Prezesa | `badania/okres-2024-2026.md`, `badania/zgromadzenie-2026-11-03.md` |
| Prezes Święczkowski i Wiceprezes Sochański | dopuszczanie sędziów do orzekania, zwoływanie Zgromadzenia Ogólnego, wyznaczanie składów, w tym w Kpt 1/26, postępowania dyscyplinarne wobec sędziów z 2026 roku; skład TK orzekający w Kp 3/24 i K 3/26 | `badania/okres-2024-2026.md`, `badania/postepowania-wobec-osob.md` |
| Anna Korwin-Piotrowska i ośmioro sędziów z 2026 roku | przerwa w czynnościach Prezesa, zgromadzenie z 2026.11.03, plan wydatków TK, losowanie składów dyscyplinarnych, sprawy pracownicze Kancelarii TK; skarga w ETPC (17392/26) | `badania/zgromadzenie-2026-11-03.md`, `zrodla/okres-2024-2026/komunikat-31-pazdziernika.md` |
| Sąd Najwyższy (Pierwszy Prezes Kapiński, Kolegium) | zażalenie II ZZ 2/26, uchwała Kolegium przeciw odsunięciu Prezesa TK | `badania/okres-2024-2026.md` |
| ETPC, TSUE, Komitet Ministrów, Komisja Wenecka | ocena wykonania wyroków, środek tymczasowy, opinie | `badania/wyroki-europejskie.md` |

Ocena wykonawcy: porozumienie bez ustawy to wymiana "ślubowania i dopuszczenie do orzekania" za "wycofanie policji, przerwy w czynnościach, wniosków prokuratury". Obie strony 2026.11.03 wezwały drugą do pierwszego kroku (`badania/scenariusze-naprawy.md`). Trwałość takiego porozumienia zależy od tego, czy sędziowie obu grup je wykonają, bo formalnie nie podlegają politykom, i od prokuratury, która formalnie działa niezależnie od premiera.

### Ścieżka E: obecna praktyka (uchwała Sejmu, wybór większością 231, ślubowanie w Sejmie)

Koalicja robi to sama. Według `zrodla/glosowania-tk-2015-2026.md`:

- uchwała z 2024.03.06: za KO, PSL-TD, Polska 2050-TD i Lewica (240), przeciw PiS i Konfederacja (197); klubu Centrum wtedy nie było;
- uchwała z 2026.03.13 (G1): za KO, PSL-TD, Centrum, Polska 2050 i Lewica (235), przeciw PiS, Konfederacja, Korona, Demokracja Bezpośrednia i 2 niezrzeszonych (197); Razem nieobecne;
- wybór sześciorga sędziów 2026.03.13 (G2) i Sławomira Patyry 2026.06.11 (G3): za te same pięć klubów koalicji, przeciw PiS i Konfederacja, Razem wstrzymało się;
- wybór Macieja Berka 2026.09.04 (G4): za Berkiem KO, PSL-TD, Centrum, Lewica i Polska 2050 (226); za Kotowskim PiS, Rozwój Plus, Demokracja Bezpośrednia i 1 niezrzeszony (184); Konfederacja, Korona i troje z Razem "przeciw wszystkim".

Blokują tę ścieżkę w praktyce Prezydent (brak ślubowania) i Prezes TK (brak dopuszczenia). Ocena wykonawcy: ta ścieżka nie kończy sporu, tylko go utrwala; to punkt wyjścia dla koalicji przy braku porozumienia.

### Ścieżka F: zmiana rządu albo przedterminowe wybory

| Wariant | Próg | Kto ma głosy |
|---|---|---|
| Skrócenie kadencji Sejmu uchwałą | zawsze 307 z ustawowej liczby posłów (art. 98 ust. 3) | wymaga KO i PiS razem albo KO i prawie wszystkich pozostałych; Bosak zapowiedział projekt, nie złożył (`badania/propozycje-na-stole.md`) |
| Konstruktywne wotum nieufności | 231 z ustawowej liczby, wniosek 46 posłów z nazwiskiem premiera (art. 158) | opozycja prawicowa 210; z Razem i niezrzeszonymi 221, za mało. Które kluby koalicji same domykają 231 (wyliczenia własne z `badania/sily-i-glosy.md`): przy samej opozycji prawicowej KO (366), PSL (242) i Lewica (dokładnie 231); Polska 2050 albo Centrum dają 225, za mało. Przy opozycji z Razem i niezrzeszonymi każdy klub koalicji wystarcza: PSL 253, Lewica 242, Polska 2050 albo Centrum 236. Morawiecki proponuje rząd techniczny Marka Jurka; Zandberg uważa to za "arytmetycznie nierealne" (`badania/scenariusze-naprawy.md`) |
| Skrócenie kadencji przez Prezydenta | tylko gdy Sejm nie powoła rządu (art. 155 ust. 2) albo nie uchwali budżetu w 4 miesiące (art. 225) | budżet na 2027 rok jest w Sejmie bez części dla TK (`badania/zgromadzenie-2026-11-03.md`); ocena wykonawcy: art. 225 to realna dźwignia Prezydenta, jeśli spór o budżet TK opóźni całą ustawę budżetową |
| Dymisja rządu | sama nie daje Prezydentowi prawa rozpisania wyborów (`badania/scenariusze-naprawy.md`, uwaga prawna) | Czarnek (PiS) wzywa do dymisji |

Niezbędni w wotum nieufności (wyliczenia własne z `badania/sily-i-glosy.md`): zawsze PiS i Rozwój Plus, bo bez PiS opozycja prawicowa ma 63, a bez Rozwoju Plus 170, i nawet z PSL (95 albo 202) nie ma 231. Konfederacja jest niezbędna tylko wtedy, gdy przechodzi sam PSL albo sama Lewica bez Razem i niezrzeszonych (bez Konfederacji 193 + 32 = 225, 193 + 21 = 214); z Razem i niezrzeszonymi PSL wystarcza także bez Konfederacji (204 + 32 = 236). Korona i Demokracja Bezpośrednia (6) są niezbędne tylko w wariancie z samą Lewicą (dokładnie 231); przy PSL bez nich jest 204 + 32 = 236. Z klubów koalicji PSL i Lewica wystarczają same, Polska 2050 albo Centrum tylko z Razem i niezrzeszonymi. KO arytmetycznie też wystarcza (366), ale to rachunek, nie scenariusz: wotum jest skierowane przeciw premierowi z KO. W skróceniu kadencji KO i PiS.

### Ścieżka G: rozstrzygnięcie przez organ, którego obie strony posłuchają

Kpt 1/26 jest w toku przed TK, którego skład jest sporny; skarga 17392/26 w ETPC nie ma terminu; SN rozpoznaje II ZZ 2/26, a Korwin-Piotrowska odmawia SN kompetencji (`badania/okres-2024-2026.md`, `badania/zgromadzenie-2026-11-03.md`). Trybunał Stanu dla Prezydenta wymaga 2/3 Zgromadzenia Narodowego (art. 145), czyli zgody PiS. Referendum (art. 125) może zarządzić Sejm bezwzględną większością, ale jego wynik nie zmienia składu TK bez ustawy. Wniosek repozytorium: "Nie ma organu, którego rozstrzygnięcie obie strony uznają" (`badania/zgromadzenie-2026-11-03.md`, wniosek 6). Uwaga dla etapu 2: Trybunał Stanu, referendum i rozstrzygnięcie Kpt 1/26 lub ETPC jako wyjścia ze sporu są w `badania/scenariusze-naprawy.md` tylko w części "Scenariusze z analiz AI", której issue nie dopuszcza do pakietu wiedzy; w pakiecie mogą być wyłącznie fakty o tych postępowaniach (przepisy, stan spraw), bez tej listy scenariuszy.

### Ścieżka H: czekanie na 2027 rok

Kadencja Jarosława Wyrembaka kończy się 2027.01.30; innych dat końca kadencji repozytorium nie podaje. Wybory parlamentarne jesienią 2027; Prezydent mówi o "resecie" po nich (`badania/scenariusze-naprawy.md`). Ocena wykonawcy: to jest alternatywa każdej strony wobec porozumienia, więc karty postaci muszą opisać, co każda z nich zyskuje przez czekanie.

### Podsumowanie: kto jest niezbędny na którejkolwiek ścieżce

Kolumny A, B i C podają niezbędność przy założeniu, kto głosuje za. A: za głosuje sama koalicja (w nawiasie: z Razem i niezrzeszonymi). B: za głosuje koalicja z Rozwojem Plus, PiS i Konfederacja przeciw (w nawiasie: gdy głosuje PiS). C: za głosują wszyscy poza PiS (w nawiasie: gdy głosuje PiS).

| Osoba lub podmiot | A (231) | B (276) | C (307) | D (bez ustawy) | F (zmiana rządu) |
|---|---|---|---|---|---|
| Prezydent Nawrocki | weto | ominięty, ale TK dalej dostępny | podpis; sporny wniosek do TK | kontroluje ślubowanie | art. 225 |
| Tusk, KO (156) | niezbędny (niezbędny) | niezbędny (nie: bez KO z PiS 304) | niezbędny (niezbędny: bez KO 304) | kontroluje policję, publikację, budżet | cel wotum (arytmetycznie 366, ale wotum jest przeciw premierowi z KO) |
| Kaczyński, PiS (147) | 50 posłów do TK po podpisie | nie (wystarcza zamiast Rozwoju Plus) | niezbędny, chyba że 307 z 313 | wpływ na Prezydenta nieudokumentowany | niezbędny do 307 i do 231 opozycji |
| Morawiecki, Rozwój Plus (40) | nie | niezbędny (nie) | niezbędny bez PiS; z PiS blokuje | własny projekt | wnioskodawca wotum; niezbędny do 231 opozycji |
| Kosiniak-Kamysz, PSL (32) | niezbędny (niezbędny) | niezbędny (nie) | niezbędny bez PiS (nie) | - | sam domyka 231 dla opozycji |
| Czarzasty, Lewica (21), Marszałek Sejmu | niezbędny (niezbędny) | niezbędny (nie) | niezbędny bez PiS (nie); zapowiedziany sprzeciw | kontroluje Sejm | sam domyka dokładnie 231 |
| Hołownia, Polska 2050 (15) | niezbędny (nie: 235) | niezbędny (nie) | niezbędny bez PiS (nie) | - | domyka 231 tylko z Razem i niezrzeszonymi |
| Centrum (15) | niezbędny (nie: 235) | niezbędny (nie) | niezbędny bez PiS (nie) | - | jak Polska 2050 |
| Bosak i Mentzen, Konfederacja (17) | nie | nie (273 bez PiS i RP) | niezbędni bez PiS; z PiS blokują | - | niezbędni do 231 opozycji; zapowiedź projektu 307 |
| Święczkowski, TK | weto po skierowaniu przez Prezydenta | kontrola następcza | wątpliwe | kontroluje TK | - |
| Korwin-Piotrowska, sędziowie z 2026 | - | - | ich los jest przedmiotem | kontrolują budynek i zgromadzenie | - |
| Razem, Korona, Demokracja Bezpośrednia, niezrzeszeni (17) | zapas dla koalicji | nie | co najmniej 11 z nich bez PiS (nie) | - | 221 z opozycją |
| Senat, Kidawa-Błońska | brak weta | - | koalicja ma 58 z 99 | - | - |

## 2. Kto siedzi przy stole

Kryterium: osoba ma weto albo jest niezbędna na co najmniej jednej z realnych ścieżek (A, B, C, D, F) i jest identyfikowana w repozytorium z imienia i nazwiska. Każda postać reprezentuje jeden obóz. Stanowiska wyjściowe są w repozytorium poza wyjątkami opisanymi w części 5.

### Skład podstawowy (10 postaci i arbiter)

1. **Karol Nawrocki, Prezydent RP.** Weto zwykłej ustawy, wniosek do TK, podpis zmiany Konstytucji, ślubowanie, Kpt 1/26, RBN, art. 225. Stanowiska w repozytorium: wywiad z 2026.10.15 ("twarda odpowiedź", reset po 2027), komunikat z RBN, komunikaty Kancelarii (`badania/scenariusze-naprawy.md`, `zrodla/okres-2024-2026/rbn-2026-11-03.md`, `badania/okres-2024-2026.md`). Bez niego nie ma żadnej ścieżki poza B i C, a i tam ma narzędzia.
2. **Donald Tusk, premier, KO (156).** Największy klub, bez którego nie ma 307 (wszyscy inni to 304), nie ma 231 przy samej koalicji (83), a 276 tylko wtedy, gdy za głosuje PiS; rząd kontroluje policję, publikację wyroków i budżet. Stanowisko: "bez zmian w Konstytucji", apel o dopuszczenie sędziów, propozycja spotkania "w cztery oczy" (`badania/propozycje-na-stole.md`, `zrodla/okres-2024-2026/premier-2026-11-03.md`). Reprezentuje też rząd, w tym ministra Żurka i rzecznika Szłapkę (uzasadnienie pominięcia Żurka niżej).
3. **Jarosław Kaczyński, PiS (147).** PiS jest niezbędny do 2/3 (chyba że zagłosuje 307 z 313 pozostałych), wystarcza do odrzucenia weta zamiast Rozwoju Plus i wraz z Rozwojem Plus albo Konfederacją blokuje zmianę Konstytucji; 50 posłów PiS może zaskarżyć każdą ustawę. Repozytorium cytuje jego wezwanie do oporu "o charakterze społecznym" z 2026.09.29, rzecznika Bochenka i posłów Wójcika i Czarnka (`badania/scenariusze-naprawy.md`). Uwaga: repozytorium nie zapisuje jego funkcji partyjnej ani oficjalnego stanowiska PiS wobec resetu; to luka do uzupełnienia w etapie 2. Wybieram go, bo jest jedynym politykiem PiS, którego repozytorium pokazuje jako głos partii w tym sporze.
4. **Mateusz Morawiecki, Rozwój Plus (40).** Jedyny klub opozycji, który z koalicją daje 276; niezbędny do 307 bez PiS; z PiS blokuje 2/3 i odrzucenie weta. Ma własny projekt zmiany Konstytucji "Trybunał dla Rzeczypospolitej" z 2026.10.07 i proponuje konstruktywne wotum nieufności (`zrodla/okres-2024-2026/rozwoj-plus-trybunal-2026.md`, `badania/scenariusze-naprawy.md`). Reprezentuje też Krzysztofa Szczuckiego, współprezentującego projekt (nazwisk autorów karta nie podaje).
5. **Władysław Kosiniak-Kamysz, PSL (32).** Przy samej koalicji bez PSL jest 207, więc PSL ma weto w ścieżce A i w wariancie B z Rozwojem Plus; w ścieżce F jest jednym z dwóch klubów koalicji (obok Lewicy; KO pomijam, bo wotum jest przeciw jej premierowi), które same domykają 231 dla konstruktywnego wotum nieufności, i jedynym z nich, który ma własny plan resetu zbieżny z opozycją; "od 2024 roku konsekwentnie postuluje reset konstytucyjny" (`zrodla/okres-2024-2026/psl-reset-2026-11-03.md`). Reprezentuje też Urszulę Pasławską. Ocena wykonawcy: to postać z największą swobodą ruchu przy stole, bo może zarówno trwać w koalicji, jak i wejść w układ z opozycją.
6. **Włodzimierz Czarzasty, Marszałek Sejmu, Lewica (21).** Przy samej koalicji bez Lewicy jest 218; jako Marszałek kontroluje bieg projektów, ślubowanie w Sejmie i uchwały; podpisał uchwałę z 2026.03.13. Jedyny lider koalicji, który wprost odrzucił zmianę Konstytucji (`badania/scenariusze-naprawy.md`, `zrodla/okres-2024-2026/uchwala-sejmu-2026-299.md`). Lewica też sama domyka 231 dla opozycji w wotum nieufności (dokładnie 231), choć nic w repozytorium na to nie wskazuje. Reprezentuje Lewicę, w tym Gawkowskiego.
7. **Szymon Hołownia, szef klubu Polska 2050 (15).** Przy samej koalicji bez Polski 2050 jest 224; stanowisko "zlikwidowany albo odbudowany" (`badania/scenariusze-naprawy.md`). Kto kieruje partią po 2026.10.24, repozytorium nie ustaliło; klub w Sejmie prowadzi Hołownia, a głosy należą do klubu, dlatego on.
8. **Krzysztof Bosak, wicemarszałek Sejmu, Konfederacja (17).** Konfederacja jest niezbędna do 2/3 bez PiS i z PiS blokuje; ma własny projekt resetu (3/5, losowanie, ślubowanie przed Marszałkiem) i zapowiedź projektu skrócenia kadencji. Bosak był na konsultacjach u Prezydenta 2026.10.31 i na RBN 2026.11.03, a jego wypowiedzi są w dwóch kartach źródeł (`zrodla/okres-2024-2026/konfederacja-reset-2026-10-31.md`, `zrodla/okres-2024-2026/konfederacja-po-rbn-2026-11-03.md`). Sławomir Mentzen trafia do karty jako współlider (jego cytaty o "wyzerowaniu" TK i o ślubowaniu przed Prezydentem).
9. **Bogdan Święczkowski, Prezes TK według Prezydenta i SN.** Kontroluje dopuszczanie sędziów, zwoływanie Zgromadzenia, składy orzekające, Kpt 1/26 i postępowania dyscyplinarne; przewodniczył w U 5/24, jest w składzie K 3/26; jest objęty 6 wnioskami o uchylenie immunitetu (`badania/okres-2024-2026.md`, `badania/postepowania-wobec-osob.md`). Każde porozumienie bez ustawy i każdy reset dotyczy jego osoby (stan spoczynku). Reprezentuje siedmioro sędziów orzekających przed 2026 rokiem, w tym Sochańskiego; karta musi odnotować, że ta grupa nie jest jednolita (zdania odrębne Steliny, Sycha i Zielonackiego w Kp 3/24 oraz Wojciechowskiego i Wyrembaka w K 3/26, `badania/warunki-rozwiazan.md`).
10. **Anna Korwin-Piotrowska, sędzia wybrana w 2026 roku, "zastępująca Prezesa".** Zarządziła przerwę w czynnościach Prezesa, zwołała zgromadzenie ośmiorga, przejęła sprawy Kancelarii TK; jest skarżącą w ETPC 17392/26 (`badania/zgromadzenie-2026-11-03.md`, `zrodla/okres-2024-2026/etpc-17392-26.md`). Prezydent żąda od premiera cofnięcia tych działań, ale wykonać je muszą sędziowie, formalnie niezależni od rządu. Reprezentuje ośmioro sędziów z 2026 roku; karta ma odnotować odmienną postawę Sławomira Patyry (ślubował przed Prezydentem, odmawia orzekania do dopuszczenia pozostałych).

**Arbiter** (osobny agent): pilnuje kolejności, liczy głosy i sprawdza procedurę (art. 120, 122, 235, 98, 158 Konstytucji). Zasady liczenia, które proponuję:

- arbiter sumuje głosy klubów, których przedstawiciele przy stole zadeklarowali poparcie, i porównuje z progiem (231, 276, 307, a dla skrócenia kadencji 307 z ustawowej liczby); nie zakłada z góry, że jakiś klub jest "niezbędny";
- głosy klubów nieobecnych przy stole (Razem, Korona, Demokracja Bezpośrednia, niezrzeszeni) liczą się jako niedostępne;
- wyjątek: Centrum (15) liczy się tak, jak zadeklaruje przedstawiciel KO, bo we wszystkich głosowaniach o TK w 2026 roku głosowało tak jak reszta koalicji (`zrodla/glosowania-tk-2015-2026.md`, G1-G4); ta zasada jest założeniem, nie faktem o przyszłych głosowaniach, i arbiter podaje ją w zapisie;
- Senat: arbiter liczy 58 głosów koalicji na 99 miejsc (jedno puste) według deklaracji KO, Lewicy i PSL;
- Prezydent i Prezes TK nie mają głosów, ale arbiter sprawdza, czy pakiet wymaga ich czynności (podpis, ślubowanie, dopuszczenie) i czy zadeklarowali ich wykonanie; obietnice dotyczące prokuratury arbiter oznacza jako "poza gwarancją stołu", bo prokuratura formalnie działa niezależnie od premiera;
- arbiter ogłasza "brak porozumienia", gdy po ustalonej liczbie rund nie ma pakietu z głosami i wymaganymi czynnościami.

Przykłady przy składzie podstawowym (wyliczenia własne): 231 wychodzi z całej koalicji (239) albo z koalicji bez jednego małego klubu plus Rozwój Plus (np. 224 + 40 = 264) albo plus PiS; 276 wychodzi z koalicji i Rozwoju Plus (279) albo z koalicji i PiS (386); 307 wychodzi tylko z udziałem KO i PiS, bo koalicja z Rozwojem Plus i Konfederacją to 296, a głosy klubów nieobecnych są niedostępne.

### Osoby pominięte, które mogłyby wydawać się potrzebne

| Osoba | Dlaczego mogłaby się wydawać potrzebna | Dlaczego pominięta |
|---|---|---|
| Waldemar Żurek, minister sprawiedliwości i Prokurator Generalny | wnioski o immunitet, śledztwa, przeszukanie w TK; "reset to niebezpieczny pomysł" | jest członkiem rządu, za który odpowiada Tusk; jego narzędzia wpisuję do karty Tuska. Ponieważ prokuratura formalnie działa niezależnie, arbiter oznacza obietnice w tej sprawie jako "poza gwarancją stołu" (zasada wyżej); jeśli pierwszy przebieg pokaże, że to blokuje porozumienie, w kolejnych można dodać Żurka jako postać |
| Zbigniew Bogucki, szef Kancelarii Prezydenta | wypowiedź o "restarcie" i ustawie jako pierwszym kroku (2026.11.03) | mówi w imieniu Prezydenta; cytat trafia do karty Nawrockiego jako sygnał możliwego ustępstwa |
| Małgorzata Kidawa-Błońska, Marszałek Senatu | Senat głosuje nad zmianą Konstytucji w 60 dni; podpisała projekt resetu z 2024 roku | koalicja ma 58 z 99, więc Senat nie ma odrębnego weta; należy do KO; jej stanowiska z 2026 roku repozytorium nie zna |
| Przedstawiciel klubu Centrum (15) | przy samej koalicji niezbędny do 231 | repozytorium nie zna nazwiska lidera ani stanowiska klubu; zamiast postaci stosuję zasadę arbitra o głosowaniu z KO; jeśli etap 2 znajdzie źródło, można dodać postać |
| Adrian Zandberg, Razem (4) | jedyny, kto wzywa do rozmów "w skromniejszym gronie"; za resetem | 4 głosy są potrzebne tylko w wariancie "307 z 313", który w składzie podstawowym i tak nie wychodzi; przewidziany w składzie wariantowym W2 |
| Paweł Kukiz (Demokracja Bezpośrednia, 3), Grzegorz Braun (Korona, 3), 7 niezrzeszonych | potrzebni tylko do 2/3 bez PiS i do 221 opozycji | ta ścieżka 2/3 wymaga 307 z 313, więc jest nierealna bez PiS (ocena wykonawcy); Braun nie ma stanowiska w repozytorium; Kukiz w W2 |
| Sławomir Mentzen, Konfederacja | współlider, autor cytatów o resecie | jeden przedstawiciel na obóz; Bosak uczestniczył w obu spotkaniach u Prezydenta |
| Krzysztof Szczucki, Urszula Pasławska, Rafał Bochenek, Przemysław Czarnek | współprezentujący i autorzy cytatów | jeden przedstawiciel na obóz; ich wypowiedzi w kartach liderów |
| Bartłomiej Sochański, Sławomir Patyra i pozostali sędziowie | sędziowie obu grup | po jednym przedstawicielu na grupę; Patyra w składzie wariantowym W3 |
| Zbigniew Kapiński, Pierwszy Prezes SN; Kolegium SN | uchwała przeciw odsunięciu Prezesa TK, sprawa II ZZ 2/26 | wpływ, nie weto; obie strony sporu nie uznają SN za rozjemcę (Korwin-Piotrowska odmawia mu kompetencji); trafia do pakietu wiedzy |
| Marcin Wiącek, RPO | stanowisko o obowiązku ślubowania | brak weta; do pakietu wiedzy |
| Tomasz Zalasiński (Batory), Piotr Trudnowski (KJ), HFPC | gotowe projekty resetu | eksperci bez głosów; ich projekty są w pakiecie wiedzy jako materiał do wykorzystania przez postaci |
| ETPC, TSUE, Komitet Ministrów, Komisja Wenecka, Komisja Europejska | oceniają wykonanie wyroków | nie siedzą przy polskim stole; arbiter może przypominać ich stanowiska na życzenie postaci |
| Andrzej Duda, Julia Przyłębska | sprawcy wcześniejszych etapów | bez obecnych narzędzi; historia w pakiecie wiedzy |

## 3. Skład podstawowy i składy wariantowe

- **W1, skład podstawowy** (10 postaci z części 2 i arbiter). Do wszystkich przebiegów z planu głównego.
- **W2, "stół prezydencki, bez premiera".** Nawrocki, Kaczyński, Morawiecki, Kosiniak-Kamysz, Hołownia, Bosak, Zandberg, Kukiz, Święczkowski, arbiter. Nawiązuje do konsultacji u Prezydenta z 2026.10.31: według repozytorium nie uczestniczyły w nich Lewica i klub Centrum [media x1], a o KO wiadomo tylko tyle, że według ustaleń Polskiego Radia podanych przez TVP Info przed spotkaniem nie zamierzała wysłać przedstawicieli [media x1] (`badania/scenariusze-naprawy.md`). Nawiązuje też do słów Boguckiego o rozmowie "chyba nie z Donaldem Tuskiem" (`badania/propozycje-na-stole.md`). Sprawdza ścieżkę F: czy bez KO da się zbudować 231 do wotum nieufności, i pokazuje, że 307 bez KO nie istnieje. Zasady arbitra w W2: KO i Lewica głosują przeciw wszystkiemu, co stół uzgodni bez nich; Centrum liczy się jako niedostępne (nie ma przedstawiciela, a na konsultacjach go nie było), więc zasada z W1 o liczeniu Centrum z KO tu nie obowiązuje; niezrzeszeni i Korona niedostępni. Przy tych zasadach kluby obecne w W2 po stronie opozycji to PiS, Rozwój Plus, Konfederacja i Demokracja Bezpośrednia (Kukiz), razem 207, oraz Razem (4). 231 wychodzi z 207 plus PSL (239); z Polską 2050 i Razem jest 207 + 15 + 4 = 226, za mało, a nawet z nieobecną Koroną 229, też za mało. Ocena wykonawcy: W2 testuje więc przede wszystkim, czy PSL przejdzie na drugą stronę.
- **W3, "stół sędziowski".** Święczkowski, Sochański, Wojciech Sych (zdanie odrębne w Kp 3/24, drugi kandydat na najdłuższy staż), Korwin-Piotrowska, Patyra, Berek, arbiter, z Nawrockim i Tuskiem jako obserwatorami, którzy mówią tylko na wezwanie arbitra. Sprawdza, czy sami sędziowie mogą uzgodnić dopuszczenie do orzekania, cofnięcie przerwy i inne kroki w TK. Uwaga: pomysł dobrowolnych odejść sędziów jest w repozytorium tylko w części "Scenariusze z analiz AI" (`badania/scenariusze-naprawy.md`), której pakiet wiedzy nie może zawierać; W3 nie podsuwa go postaciom, sprawdza tylko, czy same na niego wpadną.
- **W4, "wielka trójka"** (tani wariant kontrolny): Nawrocki, Tusk, Kaczyński, arbiter. Sprawdza, czy sam układ trzech największych sił daje porozumienie, gdy mniejsze kluby nie mają głosu; wynik porównać z W1.

Ocena wykonawcy: W2 i W4 są najcenniejsze, bo testują dwie hipotezy obecne w debacie (porozumienie z pominięciem premiera; porozumienie tylko dużych sił, o którym mówi Zandberg). W3 jest uzupełnieniem na wypadek, gdyby W1 wskazał, że blokadą są sędziowie, a nie politycy.

## 4. Lista planowanych przebiegów

Zgodnie z sekcją "Budżet": najpierw jeden pełny przebieg, wariant (b), skład W1; po nim decyzja prowadzącego. Docelowo 3 warianty po 3 przebiegi na W1. Model dla postaci i arbitra: ten sam dla wszystkich w przebiegu (issue podaje jako przykład Claude Opus 5.5). Seria kontrolna: ten sam plan na innym modelu przez Codex, poza limitem.

| Nr | Wariant motywacji | Skład | Model | Kolejność i warunek | Szacunek kosztu |
|---|---|---|---|---|---|
| 1 | (b) ugraj jak najwięcej, ale ostatecznie dobro państwa | W1 | równy dla wszystkich (np. Opus 5.5) | pierwszy; pełny przebieg do porozumienia albo jawnego braku | K (patrz niżej) |
| decyzja | prowadzący ocenia, czy symulacja działa i ile kosztowała | | | | |
| 2 | (a) dobro państwa | W1 | ten sam | po decyzji; jeden przebieg każdego wariantu najpierw, żeby zobaczyć rozrzut między wariantami | K |
| 3 | (c) czysty interes polityczny | W1 | ten sam | | K |
| 4 | (b) | W1 | ten sam | drugie przebiegi | K |
| 5 | (a) | W1 | ten sam | | K |
| 6 | (c) | W1 | ten sam | | K |
| 7 | (b) | W1 | ten sam | trzecie przebiegi | K |
| 8 | (a) | W1 | ten sam | | K |
| 9 | (c) | W1 | ten sam | | K |
| 10 | (b) | W2 | ten sam | tylko jeśli po 9 zostaje budżet | około 0,9 K |
| 11 | (b) | W4 | ten sam | tylko jeśli zostaje budżet; tani | około 0,3 K |
| 12 | (b) | W3 | ten sam | ostatni w kolejce | około 0,6 K |
| K1-K3 | (b), (a), (c) | W1 | inny model przez Codex | seria kontrolna, poza limitem 100$ | poza limitem |

Kolejność w W1 przeplata warianty (b, a, c), żeby po trzech przebiegach mieć po jednym z każdego wariantu, a nie trzy z jednego. W każdym przebiegu kolejność pierwszych wypowiedzi: Nawrocki, Tusk, Kaczyński, Morawiecki, Kosiniak-Kamysz, Czarzasty, Hołownia, Bosak, Święczkowski, Korwin-Piotrowska; potem arbiter udziela głosu. Przebiegi 2 i 3 z tego samego wariantu powinny zmieniać kolejność otwarcia (np. zaczyna Tusk, potem Kaczyński), żeby wynik nie zależał od tego, kto mówi pierwszy.

### Szacunek kosztu jednego przebiegu (K)

Issue zleca szacunek agentowi budującemu skrypt. Podaję założenia startowe, które ma zweryfikować, i wynik w tokenach, bo cennika modelu nie znam z repozytorium i nie mogę go sprawdzić bez internetu.

Założenia: 10 postaci i arbiter; pakiet wiedzy około 35 tys. tokenów (teksty z `badania/` o głosach, warunkach, scenariuszach, propozycjach i okresie 2024-2026 to razem około 13-15 tys. słów; polski tekst to około 2-2,5 tokena na słowo); karta prywatna około 1,5 tys. tokenów; wypowiedź około 400 tokenów; 10 wypowiedzi otwarcia, najwyżej 8 rund po 10 wypowiedzi i runda głosowania, czyli około 100 wypowiedzi; arbiter około 30 wywołań. Wątek pod koniec ma około 40 tys. tokenów.

Wynik: wejście około 100 wywołań razy średnio 57 tys. tokenów plus arbiter, razem około 7-8 mln tokenów wejścia; wyjście około 50-60 tys. tokenów. Z buforowaniem (cache) stałej części (pakiet, karta, dotychczasowy wątek) większość wejścia to tanie odczyty z bufora: około 0,5 mln tokenów zapisu do bufora i 6-7 mln odczytów.

Przykład liczbowy przy założeniu cennika 5$ za mln tokenów wejścia, 25$ za mln wyjścia i odczytu z bufora za 10% ceny wejścia (założenie do sprawdzenia): bez bufora około 40$, z buforem około 10-15$ za przebieg. Przy cenniku trzykrotnie wyższym: odpowiednio około 115$ i 35-45$. Wniosek: dziewięć przebiegów W1 to przy niższym cenniku z buforem 90-135$, czyli limit 100$ mieści je tylko przy dolnej granicy szacunku; przy wyższym cenniku w limicie mieszczą się 2-3 przebiegi. Dlatego plan 9 przebiegów jest celem, a nie zobowiązaniem: po przebiegu 1 koszt mierzony z pola `usage` zastępuje ten szacunek, a liczba przebiegów 2-12 jest ustalana na nowo. Dźwignie oszczędności w kolejności: buforowanie, krótsze pakiety (tylko to, co postać musi znać), limit 300 tokenów na wypowiedź, mniej rund (6 zamiast 8), składy W4 i W3.

## 5. Luki w repozytorium, które utrudnią karty postaci

Karta ma mieć: kim postać jest i jakie ma narzędzia, ile głosów, czerwone linie, co zyskuje bez porozumienia, przed kim odpowiada. Dla każdej postaci brakuje:

1. **Kaczyński i PiS.** Brak zapisu funkcji partyjnej, brak oficjalnego stanowiska PiS wobec resetu ("Oficjalnego stanowiska PiS nie znaleźliśmy", `badania/scenariusze-naprawy.md`), brak wypowiedzi Kaczyńskiego o ślubowaniu i ustawie 3/5 poza wezwaniem do oporu z 2026.09.29 [media x1]. Brak opisu relacji PiS i Rozwoju Plus (kiedy i dlaczego klub Morawieckiego się oddzielił; w głosowaniu z 2026.09.04 oba kluby głosowały tak samo).
2. **Nawrocki.** Brak ustalenia, czy aprobuje plany Konfederacji i Rozwoju Plus (Kancelaria nie potwierdziła); brak dokumentu Kancelarii o "restarcie" z wypowiedzi Boguckiego [media x1]; brak stanowiska wobec wyroków ETPC i TSUE; brak informacji, czy prace Rady Nowej Konstytucji obejmują TK; brak odpowiedzi na propozycję spotkania "w cztery oczy"; nie ustalono, czy doszło do przesłuchania Prezydenta jako świadka.
3. **Tusk i rząd.** Brak odpowiedzi rządu na żądanie z RBN; brak własnej propozycji treści zmian; stanowisko o ustawie z wyborem 3/5 tylko od posła Tomczykiewicza [media x1]. Liczba nieopublikowanych wyroków TK jest znana (85 z lat 2024-2026: 22, 41, 22, według wykazu na stronie TK, `badania/skutki-dla-obywateli.md`), ale treści wykazu w repozytorium nie ma, więc karta nie powie, których spraw to dotyczy.
4. **Kosiniak-Kamysz i PSL.** Brak zapisu jego funkcji w rządzie (Płaczek mówi o "wicepremierze" na RBN, bez nazwiska); plan PSL milczy o ślubowaniu, kierownictwie TK, sędziach z 2026 roku i dawnych wyrokach; wariant "wygaszenia TK" Pasławskiej tylko [media x1]; brak informacji, jak PSL głosowałoby przy wotum nieufności.
5. **Czarzasty i Lewica.** Stanowisko tylko z mediów [media x2-x3]; brak stanowiska klubu wobec ustawy 3/5; brak stanowiska Lewicy wobec resetu poza cytatem Czarzastego; nieobecność Lewicy na konsultacjach u Prezydenta bez wyjaśnienia [media x1].
6. **Hołownia i Polska 2050.** Jedna wypowiedź [media x2]; nie wiadomo, kto kieruje partią po 2026.10.24; brak stanowiska wobec ślubowania i wotum nieufności.
7. **Centrum.** Brak nazwiska lidera i jakiegokolwiek stanowiska; znany tylko sposób głosowania w 2026 roku i nieobecność na konsultacjach 2026.10.31 [media x1].
8. **Bosak, Mentzen i Konfederacja.** "Konkretny pomysł" z 2026.11.03 nieznany; wpisy Mentzena na X nieodczytane bezpośrednio; liczba 46 posłów do losowania tylko z mediów; relacja Konfederacji z PiS i z Prezydentem nieopisana.
9. **Morawiecki i Rozwój Plus.** Projekt jest [dok], ale nie wiadomo, czy obejmuje stanem spoczynku sędziów z 2026 roku; brak stanowiska wobec ślubowania (jest tylko Szczuckiego [media x1]); druku w Sejmie nie znaleziono; brak informacji o historii klubu; nazwisk autorów projektu karta nie podaje.
10. **Święczkowski i sędziowie sprzed 2026 roku.** Brak dat końca kadencji wszystkich piętnaściorga sędziów (jest tylko Wyrembak 2027.01.30); brak informacji, kiedy kończy się kadencja Święczkowskiego jako sędziego (wybrany 2022.02.08) i jako Prezesa; brak jego wypowiedzi o warunkach, na jakich przyjąłby stan spoczynku albo rezygnację; brak komunikatu TK po wyroku TSUE; nieznany termin rozprawy w Kpt 1/26; nie wiadomo, czy w grupie siedmiorga są różnice wobec porozumienia (zdania odrębne wskazują, że grupa nie jest jednolita).
11. **Korwin-Piotrowska i sędziowie z 2026 roku.** "Stanowiska wobec scenariuszy nie znaleźliśmy" (`badania/scenariusze-naprawy.md`); odmowa orzekania przez Patyrę tylko [media x2]; przebieg zgromadzenia z 2026.11.03 tylko z mediów, bez protokołu; nie wiadomo, czy ośmioro działa wspólnie, czy pod przewodem jednej osoby; długość aplikacji Korwin-Piotrowskiej (od niej zależy, kto ma najdłuższy staż); brak stanowiska wobec resetu, który oznaczałby także ich odejście (Batory daje im prawo ponownego kandydowania, KJ nie).
12. **Wspólne dla wszystkich kart "przed kim odpowiada".** Repozytorium nie opisuje struktur partyjnych (kto w partii decyduje), sondaży ani nastrojów wyborców; dla wariantu (c) "czysty interes polityczny" brak jakiejkolwiek miary opłacalności. Brak terminu wyborów 2027 poza "jesienią".
13. **Wspólne dla "co zyskuje bez porozumienia".** Brak dat końca kadencji sędziów i brak opisu, co stanie się z budżetem TK na 2027 rok, jeśli Sejm nie uchwali części dla TK (dźwignia z art. 225); brak listy spraw zawieszonych w TK i skutków dla obywateli za 2025-2026 (`plan.md`, zadanie 3).
14. **Prawo.** Nierozstrzygnięte, czy Prezydent może skierować zmianę Konstytucji do TK; pełnej opinii Komisji Weneckiej z 2026.10.13 nie odczytano; poprawek Senatu z 2024.07.31 nie odczytano; treści zarządzenia Prezesa SN z 2026.11.02 nie odczytano.
15. **Materiał z #45.** Issue wymienia materiał z #45 dla etapu 2; w repozytorium w wersji 78e9e45 nie ma pliku ani odsyłacza do #45, więc etap 2 musi go dostać osobno.
16. **Granica pakietu wiedzy.** Część "Scenariusze z analiz AI" w `badania/scenariusze-naprawy.md` (m.in. kompromis pakietowy, wąska zmiana Konstytucji, dobrowolne odejścia, Trybunał Stanu, referendum) jest wyłączona z pakietu przez issue. Etap 2 musi oddzielić z tego pliku fakty (progi, stan spraw) od listy scenariuszy, bo są w jednym dokumencie.

## Zapis pracy

Przeczytane pliki: `README.md`, `AGENTS.md`, `plan.md`, `analizy.md`, `metodologia.md` (początek), `historia-sporu.md` (część od 2015), `badania/sily-i-glosy.md`, `badania/warunki-rozwiazan.md`, `badania/scenariusze-naprawy.md`, `badania/propozycje-na-stole.md`, `badania/okres-2024-2026.md`, `badania/zgromadzenie-2026-11-03.md`, `badania/postepowania-wobec-osob.md` (cz. 1-4), `badania/wyroki-europejskie.md` (fragmenty), `badania/skutki-dla-obywateli.md` (początek i dane TK 2024-2026), `badania/materialy-do-sprawdzenia.md`, `zrodla/konstytucja.md` (art. 98, 120-122, 125, 135, 144, 145, 154, 155, 158, 190, 191, 194, 195, 197, 225, 235), `zrodla/glosowania-tk-2015-2026.md` (głosowania z 2024-2026) oraz karty z `zrodla/okres-2024-2026/`: rbn-2026-11-03, premier-2026-11-03, psl-reset-2026-11-03, senat-sklad-2026-11, komunikat-31-pazdziernika, zarzadzenie-przerwy-2026, zandberg-po-rbn-2026-11-03, konfederacja-po-rbn-2026-11-03, konfederacja-reset-2026-10-31, kj-29-warunkow, hfpc-zarzad-2026-10-31, rozwoj-plus-trybunal-2026 (początek), druk-166-2015 (początek), etpc-17392-26, kpt-1-26, uchwala-sejmu-2026-299. Pliki wyłączone poleceniem nie były otwierane. W rundzie poprawek dodatkowo odczytano z repozytorium zdania o konsultacjach 2026.10.31 (`badania/scenariusze-naprawy.md`) i o nieopublikowanych wyrokach (`badania/skutki-dla-obywateli.md`).

Agent-Role: wykonawca etapu 1 (issue #46). Agent-Model: claude-fable-5-1 (Claude Fable 5.1). Agent-Run: niepotwierdzony.

## Zmiany po recenzji (runda 1)

Blokery:

- **B1 (inicjatywa zmiany Konstytucji): poprawione.** Usunąłem "Rozwój Plus z Konfederacją (57)" i dopisałem, że 57 nie wystarcza; wymieniłem podmioty, które próg 92 spełniają.
- **B2 (PSL i wotum nieufności): poprawione.** Przeliczyłem: przy samej opozycji prawicowej 231 domykają KO, PSL i Lewica (dokładnie 231), a z Razem i niezrzeszonymi każdy klub koalicji; zmieniłem wiersz F, zdanie "Niezbędni" i pkt 5 oraz 6 składu.
- **B3 (PSL a 307 z PiS): poprawione.** W tabeli podsumowania PSL w kolumnie C to teraz "niezbędny bez PiS (nie)"; to samo rozpisałem dla pozostałych klubów koalicji.
- **B4 (niezbędność w ścieżce B i reguły arbitra): poprawione.** Ścieżka B ma teraz listę założeń z rachunkiem dla każdego; tabela podsumowania podaje założenia w nagłówku i wartości w nawiasach dla wariantu alternatywnego, także w kolumnie A (235 z Razem i niezrzeszonymi); reguły arbitra nie zakładają z góry niezbędności, tylko sumują głosy obecnych klubów, z przykładami.
- **B5 (kto głosował w 2024-2026): poprawione.** Ścieżka E rozpisuje głosowania zgodnie z kartą: 2024.03.06 bez Centrum, G1 Razem nieobecne, G2-G3 Razem wstrzymało się, G4 Razem "przeciw wszystkim".
- **B6 (konsultacje 2026.10.31): poprawione.** W2 podaje, że nie uczestniczyły Lewica i Centrum [media x1], a o KO tylko zapowiedź nieobecności według TVP Info [media x1]; dodałem zasadę liczenia Centrum w W2.

Uwagi nieblokujące:

- **1 (koszt 9 przebiegów): poprawione.** Napisałem wprost, że 9 przebiegów to 90-135$ przy niższym cenniku i mieści się w 100$ tylko przy dolnej granicy.
- **2 (Centrum w W2): poprawione.** W W2 Centrum liczy się jako niedostępne, co uzasadniam brakiem przedstawiciela i nieobecnością na konsultacjach; rachunek 231 w W2 przeliczony.
- **3 (scenariusze AI w ścieżce G i W3): poprawione.** Dodałem ostrzeżenia dla etapu 2 w ścieżce G, w W3 i jako lukę 16; W3 nie podsuwa postaciom pomysłu dobrowolnych odejść.
- **4 (Żurek): zostawione z uzupełnieniem.** Żurek nadal poza stołem, bo odpowiada przed premierem, ale arbiter oznacza obietnice co do prokuratury jako "poza gwarancją stołu", a tabela pominięć przewiduje dodanie go, jeśli przebieg 1 pokaże blokadę.
- **5 (Szczucki): poprawione.** "Współautor" zamieniłem na "współprezentujący" z zastrzeżeniem, że karta nie podaje nazwisk autorów.
- **6 (nieopublikowane wyroki): poprawione.** Luka 3 i tabela D podają liczbę 85 (22, 41, 22) z `badania/skutki-dla-obywateli.md` i zaznaczają, że brakuje tylko treści wykazu.
- **7 (historia-prac.md, sumy i stały link): zostawione, poza zakresem.** Dotyczy pliku prowadzonego przez koordynatora, nie dokumentu etapu 1; przekazuję uwagę do wykonania przy publikacji.
- **8 (puste miejsce w Senacie): poprawione.** Dopisałem puste miejsce po Mirosławie Różańskim we wstępie, w ścieżce C i w regułach arbitra.

## Zmiany po recenzji (runda 2)

Blokery:

- **R2-B1 (brakujące głosy w ścieżce C bez PiS): poprawione.** Koalicja, Rozwój Plus i Konfederacja to 296, więc brakuje 11 z 17 głosów Razem, Korony, Demokracji Bezpośredniej i niezrzeszonych (np. Razem i 7 z 13); poprawiłem zdanie w ścieżce C i wiersz tabeli podsumowania.
- **R2-B2 (W2, Kukiz policzony podwójnie): poprawione.** 207 już zawiera Demokrację Bezpośrednią, więc z Polską 2050 i Razem jest 226, a z Koroną 229, w obu wypadkach za mało; przepisałem zasady arbitra w W2, wniosek o PSL bez zmian.
- **R2-B3 (ścieżka F, "opozycja prawicowa w komplecie"): poprawione.** Niezbędni zawsze PiS i Rozwój Plus (bez PiS 63, bez Rozwoju Plus 170); Konfederacja tylko przy samym PSL albo samej Lewicy bez Razem i niezrzeszonych; Korona i Demokracja Bezpośrednia tylko w wariancie z samą Lewicą; kolejność liczb w nawiasie poprawiona.

Uwagi nieblokujące:

- **1 (KO jako klub domykający wotum przeciw własnemu premierowi): poprawione.** W ścieżce F, w tabeli (wiersz KO, kolumna F) i w pkt 5 składu zaznaczyłem, że to tylko rachunek, i w pkt 5 pominąłem KO.
- **2 (Tusk, "bez którego nie ma 231"): poprawione.** Dopisałem założenie: przy samej koalicji (83), a 307 zawsze (304).
- **3 (G1 i G4, niezrzeszeni): poprawione.** Dopisałem 2 niezrzeszonych przeciw w G1 i 1 niezrzeszonego za Kotowskim w G4.
- **4 (stały link w historia-prac.md): zostawione, poza zakresem.** To plik koordynatora.
