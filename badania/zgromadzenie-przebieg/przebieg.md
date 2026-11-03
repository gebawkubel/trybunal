# Przebieg: analiza Zgromadzenia Ogólnego TK z 2026.11.03

Data: 2026.11.03. Wynik: [notatka](../zgromadzenie-2026-11-03.md).

| Etap | Plik | Wykonawca | Wejście |
|---|---|---|---|
| Polecenie | [polecenie.md](polecenie.md) | prowadzący, Claude Opus 5.5 | relacje mediów z 2026.11.03 |
| Analiza A | [analiza-a.md](analiza-a.md) | agent, model Claude Fable 5.1 | polecenie, przepisy, repo, strony WWW i relacje mediów |
| Analiza B | [analiza-b.md](analiza-b.md) | agent, model Claude Opus 5.5 | polecenie, przepisy, repo, strony WWW i relacje mediów |
| Recenzja A | [recenzja-analizy-a.md](recenzja-analizy-a.md) | agent, model Claude Opus 5.5 | analiza A, przepisy |
| Recenzja B | [recenzja-analizy-b.md](recenzja-analizy-b.md) | agent, model Claude Fable 5.1 | analiza B, przepisy |
| Notatka | [zgromadzenie-2026-11-03.md](../zgromadzenie-2026-11-03.md) | prowadzący, Claude Opus 5.5 | analizy, recenzje, ELI |

Analizy powstały osobno, bez wglądu w drugą. Każdy etap wykonano raz. Analizy są pierwszymi wersjami, bez poprawek, więc zawierają błędy wskazane w recenzjach. W notatce korzystaliśmy z ustaleń po recenzji. Brzmienie przepisów cytowanych w notatce prowadzący sprawdził osobno w ELI.

Polecenie powstało w katalogu roboczym jako `polecenie-analiza.md`, stąd ta nazwa w recenzjach. W repo nazywa się `polecenie.md`, treść jest ta sama.

Sumy SHA-256 zapisane przed recenzjami:

```
fe2acc61efb8677f12a3ac6760b980f13bd1274100871c9575998753d112fb27  polecenie.md
f01e7caa1b57dde5650c825a1be052d64f33557d9c7826682bdfb59e49a63fb2  analiza-a.md
0d4176f390bca52a441c8fdc8fd8d07bc890c7bc81722fba820d28583354e28f  analiza-b.md
```

Jedyna zmiana po zapisaniu sum: w analizie A i recenzji analizy A usunęliśmy lokalny przedrostek ścieżek do plików repo (katalog domowy i położenie repo na dysku), bo nie publikujemy lokalnych ścieżek. Ścieżki zaczynają się teraz od `zrodla/`. Suma analizy A po tej zmianie:

```
fa41ecf722700749d412f372b188d81c1d6a99b98cb612d9547246661d53ebdf  analiza-a.md
```
