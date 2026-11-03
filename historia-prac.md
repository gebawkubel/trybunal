# Historia prac

Ten plik opisuje, jak powstały wyniki projektu: kto co zrobił, w jakiej kolejności, jakie błędy znaleźli recenzenci i co poprawiliśmy. Same wyniki są w [README](README.md).

Każda zmiana w repozytorium przechodzi przez PR (propozycję zmiany na GitHubie). Osobny agent AI recenzuje ją i wydaje wynik PASS albo wskazuje blokery. Raport recenzenta jest publikowany jako komentarz przy PR. Commity podają rolę i model agenta w polach Agent-Role, Agent-Model i Agent-Run. To zapis deklaracji, nie dowód, który model faktycznie pracował.

## Ustalenia

- 2026.11.02: projekt prowadzi GWK. Zaczynamy od sporu o pięć miejsc w TK w 2015 roku.
- 2026.11.02: piszemy krótko, zwykłym językiem. Terminy techniczne wyjaśniamy przy pierwszym użyciu. Nie tworzymy dokumentów ani pól na zapas.
- 2026.11.02: pierwsza wersja organizacyjna jest dopracowywana przed badaniami. Na życzenie założyciela zastępujemy jej pierwszy commit przez force push, czyli podmianę historii gałęzi. Późniejsze analizy i ich korekty mają zachowywać historię.
- 2026.11.02: model planowany do analiz to gpt-6-astra-medium. Dokumentację organizacyjną przygotowano z pomocą Codex.
- 2026.11.03: pełny zakres: geneza sporu i wszystkie późniejsze wydarzenia aż do aktualnego stanu. Moduł 2015 jest punktem wyjścia, nie ograniczeniem badań. Przeglądy okresów wskazują także luki; nie są zakończonymi ocenami odpowiedzialności.
- 2026.11.03: źródło zapisujemy jako jedną kopię MD z adresem oryginału, bez plików PDF i HTML.
- 2026.11.03: zapis przebiegu prac trzymamy w tym jednym pliku. Pełne pierwsze wersje analiz i recenzji są w historii repozytorium, pod stałymi linkami podanymi niżej.

## Chronologia zmian

