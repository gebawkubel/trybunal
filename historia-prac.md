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
| [#30](https://github.com/gebawkubel/trybunal/pull/30) | 2026.11.03 | Porządek po badaniach #24-#29 | PASS |
| [#31](https://github.com/gebawkubel/trybunal/pull/31) | 2026.11.03 | [Kto odpowiada za kryzys i które rozwiązania są lepsze](badania/odpowiedzialnosc-i-rozwiazania.md) | 3 rundy blokerów, potem PASS |
| [#32](https://github.com/gebawkubel/trybunal/pull/32) | 2026.11.03 | [Konfederacja po posiedzeniu RBN](zrodla/okres-2024-2026/konfederacja-po-rbn-2026-11-03.md), [Zandberg po spotkaniu u Prezydenta](zrodla/okres-2024-2026/zandberg-po-spotkaniu-2026-10-31.md) i [Zandberg po RBN](zrodla/okres-2024-2026/zandberg-po-rbn-2026-11-03.md): napisy nagrań WP od użytkownika i transkrypcja maszynowa nagrania Razem | 1 bloker, potem PASS |
| [#33](https://github.com/gebawkubel/trybunal/pull/33) | 2026.11.03 | Walidator pomija katalogi robocze agentów (.claude) | PASS |
| [#34](https://github.com/gebawkubel/trybunal/pull/34) | 2026.11.03 | [Warunki rozwiązań](badania/warunki-rozwiazan.md): Senat, art. 235, wyroki, projekty, Komisja Wenecka | 1 bloker, potem PASS |
| [#35](https://github.com/gebawkubel/trybunal/pull/35) | 2026.11.03 | [Skutki dla obywateli](badania/skutki-dla-obywateli.md) | 2 blokery, potem PASS |
| [#36](https://github.com/gebawkubel/trybunal/pull/36) | 2026.11.03 | [Postępowania wobec osób](badania/postepowania-wobec-osob.md) | PASS, poprawki po uwagach |
| [#37](https://github.com/gebawkubel/trybunal/pull/37) | 2026.11.03 | Porządek po badaniach #34-#36: korekta oceny, README, plan | w toku |

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

Notatka przyjmuje tylko dominacje wskazane przez obie analizy, a zastrzeżenia recenzentów do nich podaje wprost. Recenzent notatki (PR #31) wskazał dodatkowo nierówną ocenę wykonalności wariantów 1 i 2, pominięcie wyroków K 34/15 i K 35/15 we wnioskach, brak dwóch scenariuszy i kilka nieścisłości. Poprawiliśmy to. W drugiej rundzie recenzent wskazał jeszcze, że wyrok K 35/15 dotyczył przepisu uchwalonego przez większość PiS, a nie PO-PSL. W trzeciej rundzie poprawiliśmy opis art. 137a: dotyczył terminu zgłaszania kandydatów, nie kadencji. Wszystko poprawiliśmy przed scaleniem.

Recenzje odwołują się do plików w katalogu roboczym `ocena/`. W repozytorium leżały w `badania/ocena-przebieg/`. Sumy opublikowanych recenzji, już po zamianie ścieżek (sum sprzed zamiany nie zapisaliśmy):

```
d2d83f539630cb25b7d7c4668919ff5bfdef7c4fae49ddcfbdcddc0639f36b39  recenzja-analizy-a.md
f6842c46b86e87494bf4d55be1875e740ac25851a84df21f2e711e9e4cfc5929  recenzja-analizy-b.md
```

## Badania luk z oceny (PR #32-#36)

**Wypowiedzi polityków (PR #32).** Użytkownik przekazał napisy do dwóch nagrań Wirtualnej Polski (Bosak i Płaczek po RBN, Zandberg po spotkaniu u Prezydenta) i wskazał nagranie Razem bez napisów. To ostatnie przepisaliśmy automatycznie lokalnym modelem whisper-large-v3-turbo; nikt nie przesłuchał dźwięku. Recenzent porównał każdy cytat z napisami i transkrypcją. W drugiej rundzie zatrzymał jeden cytat, który nie był dosłowny ("mniej poważnych" zamiast "mniej poważne"); zastąpiliśmy go parafrazą.

**Trzy badania (PR #34-#36).** Luki z sekcji "Czego nie wiemy" w ocenie odpowiedzialności zbadały trzy osobne agenty z modelem Opus, każdy w osobnej kopii repo. Każde badanie recenzował inny agent z modelem Opus, sprawdzając źródła pierwotne. Recenzenci znaleźli:
- w warunkach rozwiązań cytat sklejony z dwóch druków (544 i 254) oraz zaniżony stan wiedzy o opinii Komisji Weneckiej z 2026 roku, którą wcześniej odczytano przez kopię w archiwum;
- w skutkach dla obywateli zły numer strony raportu HFPC (s. 12 zamiast s. 22) i fakt o skarżącej M.L. bez lokalizatora;
- w postępowaniach wobec osób tylko nieścisłości (daty przeszukania, dwie wersje liczby wniosków w jednej relacji medialnej, określenie postępowania wobec trojga sędziów).

Wszystko poprawiliśmy przed scaleniem, poza jedną uwagą nieblokującą do #35 (informacja lekarza w sprawie M.L. jako relacja skarżącej), którą wprowadziliśmy w PR #37. Po badaniach skorygowaliśmy ocenę odpowiedzialności; korekty są wymienione w jej sekcji "Korekty".

**Walidator (PR #33).** Katalogi robocze agentów w głównym katalogu dawały fałszywy błąd "Powtórzone ID". Walidator pomija teraz katalog .claude, który nie ma plików śledzonych. Zmianę recenzowano osobno.

## Porządek i propozycje z debaty (PR #39, #40)

**Porządek (PR #39).** Na prośbę użytkownika z 2026.11.04 powstała oś czasu `historia-sporu.md`, przeniesiona z wersji roboczej spoza repo. Wszystkie notatki dostały linki do głosowań, kart źródeł i osi czasu. Linki w notatkach dodał agent z modelem Sonnet, resztę prowadzący (Opus). Doszły też karta głosowań 2015-2026, przygotowana wcześniej przez agenta Sonnet i niepublikowana, oraz notatka o siłach i głosach w Sejmie. README skróciliśmy do celu, metody, historii, rozwiązań i współpracy. Recenzent (Opus, osobny kontekst) w pierwszej rundzie znalazł 6 blokerów, m.in.:
- uzasadnienie odmowy ślubowania w 2015 roku bez źródła;
- datę 1986 bez źródła;
- link P 7/20 prowadzący do postanowienia zamiast wyroku;
- zły numer głosowania z 2010 roku;
- próg z art. 98 ust. 3, który liczy się od ustawowej liczby posłów.
Po poprawkach druga runda dała PASS.

**Propozycje z debaty (PR #40).** Agent z modelem Opus odczytał dokumenty autorów propozycji: PSL, Rozwoju Plus, Konfederacji, Fundacji Batorego, HFPC, Klubu Jagiellońskiego, druk Kukiz'15 i PiS z 2015 roku, a także wypowiedź Boguckiego i felieton Dudka. Recenzent (Opus) w pierwszej rundzie znalazł 4 blokery:
- raport Rozwoju Plus jest publiczny w domenie rozwoj.plus, a notatka twierdziła, że strona jest za hasłem, i bez źródła pisała, że reset obejmuje sędziów z 2026 roku;
- cytat Boguckiego był wyrwany z kontekstu;
- cytat Dudka nie był dosłowny;
- tabela przypisywała Rozwojowi Plus objęcie resetem sędziów z 2026 roku bez źródła (przy okazji recenzent wskazał niejasny zapis wiersza Fundacji Batorego).
W drugiej rundzie zostały 2 drobne blokery: numeracja akapitów w karcie Dudka i "koła" zamiast "klubu poselskiego". W trzeciej: pominięty Szef Kancelarii Prezydenta w opisie karencji i niewierny opis bloku 4 w tym wpisie. Wszystkie poprawił prowadzący. Raporty recenzji obu PR są w komentarzach na GitHubie ([#39](https://github.com/gebawkubel/trybunal/pull/39), [#40](https://github.com/gebawkubel/trybunal/pull/40)).

## Rekomendacje modeli (issue #38)

Na prośbę użytkownika z 2026.11.04 pytanie o najlepsze rozwiązanie sporu zadaliśmy osobno dwóm modelom: Claude Fable 5.1 (wysoki wysiłek, agent Claude Code) i GPT-6 Astra (wysoki wysiłek, Codex CLI w piaskownicy tylko do odczytu). Oba pracowały na kopii repozytorium w wersji 92bdfc2. Zakaz korzystania z internetu był w poleceniu. Zakazu zmian w repozytorium u Fable pilnowała tylko wiadomość zlecająca agentowi ("tylko czytaj, niczego tam nie zmieniaj"), u Astry piaskownica. Polecenia napisał koordynator (Opus).

Każdy model zrecenzował pierwszą wersję drugiego. Pierwszą wersję Astry recenzował nowy agent Fable, a nie autor rekomendacji Fable. Potem każdy model poprawił swoją wersję, mając roboczą notatkę o propozycjach z debaty, jeszcze przed jej recenzją. Fable dostał dodatkowo trzy sprostowania do tej notatki, Astra nie. Pierwsze uruchomienie poprawki Astry przerwał limit użycia Codex, zanim powstał tekst. Poprawkę uruchomiono od nowa w nowej sesji, z tym samym materiałem. Wynik i porównanie: [rekomendacje modeli](badania/rekomendacje-modeli.md).

Pierwsze wersje i recenzje krzyżowe są w commicie fca2d67: [Fable wersja 1](https://github.com/gebawkubel/trybunal/blob/fca2d67f3e86f0516e1e4f0b9bba11fe414bffad/badania/rekomendacje/fable-high-wersja-1.md), [Astra wersja 1](https://github.com/gebawkubel/trybunal/blob/fca2d67f3e86f0516e1e4f0b9bba11fe414bffad/badania/rekomendacje/astra-high-wersja-1.md), [recenzja Astry o Fable](https://github.com/gebawkubel/trybunal/blob/fca2d67f3e86f0516e1e4f0b9bba11fe414bffad/badania/rekomendacje/recenzja-astra-o-fable.md), [recenzja Fable o Astrze](https://github.com/gebawkubel/trybunal/blob/fca2d67f3e86f0516e1e4f0b9bba11fe414bffad/badania/rekomendacje/recenzja-fable-o-astra.md).

Recenzent PR #42 (Opus, osobny kontekst) w pierwszej rundzie znalazł 7 blokerów:
- porównanie przypisywało obu modelom to, co mówił jeden: klasyfikację "nowe połączenie" (Astra uznaje rdzeń za istniejący wariant), część argumentów przeciw resetowi i ocenę szans;
- budżet TK i deeskalacja były w tabeli jako różnica, choć ma je też Fable;
- teksty opisane jako "bez redakcji" miały nieujawnione zmiany nagłówków i końcowych znaków nowej linii;
- opis zrównywał ograniczenia techniczne obu modeli;
- pierwsze wersje i recenzje leżały w drzewie repozytorium, wbrew zasadzie z AGENTS.md.

Poprawiliśmy to. Doszły też: osobny wiersz o progu 3/5 (modele liczą go inaczej), treść sprostowań dla Fable i objaśnienia pojęć.

Sumy SHA-256 oryginałów (nazwa robocza, w nawiasie plik w repozytorium):

```
afa279713a479720f4c2d88055e7a98695a3d954d68fcc82e098f0e02c185708  polecenie.md (rekomendacje/polecenie.md)
4c36897314ad118e4d26189247df2c052d2ab55d6aef99c9d201b92ab88ddf69  recenzja.md (rekomendacje/polecenie-recenzji.md)
d33b2a71de5af39018e6fccf20e65d8482666fe251fa5b369c5ae1d5d337f608  poprawka.md (rekomendacje/polecenie-poprawki.md)
b1b823b06efa8a4d3c0fe30aaa241ab8467055abb8d4148f232d04fd81411111  sprostowania-dla-fable.txt (rekomendacje/sprostowania-dla-fable.md)
dc160c70938387933e4aa82fe4d7df18536f97d5831115480601e38bcc0d1e4c  fable.md (wersja 1 Fable, commit fca2d67)
1764c2897e897ef69d797ff2dad6d5e016e9588d366661081ecf5fedb2095036  astra.md (wersja 1 Astry, commit fca2d67)
4ed83e810ecd6ecd21a0f00f0fc25cbd10e66bf1c41ce420da2cc547c06eb217  recenzja-astra-o-fable.md (commit fca2d67)
0c64f1c6f94a3de888fa8ab275f41bde88aba1fee826979ce158643f663ee389  recenzja-fable-o-astra.md (commit fca2d67)
2a3dbf72c2d0f8b78d53a6bfee9fc23d199bba94c39b8ff83343fc0ae9b69df1  fable-v2.md (rekomendacje/fable-high.md)
9ef3a1795f5139cd29356e09c42de97ae722e7ae54ba03b939aa0c94a873b057  astra-v2.md (rekomendacje/astra-high.md)
```

Robocza notatka o propozycjach przekazana obu modelom do poprawki (później poprawiona w PR #40):

```
a35c7ee1fb06b600969bf4f219051d6f675772a2276582b71b4aa948fbdfd5c3  propozycje-na-stole.md
9f2fb6533720ac1d88f31ea2691f5eb5ec182c7176c5d9715f131c694072162e  batory-zalasinski-2026.md
3b9812fc1c335575bbd1adc9046254d3478adb9405fc1258385fb596017826b2  druk-166-2015.md
8f58825efd87484c0a5765fa9626e2fb3875db12484096cd22065b1a61a3f2d5  dudek-2026-11-01.md
2bb0be551417323d4bc9a3080a517f0c3cd98749056bae0dbc3fbaa99f6e945a  hfpc-zarzad-2026-10-31.md
f8ba4f617c941a93f42a77878d56fc39c86053aeb6cfb57f8c5a24a41b051bc4  kj-29-warunkow.md
8bd677fef9af1851fee8b63ec74c766ba12bb139a48b815b691ab11fbd8e9db2  konfederacja-reset-2026-10-31.md
78fba1dff5c05b03b64c92c672704073ef2d46816a42defca625f38b0b979458  psl-reset-2026-11-03.md
```

## Bilans propozycji (issue #38)

Bilans zysków i strat 14 propozycji z debaty dla 14 sił napisał GPT-6.1 Sol (wysoki wysiłek, Codex CLI w piaskownicy tylko do odczytu) na repozytorium w wersji d8b2eb1, według polecenia koordynatora (Opus). Model dobrał koordynator, bo zadanie polega głównie na porównaniu dokumentów. Dosłowne wyjście modelu jest w commicie b7b7a5d: [pierwsza wersja bilansu](https://github.com/gebawkubel/trybunal/blob/b7b7a5d952a4a54efac9a379f13dfb01458d550a/badania/rekomendacje/bilans-wersja-1.md). W repozytorium obniżyliśmy poziomy nagłówków, dodaliśmy nagłówek z opisem, sekcję "Propozycje po kolei" i końcowy znak nowej linii.

Recenzent PR #43 (Opus, osobny kontekst) sprawdził skryptem wszystkie 196 komórek macierzy z tabelami propozycji i przeliczył każdą sumę: błędów w notatce nie znalazł. Zatrzymał dwa zdania tego wpisu (nieistniejąca w publicznym AGENTS.md zasada doboru modelu i niepełny opis zmian bez stałego linku). Z jego uwag poprawiliśmy w notatce:
- zysk PiS przy propozycji Klubu Jagiellońskiego, który według karty KJ jest raczej stratą;
- odwołanie "karta KJ" bez ścieżki;
- brak źródła głosowań przy PSL, Polsce 2050 i Centrum;
- "Brak stanowiska" wpisany jako strata Centrum i Korony (teraz "Brak danych");
- niejasne "uchylenie ustawy";
- brak słowniczka pojęć. Wynik: [bilans propozycji](badania/bilans-propozycji.md).

```
2a14146659aaf8b8269d4dce28ab62a5bc27192556af473007ffb6621fe23013  polecenie.md (rekomendacje/polecenie-bilansu.md)
4d4cb7d5c59b8e32090be640ee223828eeb9ef3adacca42159f2ac972b8bc914  bilans.md (pierwsza wersja modelu)
```

Uzupełnienie po scaleniu PR #43: w kolejnym PR dodaliśmy ścieżkę karty KJ w wierszu PiS w sekcji 8 (uwaga nieblokująca recenzenta). Link z rekomendacji modeli do bilansu dodaliśmy już w PR #43, czego wpis wyżej nie wymieniał.

## Odpowiedź na pytanie (issue #38)

Notatkę końcową [odpowiedź na pytanie](badania/odpowiedz.md) napisał koordynator (Opus). Zbiera wnioski z [rekomendacji modeli](badania/rekomendacje-modeli.md) i [bilansu propozycji](badania/bilans-propozycji.md), bez własnej rekomendacji projektu.

## Symulacja negocjacji: etap 1 (issue #46)

Pierwszą próbę etapu 1 (PR #47, [commit c274b85](https://github.com/gebawkubel/trybunal/tree/c274b853aed3ff0de71e71d991e6002d6b083b3a)) zamknęliśmy bez scalania: polecenie napisał koordynator poza issue i dopisał w nim własne wytyczne, m.in. przykładową listę kandydatów. Na prośbę użytkownika z 2026.11.04 do issue #46 doszła zasada przejrzystości: wykonawca dostaje tylko dosłowną treść issue i krótką wiadomość techniczną, obie publikowane. Etap 1 wykonał od nowa Claude Fable 5.1 (wysoki wysiłek, nowy agent Claude Code) na repozytorium w wersji 78e9e45. Wynik: [skład stołu i plan przebiegów](badania/symulacja/etap-1.md).

```
87b17221569d2b4c2fb0229d72aa7f1f4c2e64a9c8a1c5155da663b2deb3dfe8  issue-46.md (badania/symulacja/etap-1-polecenie-issue.md)
bb5286b12e1c2810a8028278609d83d477a10fff91e1089a78e13d34274f9e7d  wiadomosc-techniczna.md (badania/symulacja/etap-1-wiadomosc.md)
db923f3ff54019ddf97908c85a7e2da020b2d7010c053858384ce09ecc0e6575  etap-1.md (oryginał wersji 1, commit 57463fe)
61636b0692fc757ba3bfdce876cb592dc00c71947865946c28ca446cc756879f  wiadomosc-poprawka.md (oryginał; badania/symulacja/etap-1-wiadomosc-poprawka.md)
8cd57fbddfcd6f806c0e9521ea0c65ebb32941aa3837b53d27c38120193f77ae  etap-1-v2.md (oryginał wersji 2, commit 0624cb0)
1b6d283c17a7adfb6195c8adabc2289f62a1e482ceb635772129f45ebd6988f5  wiadomosc-poprawka-2.md (oryginał; badania/symulacja/etap-1-wiadomosc-poprawka-2.md)
e1ba02aec6254e1fc461974ebb3271d78cf98685ff32f286bed7766a406f6a74  etap-1-v3.md (oryginał wersji 3, commit 066697b)
7b5375e3c58706ecd4208c529b09483cf1c21a04300d3bb21d298afe21b006b5  wiadomosc-poprawka-3.md (oryginał; badania/symulacja/etap-1-wiadomosc-poprawka-3.md)
d72d7bde944e28fd3c610fd054d73ce25ab0649faa5cfdd9c065185df3446f76  etap-1-v4.md (oryginał wersji 4; badania/symulacja/etap-1.md)
```

Recenzent (Opus, osobny kontekst) w pierwszej rundzie zatrzymał 6 blokerów, głównie arytmetycznych: kto jest "niezbędny" w ścieżkach i regułach arbitra, inicjatywa 57 posłów zamiast 92, rola PSL przy wotum nieufności, oraz dwa fakty niezgodne z repo (przebieg głosowań, nieobecni na konsultacjach 2026.10.31). [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6628753608) opublikowaliśmy w issue #46, a poprawki zrobił autor etapu w tej samej rozmowie, według jawnej wiadomości. Wersja 1: [commit 57463fe](https://github.com/gebawkubel/trybunal/blob/57463fe13de56d0ba7110bb1a080520fe4d6f055/badania/symulacja/etap-1.md).

W drugiej rundzie recenzent potwierdził usunięcie B1-B6, ale zatrzymał trzy nowe błędy arytmetyczne z poprawek: brakujące głosy w ścieżce konstytucyjnej (11 z 17, nie 7), podwójnie policzone koło Kukiza w regułach wariantu W2 i zbyt szeroko określonych niezbędnych przy wotum nieufności. [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6628905883) jest w issue #46; poprawki zrobił autor etapu (wersja 3).

W trzeciej rundzie recenzent zatrzymał jedno zdanie o tym, kiedy Konfederacja jest niezbędna przy wotum nieufności. Recenzent zaznaczył, że nieprecyzyjne brzmienie pochodziło z jego własnej propozycji poprawki. [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6628976888) jest w issue #46; poprawkę zrobił autor etapu (wersja 4).

## Wywiad Bosaka w Polsat News (issue #48)

Czytelnik wskazał wywiad Krzysztofa Bosaka w "Graffiti" Polsat News z 2026.11.04 i przekazał automatyczne napisy. Kartę nagrania i [notatkę z porównaniem z bazą](badania/bosak-2026-11-04.md) przygotował agent Opus (claude-opus-5-5, Claude Code) na podstawie automatycznych napisów YouTube, bez odsłuchu ([karta](zrodla/okres-2024-2026/bosak-polsat-2026-11-04.md)). Karta jest wyciągiem z krótkimi cytatami, jak inne karty nagrań. Spośród 36 twierdzeń 13 już było w bazie, 10 jest nowych, 4 nie zgadzają się z dokumentami, 9 to oceny. Jedyne nowe sprawdzenie poza bazą: wyroki TK ogłoszone od 2023.12.13 w Dzienniku Ustaw i Monitorze Polskim, w API ELI Sejmu. Nowe elementy stanowiska Konfederacji dopisano w [propozycjach z debaty](badania/propozycje-na-stole.md) i w indeksie stron [scenariuszy naprawy](badania/scenariusze-naprawy.md).

Recenzent (Opus, osobny kontekst) zatrzymał pierwszą wersję (commit 89600c7) z pięcioma blokerami:
- sprawdzenie publikacji wyroków objęło tylko lata 2024-2026, a rząd urzęduje od 2023.12.13; brakowało 6 wyroków z grudnia 2023 roku w Dzienniku Ustaw i Kp 1/23 w Monitorze Polskim;
- teza o "szczególnych sytuacjach" przy ślubowaniu opierała się na czasowniku dopisanym do napisów; kontekst wskazuje na odłożenie, nie odmowę;
- wariant "dwa tygodnie" może być wtrąceniem prowadzącego;
- zdanie, że Bosak woli wotum nieufności "zamiast" skrócenia kadencji, było za mocne;
- zły znacznik czasu przy pytaniu o głos za Święczkowskim i brak zaznaczenia, że "nie zaprzecza" to wniosek z kontekstu.

Poprawki: liczba wyroków ogłoszonych za obecnego rządu (9 w Dzienniku Ustaw i 1 w Monitorze Polskim, sprawdzone w ELI), data objęcia urzędu ze źródłem; twierdzenie o ślubowaniu rozdzielone na zgodne częściowo z K 34/15 i K 3/26 oraz na ocenę Bosaka, z trzema przesłankami z K 34/15 jako wnioskiem projektu; zastrzeżenia przy wariancie "dwa tygodnie" i przy wotum nieufności; znaczniki 7:47 i 8:56. Przy okazji wprowadziliśmy uwagi nieblokujące: dokładność znaczników, terminy maksymalne w art. 235, łagodniejsze ujęcie ślubowania w Konstytucji, kto pierwszy podał pięć godzin obrad, wyliczenie 2030.12.09 jako nasz wniosek.

## Debata wskazana przez czytelnika (issue #45)

Film z YouTube wskazany przez czytelnika to posiedzenie sejmowej Komisji Sprawiedliwości i Praw Człowieka nr 149 z 2026.04.28 o sytuacji w TK. Koordynator (Opus) ustalił to z metadanych filmu i API Sejmu oraz pobrał oficjalny zapis przebiegu i automatyczne napisy. Badacz (Agent-Role: badacz, Agent-Model: claude-opus-5-5, Agent-Run: Claude Code) przygotował:
- [kopię oficjalnego zapisu](zrodla/okres-2024-2026/spc-149-2026-04-28.md) z HTML z API Sejmu, z opisem normalizacji;
- porównanie napisów z zapisem skryptem: film obejmuje całe posiedzenie od otwarcia do zamknięcia (krótkich cięć wewnątrz nie wykluczamy), a różnica około 17,5 minuty wobec transmisji Sejmu przypada według godzin z API głównie na czas przed otwarciem i po zamknięciu; filmu nie oglądano;
- [notatkę o posiedzeniu](badania/komisja-2026-04-28.md): mówcy, 50 twierdzeń porównanych z bazą (zgadza się 19, częściowo 6, błędne 2, brak w bazie 17, spór o interpretację 6), braki w bazie i stanowiska stron;
- wpis na [osi czasu](historia-sporu.md) i linki w [liście analiz](analizy.md) oraz [materiałach do sprawdzenia](badania/materialy-do-sprawdzenia.md).

Najważniejsze ustalenie dla bazy: Kancelaria Prezydenta twierdzi na posiedzeniu, że Prezydent nigdy nie odmówił ślubowania czworgu, a nasza oś czasu pisze pod 2026.04.01 "Od pozostałych odmawia" bez przypisania. Notatka proponuje rozważenie tego zapisu w osobnej zmianie.

Pierwsza wersja notatki jest w commicie [acfc922](https://github.com/gebawkubel/trybunal/blob/acfc9226c88980cac65ff9b8975d3edf7fb4bf0f/badania/komisja-2026-04-28.md). Recenzent PR #49 (Opus, osobny kontekst) porównał skryptem całą kartę z oryginałem słowo po słowie i sprawdził cytaty, oceny i odwołania. Zatrzymał dwa zdania: na osi czasu przypisanie Żurkowi poglądu o ważności ślubowania w Sejmie, którego na posiedzeniu nie wyraził, oraz dwie nieprawdziwe liczby w opisie metody (najdłuższa przerwa w napisach ok. 18 s, nie poniżej 15 s; zamknięcie w 1:50:43). Poprawiliśmy je, a także: usunęliśmy "sędzia w stanie spoczynku" przy Zdziennickim (zapis tego nie podaje) i dodaliśmy zastrzeżenie o możliwych krótkich cięciach filmu.

```
6172828a4390eb0cc18a48612ad6cd8c9ffa2540931eb0a0ff4c0b7dfa51569d  komisja-2026-04-28.md (pierwsza wersja)
```

## Symulacja negocjacji: etap 2 (issue #46)

Pakiet wiedzy, karty dziesięciu postaci składu W1, instrukcje wariantów motywacji i arbitra oraz luki przygotował Claude Fable 5.1 (wysoki wysiłek, nowy agent Claude Code), według wytycznych etapu 2 dopisanych publicznie do issue #46. Polecenie: treść issue z komentarzami i jawna wiadomość techniczna. Wykonawca pracował na wersji 70b735a (gałąź `symulacja-baza-etap-2`), która łączyła zrecenzowany etap 1 z dwoma zrecenzowanymi, wtedy jeszcze nie scalonymi opracowaniami (#45, #48); GitHub miał awarię i scalanie stało. Wyniki: [pakiet wiedzy](badania/symulacja/etap-2/pakiet-wiedzy.md), [instrukcja arbitra](badania/symulacja/etap-2/arbiter.md), [warianty motywacji](badania/symulacja/etap-2/warianty-motywacji.md), [luki](badania/symulacja/etap-2/luki.md) i karty postaci w tym samym katalogu.

Sumy SHA-256 oryginałów (nazwa robocza, w nawiasie plik w repozytorium):

```
167361e9375afb1998a92677178e5d070be15b7429cdcabb5a85511ddfc65b2f  arbiter.md (badania/symulacja/etap-2/arbiter.md)
455d9f5a830e252206ad89303366b1e8f74b23d6713ac8c7fc4a031a65b8f575  karta-bosak.md (badania/symulacja/etap-2/karta-bosak.md)
7fd453f93526920afd1730e5235f77162735a8571e3005bdd09b7a71fd9ca2f1  karta-czarzasty.md (badania/symulacja/etap-2/karta-czarzasty.md)
afbd00ea421e2005858bb91d7ea6daaa40be79f8937f3aea270f475a2464a652  karta-holownia.md (badania/symulacja/etap-2/karta-holownia.md)
05b425a8865ef2390cd29d488545b18e12fb529663560ff04df8c4403c806241  karta-kaczynski.md (badania/symulacja/etap-2/karta-kaczynski.md)
3ea4cbd231641d6bf7b132bdb4bd8f885a7f2f2d138f05de55e456e6c18b6d4a  karta-korwin-piotrowska.md (badania/symulacja/etap-2/karta-korwin-piotrowska.md)
daaf6b00f0873054f6a084577cbd809d15955b0f886414a7074af3d24d424eda  karta-kosiniak-kamysz.md (badania/symulacja/etap-2/karta-kosiniak-kamysz.md)
0c356d8581d3c06ce023f258eda98b6a799d54b140c7feb0028a54bc5e591975  karta-morawiecki.md (badania/symulacja/etap-2/karta-morawiecki.md)
ae017499993d712fa434cbc7052bf9b5c590f8426bceb98dac7b22555333d163  karta-nawrocki.md (badania/symulacja/etap-2/karta-nawrocki.md)
7433bdaa7768ef4c7798945587f0c4c45ae45635c5bc7843245e3c35a71e35d5  karta-swieczkowski.md (badania/symulacja/etap-2/karta-swieczkowski.md)
22149325b4319c49a198bda68ef8bca3596fdd81622c37ebc9741ef568dfd2c9  karta-tusk.md (badania/symulacja/etap-2/karta-tusk.md)
df38eb961093749ee4874d51297b3e16b244c606efb9cb6a0a978d495d0d8290  luki.md (badania/symulacja/etap-2/luki.md)
ac458f6ffa259d9d5ae80500583efb14e9744ef6735976fd6ee4e9e77b8d66cb  pakiet-wiedzy.md (badania/symulacja/etap-2/pakiet-wiedzy.md)
6114ebe4427694d27cdecd1077fbc04a4f24ff6b55b2e0b8d5ecdb5be255d881  warianty-motywacji.md (badania/symulacja/etap-2/warianty-motywacji.md)
5cd0d4836fdbbbb2e0cd21f90e5b8c04849923f420eaa221eb96fe6e969bdbe5  issue-46.md (badania/symulacja/etap-2/polecenie-issue.md)
6eefaaeb96b34814a21643f797e0d549c80cd4e448589690a90bf958eb5343af  wiadomosc-techniczna.md (badania/symulacja/etap-2/wiadomosc.md)
```

Recenzent (Opus, osobny kontekst) w pierwszej rundzie zatrzymał 5 blokerów: zaniżony o połowę szacunek tokenów pakietu (zmierzony `count_tokens`: około 118,5 tys.) i za niski limit tokenów wypowiedzi, niespójną granicę między faktem a oceną w pakiecie, błąd prawny i dwa liczbowe w karcie Kaczyńskiego, słowa przypisane Kosiniakowi-Kamyszowi na podstawie adresu URL oraz nierówne traktowanie (tylko karta Bosaka zawierała korekty jego wypowiedzi). [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6629816916) jest w issue #46; poprawki zrobił autor etapu (wersja 2, opis zmian w `luki.md`). Wersja 1: [commit bd2643c](https://github.com/gebawkubel/trybunal/tree/bd2643ca06f88f370280b4e3bb57a4fa4dedde9e/badania/symulacja/etap-2).

```
a0149bad72164c4d9efb065289d5a909b044461d8822025049f8582109d14dd4  arbiter.md (oryginał v2; badania/symulacja/etap-2/arbiter.md)
0a04afdc95984be0820f26909daef60ffa1db88305e560362bc3c457ff47588c  karta-bosak.md (oryginał v2; badania/symulacja/etap-2/karta-bosak.md)
0ab7cd78aa1aee04e5314f906fb2cc3a4da342271dfee4a956b6530de8bcfa93  karta-czarzasty.md (oryginał v2; badania/symulacja/etap-2/karta-czarzasty.md)
624d0b5b7e85342f1fb210428320a8ab618083968d52958fbb185fb6fc32dd34  karta-holownia.md (oryginał v2; badania/symulacja/etap-2/karta-holownia.md)
b8ad92d7083d259a7e062d93a5c3dcde4009085428d6949d50d7166bbd4822ef  karta-kaczynski.md (oryginał v2; badania/symulacja/etap-2/karta-kaczynski.md)
daf787e387f12441a0bb0369c88ff50ecbac794ef99b0ef3720b691d13fae4a3  karta-korwin-piotrowska.md (oryginał v2; badania/symulacja/etap-2/karta-korwin-piotrowska.md)
2c9d89ed90cac62dba42315cddd92f5a7b878c70eb2a76ea8039f9bff5ec33b2  karta-kosiniak-kamysz.md (oryginał v2; badania/symulacja/etap-2/karta-kosiniak-kamysz.md)
a76bbf0bb54d0d475042ae756c8b3de6727343a8dad1a0fb9876a521ff542620  karta-morawiecki.md (oryginał v2; badania/symulacja/etap-2/karta-morawiecki.md)
aa86dd11d67458f93e55ce26890a6da62f49df25f86d906d0d789d3d3f3c288f  karta-nawrocki.md (oryginał v2; badania/symulacja/etap-2/karta-nawrocki.md)
cc6fe7d0fb10dcbb26f357e0c7720314189c1033fd886fb4cbca1e128ed84eda  karta-swieczkowski.md (oryginał v2; badania/symulacja/etap-2/karta-swieczkowski.md)
ff9d2518ba1ce9fd2da6306a34248c828e242d2f038b3c260495c49d14f82fcd  karta-tusk.md (oryginał v2; badania/symulacja/etap-2/karta-tusk.md)
cca79bc86069701df940aa12042c8d50a06906ecaf2cbba43a43dff18cfa5c62  luki.md (oryginał v2; badania/symulacja/etap-2/luki.md)
a91afbf898b554477a349f65671eea1477047fde430bb0959ea2fd061f8584a3  pakiet-wiedzy.md (oryginał v2; badania/symulacja/etap-2/pakiet-wiedzy.md)
4497509268a10557c9a7363b504fb21861234b7d11b647ab9f17f7b5c8b3072b  warianty-motywacji.md (oryginał v2; badania/symulacja/etap-2/warianty-motywacji.md)
00f9977e766183a0acd087d7226bacf8d10703ee19b6d1eb5cbe6f4eec18a6bf  wiadomosc-poprawka.md (oryginał v2; badania/symulacja/etap-2/wiadomosc-poprawka.md)
```

W drugiej rundzie recenzent potwierdził usunięcie B1-B5 i zatrzymał jedno zdanie w instrukcji arbitra (przy stole wotum nieufności daje też Lewica z Polską 2050, 240 głosów, a tekst mówił "tylko PSL albo KO"). [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6630020845) jest w issue #46; poprawki zrobił autor etapu (wersja 3, 9 zmienionych plików). Wersja 2: [commit 62f5e27](https://github.com/gebawkubel/trybunal/tree/62f5e272ab4a9224af1e6bd540e77fcbdc01124a/badania/symulacja/etap-2).

```
08445af7c3cc107dd34075acf02e233f48116115a8a8b091934531a987adc255  arbiter.md (oryginał v3; badania/symulacja/etap-2/arbiter.md)
b88a79a67ddef5d6e01807a07582d6494170e5d658145ae6c1039289fc5ef833  karta-bosak.md (oryginał v3; badania/symulacja/etap-2/karta-bosak.md)
0ab7cd78aa1aee04e5314f906fb2cc3a4da342271dfee4a956b6530de8bcfa93  karta-czarzasty.md (oryginał v3; badania/symulacja/etap-2/karta-czarzasty.md)
624d0b5b7e85342f1fb210428320a8ab618083968d52958fbb185fb6fc32dd34  karta-holownia.md (oryginał v3; badania/symulacja/etap-2/karta-holownia.md)
e3892bdeeb151d281361757f6c3fd975153a2e68dbd22b2b13e3427df509c9c1  karta-kaczynski.md (oryginał v3; badania/symulacja/etap-2/karta-kaczynski.md)
9f767bb440c64e50e4942861476be387d2f202fc9e2d32bd70283289907543ed  karta-korwin-piotrowska.md (oryginał v3; badania/symulacja/etap-2/karta-korwin-piotrowska.md)
2c9d89ed90cac62dba42315cddd92f5a7b878c70eb2a76ea8039f9bff5ec33b2  karta-kosiniak-kamysz.md (oryginał v3; badania/symulacja/etap-2/karta-kosiniak-kamysz.md)
a76bbf0bb54d0d475042ae756c8b3de6727343a8dad1a0fb9876a521ff542620  karta-morawiecki.md (oryginał v3; badania/symulacja/etap-2/karta-morawiecki.md)
9049d7dece1d7e1029b044310d8dac387d9c15f6336802cb6eb276ba391c70a0  karta-nawrocki.md (oryginał v3; badania/symulacja/etap-2/karta-nawrocki.md)
72c42e3af8b54e1effb16fa105619990f8cbd194bd80675a2c67796b83973a0d  karta-swieczkowski.md (oryginał v3; badania/symulacja/etap-2/karta-swieczkowski.md)
147195d1c1231f28a9f530da8dcf68bf79e324d336e6bae2685d9405a43a4963  karta-tusk.md (oryginał v3; badania/symulacja/etap-2/karta-tusk.md)
0af52792be8bee8f1fd8c9d8721680c6803d1bca2db0f5ec1d55dfdbb79e49de  luki.md (oryginał v3; badania/symulacja/etap-2/luki.md)
e6e97359336e53510d9a52990bc6da147027281c0fc0389d12fad7fd3cee4457  pakiet-wiedzy.md (oryginał v3; badania/symulacja/etap-2/pakiet-wiedzy.md)
4497509268a10557c9a7363b504fb21861234b7d11b647ab9f17f7b5c8b3072b  warianty-motywacji.md (oryginał v3; badania/symulacja/etap-2/warianty-motywacji.md)
43f459c0a01b73d1eba2e4121ac06d6cb030e2bedb2f4abd861a9ea3d3e86b2a  wiadomosc-poprawka-2.md (oryginał v3; badania/symulacja/etap-2/wiadomosc-poprawka-2.md)
```

## Symulacja negocjacji: etap 3 (issue #46)

Skrypt rozmowy i arbitra (`narzedzia/symulacja/`) napisał Claude Opus 5.5 (osobny agent Claude Code) według wytycznych etapu 3 dopisanych publicznie do issue #46. Polecenie: treść issue i jawna wiadomość techniczna; w trakcie pracy wykonawca dostał też uzupełnienie o zapisie na żywo, opublikowane najpierw w issue. Wykonawca mógł wywoływać tylko liczenie tokenów; generowania nie uruchamiał. Szacunek kosztu pierwszego przebiegu: około 15 USD (zakres 12-23 USD); po pierwszej rundzie recenzji (stały schemat arbitra, zapas w limicie kosztu) i po wyborze kolejności kontekstu z etapu 2 przez prowadzącego: około 18 USD (zakres 16-24 USD), opis w `narzedzia/symulacja/README.md`.

```
a32dc38d1d22288e82b0d61e0610c0778d9d8d43397343018ebcf54cb763680c  issue-46.md (badania/symulacja/etap-3/polecenie-issue.md)
0ab8b7ebde891c5ac1666599d4ff8c5c2c918900842580d862672fe35a241a00  wiadomosc-techniczna.md (badania/symulacja/etap-3/wiadomosc.md)
72e10e1ffb0433c5691031465a098c839c42a1b4ec660a770df77d1d432334d1  wiadomosc-uzupelnienie.md (badania/symulacja/etap-3/wiadomosc-uzupelnienie.md)
```

Recenzent (Opus, osobny kontekst) w pierwszej rundzie zatrzymał 2 blokery: zmienny schemat odpowiedzi arbitra unieważniał bufor (koszt typowego przebiegu około 23,5 USD zamiast 15) i limit kosztu nie rezerwował kwoty na ogłoszenie przerwania. Wskazał też dwie decyzje wykonawcy wymagające zgody prowadzącego; prowadzący [rozstrzygnął](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6630993172): kolejność kontekstu jak w etapie 2, głos poza kolejnością po rundzie. [Raport](https://github.com/gebawkubel/trybunal/issues/46#issuecomment-6630779132) jest w issue #46; poprawki zrobił wykonawca (commit 39a0e8a).

```
45804ee4e07e335f745afa64b4a29a9e5d54fe0c0442b87906b9aa30d14fe7cd  wiadomosc-poprawka.md (badania/symulacja/etap-3/wiadomosc-poprawka.md)
9ce9f3a9edbdf9c118edc40fab167297551742492e62ac5da527d87b9698cfd6  wiadomosc-rozstrzygniecia.md (badania/symulacja/etap-3/wiadomosc-rozstrzygniecia.md)
```

## Symulacja negocjacji: przebieg 1 (issue #46)

Pierwszy płatny przebieg uruchomił koordynator 2026.11.04, 14:03-14:29: skrypt z PR #53, skład W1, wariant (b), model `claude-opus-5-5`, wysiłek `medium`, limit 25 USD. Koszt z `usage`: 14,50 USD (szacunek około 18 USD), 81 wywołań. Wynik według arbitra: porozumienie, 10 głosów za pakietem nr 1. Skrypt uciął po limicie 1100 tokenów 10 wypowiedzi; we wszystkich 9 z głosowania głos padł przed cięciem. Zapis, ustawienia i sumy: `badania/symulacja/przebieg-1/`. W `zapis.md` zamieniono 12 półpauz z wypowiedzi modelu na łączniki; `zapis.jsonl` jest bez zmian.

Na prośbę prowadzącego koordynator napisał [raport](badania/symulacja/przebieg-1/raport.md) z porównaniem z wcześniejszymi analizami i dopisał wynikowy wariant ("reset z zachowaniem sędziów z 2026 roku") do [scenariuszy naprawy](badania/scenariusze-naprawy.md#scenariusze-z-symulacji-negocjacji).

```
8a471bca7251d286f77c90e7d2bf92bd719086817ff22ea1861e6add50520107  zapis.md (oryginał; w repo 0636945628b5aaecd93c70225f6de2775317b6e49b2fb2096527abaa74a883d3)
c7d2bf5272f189a278578fa8428783f7649af9fa6478b3fd14732a448ccf8ea6  zapis.jsonl
```

## Symulacja negocjacji: etap 4 (issue #46)

Po przebiegu 1 prowadzący napisał w #46, że przy stole nie trzeba tylu osób, zgoda wszystkich nie jest wymagana, a długość wypowiedzi trzeba umiarkowanie poprawić. Koordynator zapisał te uwagi dosłownie w komentarzu "Etap 4" i zlecił wykonanie osobnemu agentowi (Claude Opus 5.5, Claude Code). Polecenie: treść issue z komentarzami i jawna wiadomość techniczna, w jednym pliku o SHA-256 `0072843696f5d995404b4e25e765214554f480ee3bb4c6809f9f1e1d599493c8` (w wiadomości ścieżkę lokalną zastąpiono "<katalog roboczy>"). Pierwsza wersja wyniku: commit [01b1b37](https://github.com/gebawkubel/trybunal/commit/01b1b37d3ed21d4c9bd4f3066a59294d05098adf). Recenzent (Opus, osobny kontekst) w pierwszej rundzie zatrzymał 1 bloker: cytat z Kp 3/24 z błędnym lokalizatorem, niedosłowny i o zbyt szerokim zakresie. Wykonawca poprawił go w `etap-4.md` i w `arbiter.md` (nowe sumy tekstów) oraz wprowadził 7 z 8 uwag; polecenie poprawki: `wiadomosc-poprawka.md` (w opublikowanej wersji ścieżka zastąpiona "<katalog roboczy>").

```
25f32052c68121e023253bc4fa589b3bb889c5c42798be9a43ea3a3cf4f923fa  polecenie-issue.md (badania/symulacja/etap-4/polecenie-issue.md)
68eac874b7a3c274d80eb8f205944989f24fa58f5a83321473089d8cf8d25566  wiadomosc.md (badania/symulacja/etap-4/wiadomosc.md)
97c0e296f7e9f4211af1e884becd9aca56ee78fd283b59442c18e073bc783ba1  etap-4.md (pierwsza wersja, 01b1b37)
e6ebcdfeb08d2c524ab77bb96f42678b063222af941934f81b3a96ee7696d10d  wiadomosc-poprawka.md (badania/symulacja/etap-4/wiadomosc-poprawka.md)
dc10c9603e45222cd5e573bc82601d5b503a1f21739d2010bc3ba36b3915a436  etap-4.md (wersja 2 po recenzji, 47f6183)
```

## Symulacja negocjacji: przebiegi 2-10 (issue #46)

Po scaleniu PR #55 i decyzji prowadzącego ("dzialaj") koordynator uruchomił 2026.11.04, 17:18-19:10, przebiegi 2-10 według planu z etapu 4: skład W5, warianty a, c, b, przesunięcie 0, 1, 2, limit 18 USD na przebieg, repozytorium 20270d2. Pierwsza próba uruchomienia 5-7 nie wystartowała (błąd argumentów w pętli powłoki, skrypt zakończył się przed wywołaniem API, bez kosztu). Wszystkie przebiegi skończyły się porozumieniem. Koszt z `usage` przebiegów 1-10 łącznie: 56,35 USD. Zestawienie koordynatora: [wyniki](badania/symulacja/wyniki.md); w scenariuszach naprawy dopisano wiersz o krokach "na teraz" uzgodnionych we wszystkich przebiegach. W `zapis.md` półpauzy z wypowiedzi modelu zamieniono na łączniki; `zapis.jsonl` bez zmian. Recenzent (Opus, osobny kontekst) w pierwszej rundzie zatrzymał 3 blokery w zestawieniu: sędziowie z 2026 roku "zostają" mimo otwartej sprawy Berka, zbyt mocny wniosek o wpływie motywacji i nieprawdziwe zdanie, że sporne sprawy zawsze zostawały otwarte. Koordynator poprawił je razem z uwagami. Pierwsza wersja zestawienia: commit [901b3bf](https://github.com/gebawkubel/trybunal/commit/901b3bfe557d8d7de89d08786995d2b523383eb9).

```
29063426460ba13cd979e0de94ef54ed83dc495ec62d64fd74f20e500407647c  wyniki.md (pierwsza wersja, 901b3bf)
ff44aa53c7ddecdbe8209fc9f25d98a912dba13e83f9cad57d093bc495e4afc9  wyniki.md (wersja 2 po recenzji)
f88d646d8048e650b3c6e57fe7c2a04d034612abe040be6dc75bf385079a1bb6  wyniki.md (wersja 3: krótkie podsumowanie na prośbę prowadzącego i poprawki po rundzie 2 recenzji)
c69835019c3cdf4bb8e592d6a37280c31dfa02a58db5d26298ab46c22862408f  przebieg-2/zapis.md (oryginał; w repo c69835019c3cdf4bb8e592d6a37280c31dfa02a58db5d26298ab46c22862408f)
8b648b5d130ab609df0fbff8108cde9aaf35fd68f70e7017e66a082e81da0286  przebieg-3/zapis.md (oryginał; w repo e31558c9f917df205fd98f45777d2041713bb989032cd212cdc5f196100905d6)
8e5ae6d521b72f477546bb976aa835b826504305b25024404d6d288249ab2e84  przebieg-4/zapis.md (oryginał; w repo 441fc7604db7792f59b852778227d9e4e918606b1bf83038012dd236d6283428)
9d5e7e10efe63abe56d741ebb3d5a9a888885b52b3bdb20cce3d5c3966a68135  przebieg-5/zapis.md (oryginał; w repo 9d5e7e10efe63abe56d741ebb3d5a9a888885b52b3bdb20cce3d5c3966a68135)
db435919538bf5e37684f649b100a849a325fffbbec0ac4165ec0197db03af02  przebieg-6/zapis.md (oryginał; w repo 2b784962296a2801f5a942e0d344803930ece7dcb8ba70648848842fc551da4c)
9b3479e86f6697d84667c339d7d59a875e45b1806f6ffeb0c1a5746334624c53  przebieg-7/zapis.md (oryginał; w repo 2eb6cdf79b970d8938d9e8eb43954af8c26fcc7f7610bee435903098fb4fc5e8)
aab0d984a6b63ddefeb3ba36e0acfc4a1e92531ccb4c7b451a5adecef87ef6ec  przebieg-8/zapis.md (oryginał; w repo aab0d984a6b63ddefeb3ba36e0acfc4a1e92531ccb4c7b451a5adecef87ef6ec)
44e34174fce698dcd3df5339e9669ae22e1a9dbb3dd580c81105f062efdbacf1  przebieg-9/zapis.md (oryginał; w repo 2e1b0cbe66e508e42adaa82982b7d068d9a04a48003ae9873fcd81613c656d27)
2ca46d58e7683eaae9507232b9a36dee9e5b51e7cf55db50ddbf92ebea74b4c1  przebieg-10/zapis.md (oryginał; w repo 2ca46d58e7683eaae9507232b9a36dee9e5b51e7cf55db50ddbf92ebea74b4c1)
```

## Bilans propozycji: scenariusze spoza debaty (issue #57)

Na prośbę prowadzącego, zapisaną dosłownie w issue #57, koordynator zlecił dopisanie do bilansu scenariuszy, które rozwiązują spór, a pojawiły się poza debatą (symulacja #46, rekomendacje modeli #38, scenariusze z analiz AI). Wykonawca: GPT-6.1 Sol, ten sam model co pierwotny bilans (wysoki wysiłek, Codex CLI w piaskownicy tylko do odczytu, bez internetu), na repozytorium 0ed9a42. Polecenie: treść issue i wiadomość techniczna, [polecenie-bilansu-57.md](badania/rekomendacje/polecenie-bilansu-57.md). Model zwrócił pełną nową treść pliku; w repozytorium dodaliśmy tylko końcowy znak nowej linii. Dodał propozycje 15 (reset z zachowaniem sędziów z 2026 roku, z symulacji) i 16 (wąska zmiana Konstytucji bez resetu i kompromis z Prezydentem, z rekomendacji modeli) oraz sekcję o doborze; oceny propozycji 1-14 bez zmian, zmienione nagłówek i wnioski 1, 3 i 4, dodane wnioski 9 i 10. Dosłowne wyjście modelu: [bilans w commicie 8f846f3](https://github.com/gebawkubel/trybunal/blob/8f846f347bc625869cc634f1c9e742f138becb17/badania/bilans-propozycji.md), różni się od niego tylko końcowym znakiem nowej linii. Recenzja PR #58 (Opus, osobny kontekst): PASS bez blokerów; uwagi do tekstu modelu (słowniczek bez PKW, ETPC i TSUE, niejednoznaczne zdanie we wniosku 4, różne nazwy wiersza 15 i sekcji) zostawiamy jawnie, bez zmiany tekstu modelu.

```
7239b7b83e2fd0a6af1db472c43d509a25a4f7aaea279b717b8a176a6a5b0789  polecenie-bilansu-57.md (badania/rekomendacje/polecenie-bilansu-57.md)
e5604e87cce9be98b9fce7f842aa55df27ee86e8a9b63d061cacf11caa7bee14  bilans.md (pierwsza wersja modelu, bez końcowego znaku nowej linii)
```

## Symulacja negocjacji: zamknięcie (issue #46)

Prowadzący uznał symulację za eksperyment i nie zlecił serii kontrolnej na innym modelu (2026.11.04: "ta symulacja to byl tylko eksperyment zeby wylonic moze jakies nowe koncepcje i zobaczyc z ciekawosci sprawdzic czy to sie wo ogole powiedzie"). Na jego prośbę koordynator ułożył opis od ogółu do szczegółu: wpis w README i liście analiz, [strona symulacji](badania/symulacja/wyniki.md) z planem, przebiegiem, wynikiem i wnioskami oraz linkami do wszystkich rozmów i etapów, a w [odpowiedzi na pytanie](badania/odpowiedz.md) zdanie o propozycjach 15 i 16 bilansu zamiast nieaktualnego "bilans nie obejmuje pakietu modeli". Wykorzystano 56,35 USD z budżetu 100 USD.
