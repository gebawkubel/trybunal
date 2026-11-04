> Polecenie dla obu modeli: poprawka po recenzji. Do polecenia dołączono recenzję i roboczą wersję notatki o propozycjach. Fable dostał potem dodatkowo [trzy sprostowania](sprostowania-dla-fable.md), Astra nie. Napisał koordynator (Claude Opus 5.5). Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `d33b2a71de5af39018e6fccf20e65d8482666fe251fa5b369c5ae1d5d337f608`. Katalog `propozycje/` i plik `propozycje-na-stole.md` wymienione w tekście to robocza wersja notatki o propozycjach, przekazana modelowi przed jej recenzją; po poprawkach trafiła do repozytorium jako [propozycje z debaty](../propozycje-na-stole.md) z kartami w `zrodla/okres-2024-2026/`.
> Porównanie obu rekomendacji: [rekomendacje modeli](../rekomendacje-modeli.md).

---

# Polecenie: poprawka rekomendacji po recenzji

Dostajesz recenzję swojej rekomendacji przygotowaną przez inny model oraz nowy materiał: notatkę o treści propozycji naprawy TK (katalog propozycje/, plik propozycje-na-stole.md i karty źródeł). Notatka jest w recenzji projektu i nie została jeszcze zatwierdzona; traktuj ją jak źródło do sprawdzenia, nie jak pewnik.

Zadanie:
1. Popraw każdy punkt oznaczony BŁĄD, chyba że wykażesz z repozytorium, że recenzent się myli. Wtedy napisz dlaczego.
2. Przy punktach WĄTPLIWE i UWAGA zdecyduj: poprawiasz albo zostawiasz z uzasadnieniem.
3. Uwzględnij nowy materiał o propozycjach. Zwłaszcza sprawdź, czy Twoja ocena "czy to już jest w debacie" i bilans dla PSL, Konfederacji, Rozwoju Plus, Razem i Prezydenta nadal się trzyma, skoro większość propozycji przewiduje reset.
4. Możesz zmienić rekomendację, jeśli uznasz to za słuszne. Napisz wtedy wprost, co zmieniłeś i dlaczego.

Format: pełna nowa wersja rekomendacji w tym samym formacie co poprzednio (punkty 1-9), a na końcu sekcja "10. Co zmieniłem po recenzji": lista punktów recenzji z decyzją (poprawione / zostawione, z jednym zdaniem uzasadnienia). Po polsku, zwykłym łącznikiem, proste apostrofy, najwyżej około 1800 słów bez sekcji 10.