| PR | Data | Co | Recenzja |
|---|---|---|---|
| [#4](https://github.com/gebawkubel/trybunal/pull/4) | 2026.11.03 | Pięć miejsc w TK: pierwsze źródła i oś czasu | PASS |
| [#5](https://github.com/gebawkubel/trybunal/pull/5), [#6](https://github.com/gebawkubel/trybunal/pull/6) | 2026.11.03 | Zasady recenzji i scalania | PASS |
| [#7](https://github.com/gebawkubel/trybunal/pull/7) | 2026.11.03 | Dokumenty z 2015 roku: ustawy, uchwały, druki | PASS |
| [#8](https://github.com/gebawkubel/trybunal/pull/8), [#9](https://github.com/gebawkubel/trybunal/pull/9) | 2026.11.03 | Pięć miejsc: skutki K 34/15, głosowania, ślubowania, droga art. 137 | PASS |
| [#10](https://github.com/gebawkubel/trybunal/pull/10) | 2026.11.03 | [Lista scenariuszy naprawy TK](badania/scenariusze-naprawy.md) | dwie rundy blokerów, potem PASS |
| [#11](https://github.com/gebawkubel/trybunal/pull/11) | 2026.11.03 | Źródła bez duplikatów: usunięte PDF i HTML | PASS |
| [#13](https://github.com/gebawkubel/trybunal/pull/13), [#14](https://github.com/gebawkubel/trybunal/pull/14) | 2026.11.03 | Przeglądy okresów 2016-2026 i poprawki po recenzji | PASS |
| [#15](https://github.com/gebawkubel/trybunal/pull/15), [#16](https://github.com/gebawkubel/trybunal/pull/16) | 2026.11.03 | Lata 2024-2026, kierownictwo TK w 2016 roku | PASS po 2 i 3 rundach |
| [#17](https://github.com/gebawkubel/trybunal/pull/17) | 2026.11.03 | Lista scenariuszy po Zgromadzeniach Ogólnych TK i SN | 7 blokerów (oznaczenia źródeł, przypisania), potem PASS |
| [#18](https://github.com/gebawkubel/trybunal/pull/18) | 2026.11.03 | Chronologia 2026.11.03 w dokumentach | PASS |
| [#19](https://github.com/gebawkubel/trybunal/pull/19) | 2026.11.03 | Źródła pierwotne KPRP, KPRM, Kolegium SN i komunikat TK w liście scenariuszy | PASS, poprawki po uwagach |
| [#20](https://github.com/gebawkubel/trybunal/pull/20) | 2026.11.03 | [Czy Zgromadzenie Ogólne TK było ważne](badania/zgromadzenie-2026-11-03.md) | 3 blokery, potem PASS |
| [#21](https://github.com/gebawkubel/trybunal/pull/21) | 2026.11.03 | Tabela scenariuszy z analiz AI po Zgromadzeniu | PASS, poprawki po uwagach |
| [#22](https://github.com/gebawkubel/trybunal/pull/22) | 2026.11.03 | Staż sędziów, budżet TK, art. 11 ust. 3 i 5 | 2 blokery, potem PASS |
| [#23](https://github.com/gebawkubel/trybunal/pull/23) | 2026.11.03 | Porządek: jedna historia prac, nowe README | PASS |
| [#24](https://github.com/gebawkubel/trybunal/pull/24) | 2026.11.03 | [Spór o kadencję prezes TK](badania/kadencja-prezes-2022-2023.md) | 2 blokery, potem 1, potem PASS |
| [#25](https://github.com/gebawkubel/trybunal/pull/25) | 2026.11.03 | [Opóźniona publikacja wyroków](badania/publikacja-wyrokow.md) | PASS, poprawki po uwagach |
| [#26](https://github.com/gebawkubel/trybunal/pull/26) | 2026.11.03 | [Wyroki ETPC i TSUE o TK](badania/wyroki-europejskie.md) | PASS, poprawki po uwagach |
| [#27](https://github.com/gebawkubel/trybunal/pull/27) | 2026.11.03 | [Geneza: TK przed 2015 rokiem](badania/geneza-przed-2015.md) | 1 bloker, potem PASS |
| [#28](https://github.com/gebawkubel/trybunal/pull/28) | 2026.11.03 | [Lata 2020-2023: składy, zdania odrębne, statystyki](badania/okres-2020-2023-uzupelnienie.md) | PASS, poprawki po uwagach |
| [#29](https://github.com/gebawkubel/trybunal/pull/29) | 2026.11.03 | [Dopuszczenie sędziów do orzekania](badania/piec-miejsc.md#dopuszczenie-do-orzekania) | 2 blokery, potem PASS |

Numery #1 i #12 to zgłoszenia zadań, a PR #2 i #3 z 2026.11.02 zamknięto bez scalenia. Pierwszą wersję organizacyjną przygotowano z pomocą Codex. PR #13-#16 i #18 powstały równolegle do pozostałych prac. Model podano w commitach.

## Lista scenariuszy naprawy (PR #10, #17, #19, #21)

Prowadzący: Claude Code, model claude-opus-5-5. Wszyscy agenci pracowali z wyszukiwaniem w sieci, każdy w osobnym kontekście, bez dostępu do repozytorium. Każdy etap wykonano raz. Identyfikatory przebiegów agentów nie są publicznie weryfikowalne, więc ich nie podajemy.

| Etap | Wykonawca | Wynik |
|---|---|---|
| Polecenie katalogu stanowisk | prowadzący | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/polecenie-katalog.md) |
| Dwa katalogi stanowisk: koalicja i Prezydent, opozycja i instytucje | dwa agenty, model Sonnet (wersja niepotwierdzona) | [commit c0d4f4e](https://github.com/gebawkubel/trybunal/tree/c0d4f4e/badania/scenariusze-przebieg) |
| Polecenie analiz scenariuszy | prowadzący | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/polecenie-scenariusze.md) |
| Analiza A | agent, claude-fable-5-1 (według deklaracji modelu) | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/analiza-a.md) |
| Analiza B | agent, claude-opus-5-5 (według deklaracji modelu) | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/analiza-b.md) |
| Recenzja analizy A | agent, claude-opus-5-5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/recenzja-analizy-a.md) |
| Recenzja analizy B | agent, claude-fable-5-1 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/recenzja-analizy-b.md) |
| Weryfikacja faktów: 69 twierdzeń ze źródłami | agent, claude-opus-5-5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/fakty-zweryfikowane.md) |
| Weryfikacja stanowisk | agent, model Sonnet (wersja niepotwierdzona) | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/scenariusze-przebieg/stanowiska-zweryfikowane.md) |

Analizy powstały rano 2026.11.03, przed Zgromadzeniami Ogólnymi. Sumy SHA-256 pierwszych wersji zapisaliśmy przed recenzjami:

```
67d63d47f338af684ce218a786cef6c32fa6d38168e3c4c0d3d704c0392f5269  analiza-a.md
9b61393a32d92294f6889fb61593a7eece410a2e59a19e85fb2b4ac383a0782b  analiza-b.md
c68bf8e9b85e598494e27d74772d6e1fee826046faf8d973ef6ea78ab9482d98  katalog-koalicja-prezydent.md
a88a895ebc33173284b73e2d0881f4d27f19ea7812384ec308a8a419df4086e7  katalog-opozycja-instytucje.md
f52aad4f48a447de551610419a542ab1ca09350a97733964cf2074b23e5aed59  polecenie-scenariusze.md
```

**Co znaleźli weryfikatorzy.** Katalogi i analizy miały błędy, których nie przenieśliśmy do listy. Przykłady:
- nieaktualna liczebność klubów: PiS 188 zamiast 147 i pominięty klub Rozwój Plus,
- błędne daty: powołanie Prezesa Święczkowskiego, skierowanie ustaw z 2024 roku do TK, powołanie Rady Nowej Konstytucji,
- wyrok K 3/26 pomylony ze sporem kompetencyjnym Kpt 1/26,
- ślubowanie w Sejmie przypisane czworgu zamiast sześciorgu sędziów,
- błędne przypisania stanowisk: m.in. "brak stanowiska PiS wobec resetu", choć wypowiadał się poseł Wójcik, plan Szczuckiego przypisany Morawieckiemu, HFPC opisana jako zwolenniczka poprawy trybu bez zmiany składu, choć popiera reset z wygaszeniem kadencji.

Pełne listy są w sekcji 2 weryfikacji faktów i w części "Błędy w katalogach" weryfikacji stanowisk. W liście korzystaliśmy z wersji zweryfikowanych.

**Aktualizacje z wieczora 2026.11.03.** Wyniki Zgromadzeń Ogólnych TK i SN oraz posiedzenia RBN zebrał agent z modelem Sonnet przez wyszukiwarkę (PR #17). Pierwsza recenzja znalazła 7 błędów, głównie zawyżone oznaczenia liczby źródeł i dwa stanowiska przypisane bez podstawy (Konfederacji i Kukizowi). W PR #19 część relacji mediów zastąpiliśmy dokumentami stron, a przy okazji poprawiliśmy termin Prezydenta: nie jest to data 2026.11.11, tylko "przed rozpoczęciem tygodnia" obchodów Święta Niepodległości. Cytatów z relacji nie przenosiliśmy bez porównania ze źródłem.

## Notatka o Zgromadzeniu Ogólnym TK (PR #20, #22)

| Etap | Wykonawca | Wynik |
|---|---|---|
| Polecenie | prowadzący, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/polecenie.md) |
| Analiza A | agent, Claude Fable 5.1 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/analiza-a.md) |
| Analiza B | agent, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/analiza-b.md) |
| Recenzja analizy A | agent, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/recenzja-analizy-a.md) |
| Recenzja analizy B | agent, Claude Fable 5.1 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/recenzja-analizy-b.md) |
| Staż sędziów z art. 11 ust. 2 | agent, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/2d831a9acef1db7ea9c0aa9882b8ca5b01b1e28d/badania/zgromadzenie-przebieg/staz-sedziow.md) |
| Stan budżetu TK na 2027 rok | agent, model Sonnet (wersja niepotwierdzona) | wyniki weszły do notatki tylko ze źródłami |

Analizy powstały osobno, bez wglądu w drugą. Każdy etap wykonano raz. Polecenie powstało pod nazwą `polecenie-analiza.md`, stąd ta nazwa w recenzjach. Polecenie opierało się na relacjach mediów z przebiegu Zgromadzenia. Sumy SHA-256 zapisane przed recenzjami:

```
fe2acc61efb8677f12a3ac6760b980f13bd1274100871c9575998753d112fb27  polecenie.md
f01e7caa1b57dde5650c825a1be052d64f33557d9c7826682bdfb59e49a63fb2  analiza-a.md
0d4176f390bca52a441c8fdc8fd8d07bc890c7bc81722fba820d28583354e28f  analiza-b.md
```

Przed publikacją usunęliśmy z analizy A i recenzji analizy A lokalny przedrostek ścieżek do plików repo. Suma analizy A po tej zmianie: `fa41ecf722700749d412f372b188d81c1d6a99b98cb612d9547246661d53ebdf`. Wersja pierwotna, zgodna z sumą sprzed recenzji, jest w [commicie 13358fa](https://github.com/gebawkubel/trybunal/blob/13358fafa93655087f2f78c3cc5588fb13d047c3/badania/zgromadzenie-przebieg/analiza-a.md). W wyliczeniu stażu zamieniliśmy tylko lokalną ścieżkę na słowa "katalog roboczy agenta". Suma przed zmianą: `34b1e784f12eeed3c9b1668d148fa4f84b4887061e9e0442e7e7d2275a256e34`. Wersji sprzed zmiany nie ma w repozytorium, więc tej sumy nie da się sprawdzić.

**Co znaleźli recenzenci.**
- Analiza A pominęła uchwałę Sejmu z 2026.03.13. Jej pkt 3 daje stronie zwołującej argument, że stanowisko Prezesa w praktyce jest nieobsadzone. Analiza A pomyliła też daty i opisy orzeczeń.
- Analiza B źle zrekonstruowała podstawę przerwy w czynnościach Prezesa. Pominęła też termin 7 dni na zawiadomienie i stan budżetu TK.
- Recenzent notatki (PR #20) zauważył, że wniosek przypisywał wyrokom K 1/17 i K 3/26 więcej, niż w nich jest, i że części faktów brakowało źródeł.
- Recenzent PR #22 wskazał, że wyliczenie stażu zakładało ciągłą pracę od początku aplikacji, czego życiorys nie potwierdza. Wiersz Piotrowicza w wyliczeniu opiera się częściowo na pamięci modelu, co nie wpływa na wynik.

Brzmienie przepisów cytowanych w notatce prowadzący sprawdził osobno w ELI. Życiorys z druku 2333, biogram Sycha i uzasadnienie druku 3150 też sprawdził sam.

## Badania z późnego wieczora 2026.11.03 (PR #24-#29)

Każde badanie wykonał osobny agent w osobnej kopii repozytorium, z wyszukiwaniem w sieci. Agent pisał notatkę i karty źródeł oraz robił commit, a prowadzący (Claude Opus 5.5) wypychał gałąź, otwierał PR i zlecał recenzję innemu agentowi.

| PR | Badanie | Wykonawca | Recenzent | Co poprawił recenzent |
|---|---|---|---|---|
| #24 | kadencja prezes | agent, claude-opus-5-5 | agent, claude-fable-5-1 | błędny opis prawa obowiązującego w dniu powołania prezes, zdanie przypisane źródłu bez pokrycia |
| #25 | publikacja wyroków | agent, claude-opus-5-5 | agent, claude-fable-5-1 | wykładnia rządu podana jako fakt, nie dosłowne cytaty, funkcja świadka |
| #26 | wyroki europejskie | agent, claude-opus-5-5 | agent, claude-fable-5-1 | wniosek autora podany jako ustalenie SN, liczba wyników bez filtrów |
| #27 | geneza przed 2015 | agent, claude-opus-5-5 | agent, claude-fable-5-1 | fałszywe twierdzenie, że API Sejmu nie podaje głosów przy głosowaniu listą |
| #28 | lata 2020-2023 | agent, claude-opus-5-5 | agent, claude-fable-5-1 | przypisanie dat i liczb do źródła, duplikat karty z PR #26 usunięty przed recenzją |
| #29 | dopuszczenie 2015-2016 | agent, model Sonnet (wersja niepotwierdzona) | agent, claude-opus-5-5 | treść dokumentu opisana błędnie, wniosek o podstawie prawnej podany jako fakt |

Przy scalaniu gałęzi kolejnych badań konflikty w `zrodla/manifest.json` rozwiązywaliśmy przez połączenie wpisów i przeliczenie sum. Od PR #28 każdy plik w `zrodla/` ma wpis w manifeście.

## Ocena odpowiedzialności i rozwiązań (PR #31)

Wynik: [notatka o odpowiedzialności i rozwiązaniach](badania/odpowiedzialnosc-i-rozwiazania.md). Analizy oparto wyłącznie na materiale repozytorium (stan main po PR #30), bez nowego szukania w sieci.

| Etap | Wykonawca | Plik |
|---|---|---|
| Polecenie | prowadzący, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/95f069df462372e29e5237e8293e56da466df97e/badania/ocena-przebieg/polecenie.md) |
| Analiza A | agent, Claude Fable 5.1 | [plik](https://github.com/gebawkubel/trybunal/blob/95f069df462372e29e5237e8293e56da466df97e/badania/ocena-przebieg/analiza-a.md) |
| Analiza B | agent, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/95f069df462372e29e5237e8293e56da466df97e/badania/ocena-przebieg/analiza-b.md) |
| Recenzja analizy A | agent, Claude Opus 5.5 | [plik](https://github.com/gebawkubel/trybunal/blob/95f069df462372e29e5237e8293e56da466df97e/badania/ocena-przebieg/recenzja-analizy-a.md) |
| Recenzja analizy B | agent, Claude Fable 5.1 | [plik](https://github.com/gebawkubel/trybunal/blob/95f069df462372e29e5237e8293e56da466df97e/badania/ocena-przebieg/recenzja-analizy-b.md) |

Analizy powstały osobno, każdy etap raz. Sumy SHA-256 zapisane przed recenzjami:

```
58cd0def352290bdc018f78d1d71f18be36862f4f24c60b459f283a14fad703c  polecenie.md
906875e03176d724031989a8ade4908d3ec0c446af4a161cbe55344809f23587  analiza-a.md
3d5b146a5de594bede318464cde2c0bfb5cce3b036caf6792e77589b0ca07f10  analiza-b.md
```

W poleceniu przed publikacją zamieniliśmy lokalną ścieżkę repozytorium na słowo "publiczne". Suma po tej zmianie: `bbae260db457f18022177ed85c5adea26741d97707e2214c36bad6a7930b06ad`. W recenzjach zamieniono w ten sam sposób ścieżki katalogu roboczego.

**Co znaleźli recenzenci.**
- W obu analizach błędna data ślubowania czworga sędziów z 2015 roku (było 2015.12.03, tego samego dnia co K 34/15).
- W analizie A:
  - zwrot "sententia non existens" przypisany K 6/21 zamiast postanowieniu w P 7/20,
  - błędna dominacja referendum,
  - tabela, w której przy dwóch działaniach zamiast obrony podano zarzuty,
  - wymuszone symetrie.
- W analizie B:
  - przepis o ślubowaniu wskazany jako art. 6 ust. 1 zamiast art. 4 ust. 1 ustawy o statusie sędziów TK,
  - wnioski części 1 bez orzeczeń TK niekorzystnych dla obecnej większości (U 5/24, K 3/26),
  - nieuzasadnione dominacje dwóch wariantów.

Notatka przyjmuje tylko dominacje wskazane przez obie analizy, a zastrzeżenia recenzentów do nich podaje wprost. Recenzent notatki (PR #31) wskazał dodatkowo nierówną ocenę wykonalności wariantów 1 i 2, pominięcie wyroków K 34/15 i K 35/15 we wnioskach, brak dwóch scenariuszy i kilka nieścisłości. Wszystko poprawiliśmy. W drugiej rundzie recenzent wskazał jeszcze, że wyrok K 35/15 dotyczył przepisu uchwalonego przez większość PiS, a nie PO-PSL. W trzeciej rundzie poprawiliśmy opis art. 137a: dotyczył terminu zgłaszania kandydatów, nie kadencji. Wszystko poprawiliśmy przed scaleniem.

Recenzje odwołują się do plików w katalogu roboczym `ocena/`. W repozytorium leżały w `badania/ocena-przebieg/`. Sumy opublikowanych recenzji, już po zamianie ścieżek (sum sprzed zamiany nie zapisaliśmy):

```
d2d83f539630cb25b7d7c4668919ff5bfdef7c4fae49ddcfbdcddc0639f36b39  recenzja-analizy-a.md
f6842c46b86e87494bf4d55be1875e740ac25851a84df21f2e711e9e4cfc5929  recenzja-analizy-b.md
```
