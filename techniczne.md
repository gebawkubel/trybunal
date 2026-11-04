# Informacje techniczne

## Jak czytać pliki

Wszystkie dokumenty to pliki Markdown (`.md`). Można je czytać na GitHubie albo pobrać repozytorium i otworzyć folder w [Obsidianie](https://obsidian.md), programie do połączonych notatek. Linki między plikami działają w obu miejscach.

## Układ katalogów

| Gdzie | Co jest w środku |
|---|---|
| `historia-sporu.md` | oś czasu całego sporu |
| `analizy.md` | lista wszystkich notatek badawczych |
| `badania/` | notatki badawcze |
| `zrodla/` | kopie dokumentów źródłowych w Markdown, każda z adresem oryginału i datą dostępu |
| `zrodla/manifest.json` | sumy kontrolne SHA-256 kopii źródeł, które pokazują, czy plik zmieniono po zapisaniu |
| `historia-prac.md` | przebieg prac, recenzje, sumy kontrolne pierwszych wersji i stałe linki do nich |
| `narzedzia/sprawdz.py` | automatyczna kontrola repozytorium |
| `AGENTS.md` | reguły dla agentów AI pracujących nad projektem; `CLAUDE.md` to dowiązanie do tego pliku |

## Automatyczna kontrola

Przed wysłaniem zmiany na GitHub uruchamiamy:

```
python3 narzedzia/sprawdz.py
```

Program sprawdza sumy kontrolne źródeł, czy linki między plikami prowadzą do istniejących plików i nagłówków, czy w tekstach nie ma prywatnych ścieżek ani tokenów GitHub, typografię oraz autora i committera w historii Git. Ta sama kontrola działa na GitHubie przy każdej propozycji zmiany. Kontrola wykrywa błędy techniczne, nie sprawdza prawdziwości treści.

## Jak zmiana trafia do bazy

1. Autor przygotowuje zmianę na osobnej gałęzi i otwiera Pull Request (PR).
2. Osobny agent AI recenzuje dokładną wersję zmiany i wydaje wynik: akceptacja albo lista błędów.
3. Po akceptacji i zielonych kontrolach zmiana jest scalana zwykłym merge, żeby zachować wszystkie commity.

Commity agentów zawierają pola `Agent-Role`, `Agent-Model` i `Agent-Run`, które mówią, jaka rola i jaki model wykonały pracę. Szczegóły: [AGENTS.md](AGENTS.md).
