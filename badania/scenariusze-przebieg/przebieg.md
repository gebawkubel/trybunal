# Przebieg prac nad listą scenariuszy

Data: 2026.11.03. Prowadzący: Claude Code, model claude-opus-5-5. Wszyscy agenci pracowali z wyszukiwaniem w sieci i pobieraniem stron, każdy w osobnym kontekście, bez dostępu do repozytorium. Wynik końcowy: [scenariusze naprawy](../scenariusze-naprawy.md).

| Etap | Plik | Wykonawca | Wejście |
|---|---|---|---|
| Polecenie analiz | [polecenie-scenariusze.md](polecenie-scenariusze.md) | prowadzący | - |
| Polecenie katalogu | [polecenie-katalog.md](polecenie-katalog.md) | prowadzący | - |
| Katalog: koalicja i Prezydent | [katalog-koalicja-prezydent.md](katalog-koalicja-prezydent.md) | agent, model sonnet (wersja niepotwierdzona) | polecenie katalogu + lista stron |
| Katalog: opozycja i instytucje | [katalog-opozycja-instytucje.md](katalog-opozycja-instytucje.md) | agent, model sonnet (wersja niepotwierdzona) | polecenie katalogu + lista stron |
| Analiza A | [analiza-a.md](analiza-a.md) | agent, claude-fable-5-1 (według deklaracji modelu) | polecenie analiz; zakaz czytania innych wyników |
| Analiza B | [analiza-b.md](analiza-b.md) | agent, claude-opus-5-5 (według deklaracji modelu) | polecenie analiz; zakaz czytania innych wyników |
| Recenzja analizy A | [recenzja-analizy-a.md](recenzja-analizy-a.md) | agent, claude-opus-5-5 | polecenie analiz + analiza A |
| Recenzja analizy B | [recenzja-analizy-b.md](recenzja-analizy-b.md) | agent, claude-fable-5-1 | polecenie analiz + analiza B |
| Weryfikacja faktów | [fakty-zweryfikowane.md](fakty-zweryfikowane.md) | agent, claude-opus-5-5 | katalogi i analizy |
| Weryfikacja stanowisk | [stanowiska-zweryfikowane.md](stanowiska-zweryfikowane.md) | agent, model sonnet (wersja niepotwierdzona) | katalogi |

Każdy etap wykonano raz, bez ponowień. Identyfikatory przebiegów agentów nie są publicznie weryfikowalne, więc ich nie podajemy.

Sumy SHA-256 pierwszych wersji, zapisane przed recenzjami i weryfikacją. Pliki w tym katalogu są tymi pierwszymi wersjami, bez poprawek:

```
67d63d47f338af684ce218a786cef6c32fa6d38168e3c4c0d3d704c0392f5269  analiza-a.md
9b61393a32d92294f6889fb61593a7eece410a2e59a19e85fb2b4ac383a0782b  analiza-b.md
c68bf8e9b85e598494e27d74772d6e1fee826046faf8d973ef6ea78ab9482d98  katalog-koalicja-prezydent.md
a88a895ebc33173284b73e2d0881f4d27f19ea7812384ec308a8a419df4086e7  katalog-opozycja-instytucje.md
f52aad4f48a447de551610419a542ab1ca09350a97733964cf2074b23e5aed59  polecenie-scenariusze.md
```

Katalogi i analizy zawierają błędy wykryte później w weryfikacji, np. nieaktualną liczebność klubów, błędne daty i przypisania stanowisk. Lista ich zawiera [weryfikacja faktów](fakty-zweryfikowane.md#2-błędy-w-plikach) oraz [weryfikacja stanowisk](stanowiska-zweryfikowane.md#błędy-w-katalogach). W liście końcowej korzystaliśmy z wersji zweryfikowanych.
