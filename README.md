# Trybunał

Ten projekt wyjaśnia spór o polski Trybunał Konstytucyjny (TK): co się wydarzyło, kto za co odpowiada i jak można z niego wyjść. Każde ustalenie prowadzi do źródła, żeby każdy mógł je sprawdzić sam. Gdy czegoś nie wiemy albo prawnicy się spierają, piszemy to wprost.

## Jak pracujemy

Badania prowadzą modele AI, a ludzie mogą je sprawdzać i poprawiać.

1. **Źródła przede wszystkim.** Opieramy się na ustawach, wyrokach, uchwałach, głosowaniach w Sejmie i nagraniach. Przy każdym ustaleniu jest link do źródła, a kopie najważniejszych dokumentów trzymamy w katalogu `zrodla`.
2. **Jeden agent AI pisze, osobny agent sprawdza.** Każdą notatkę przygotowuje jeden agent AI. Osobny agent, który nie widział jej powstawania, sprawdza źródła i wnioski. Zmiana trafia do bazy dopiero po jego akceptacji.
3. **Trudne pytania stawiamy kilku modelom osobno.** Porównujemy odpowiedzi, ale nie liczymy ich jak głosów. Zgodność modeli nie dowodzi prawdy.
4. **Fakty oddzielamy od ocen.** Każda ocena ma autora: sąd, stronę sporu albo nas.
5. **Błędy poprawiamy jawnie.** Pierwsze wersje, recenzje i korekty zostają w [historii prac](historia-prac.md).

Szczegóły: [jak sprawdzamy informacje](metodologia.md).

## Historia sporu

**[Cała historia krok po kroku](historia-sporu.md)**: od 1997 roku do dziś, w pełnych zdaniach, z linkiem przy każdym punkcie do szczegółów i źródła.

## Rozwiązania

- [Scenariusze naprawy](badania/scenariusze-naprawy.md): co jest w debacie, kto za tym stoi i kto jest przeciw.
- [Propozycje z debaty](badania/propozycje-na-stole.md): treść propozycji partii, Kancelarii Prezydenta i ekspertów.
- [Porównanie rozwiązań i odpowiedzialność](badania/odpowiedzialnosc-i-rozwiazania.md): ocena według jawnych kryteriów.
- [Siły i głosy w Sejmie](badania/sily-i-glosy.md): kto ile ma głosów i kto z kim ma potrzebną większość.
- [Bilans propozycji](badania/bilans-propozycji.md): kto zyskuje, a kto traci na każdej propozycji z debaty.
- [Rekomendacje modeli](badania/rekomendacje-modeli.md): co jako najlepsze rozwiązanie wybrały dwa modele AI, każdy osobno.

Wszystkie pozostałe notatki są w [liście analiz](analizy.md).

## Jak się dołączyć

- **Znalazłeś błąd albo brakujący dokument?** Zgłoś to w zakładce [Issues](https://github.com/gebawkubel/trybunal/issues) i podaj źródło.
- **Chcesz sprawdzić coś swoim modelem AI?** Wybierz pytanie z Issues i prześlij wynik. Instrukcja: [jak możesz pomóc](wspolpraca.md).
- **Szczegóły techniczne** (układ plików, kontrole, czytanie w Obsidianie): [informacje techniczne](techniczne.md).
