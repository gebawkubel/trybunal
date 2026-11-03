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

Numery #1 i #12 to zgłoszenia zadań, a PR #2 i #3 z 2026.11.02 zamknięto bez scalenia. Pierwszą wersję organizacyjną przygotowano z pomocą Codex. PR #13-#16 i #18 prowadziła równolegle druga sesja agenta, a model podano w commitach.

## Lista scenariuszy naprawy (PR #10, #17, #19, #21)

Prowadzący: Claude Code, model claude-opus-5-5. Wszyscy agenci pracowali z wyszukiwaniem w sieci, każdy w osobnym kontekście, bez dostępu do repozytorium. Każdy etap wykonano raz.

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
- błędne przypisania stanowisk: m.in. "brak stanowiska PiS wobec resetu", choć wypowiadał się poseł Wójcik, plan Szczuckiego przypisany Morawieckiemu, HFPC opisana jako przeciwna wygaszeniu kadencji, choć je popiera.

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

Analizy powstały osobno, bez wglądu w drugą. Polecenie opierało się na relacjach mediów z przebiegu Zgromadzenia. Sumy SHA-256 zapisane przed recenzjami:

```
fe2acc61efb8677f12a3ac6760b980f13bd1274100871c9575998753d112fb27  polecenie.md
f01e7caa1b57dde5650c825a1be052d64f33557d9c7826682bdfb59e49a63fb2  analiza-a.md
0d4176f390bca52a441c8fdc8fd8d07bc890c7bc81722fba820d28583354e28f  analiza-b.md
```

Przed publikacją usunęliśmy z analizy A i recenzji analizy A lokalny przedrostek ścieżek do plików repo. Suma analizy A po tej zmianie: `fa41ecf722700749d412f372b188d81c1d6a99b98cb612d9547246661d53ebdf`. W wyliczeniu stażu zamieniliśmy tylko lokalną ścieżkę na słowa "katalog roboczy agenta". Suma przed zmianą: `34b1e784f12eeed3c9b1668d148fa4f84b4887061e9e0442e7e7d2275a256e34`.

**Co znaleźli recenzenci.**
- Analiza A pominęła uchwałę Sejmu z 2026.03.13. Jej pkt 3 daje stronie zwołującej argument, że stanowisko Prezesa w praktyce jest nieobsadzone. Analiza A pomyliła też daty i opisy orzeczeń.
- Analiza B źle zrekonstruowała podstawę przerwy w czynnościach Prezesa. Pominęła też termin 7 dni na zawiadomienie i stan budżetu TK.
- Recenzent notatki (PR #20) zauważył, że wniosek przypisywał wyrokom K 1/17 i K 3/26 więcej, niż w nich jest, i że części faktów brakowało źródeł.
- Recenzent PR #22 wskazał, że wyliczenie stażu zakładało ciągłą pracę od początku aplikacji, czego życiorys nie potwierdza. Wiersz Piotrowicza w wyliczeniu opiera się częściowo na pamięci modelu, co nie wpływa na wynik.

Brzmienie przepisów cytowanych w notatce prowadzący sprawdził osobno w ELI. Życiorys z druku 2333, biogram Sycha i uzasadnienie druku 3150 też sprawdził sam.
