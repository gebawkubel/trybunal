> Polecenie dla modelu: skład stołu do symulacji. Napisał koordynator (Claude Opus 5.5). Wynik: [analiza składu](sklad-stolu.md). Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `e3647191f9ffe7127ba3a9575290bf7aa0da706dc000f2d8c46ea3cac80e12d5`.

---

# Polecenie: skład stołu do symulacji negocjacji o TK

Materiał: repozytorium bazy wiedzy o sporze wokół TK (katalog podany przez zlecającego). Najważniejsze pliki: historia-sporu.md, badania/sily-i-glosy.md, badania/warunki-rozwiazan.md, badania/propozycje-na-stole.md, badania/scenariusze-naprawy.md (tylko części o stanowiskach stron i indeks stron), zrodla/konstytucja.md. Nie szukaj w internecie. Nie czytaj badania/rekomendacje-modeli.md, badania/rekomendacje/, badania/bilans-propozycji.md ani badania/odpowiedz.md: symulacja ma działać bez tych wniosków, a Ty projektujesz jej skład.

## Kontekst

Planujemy symulację zamkniętego spotkania osób, od których zależy rozwiązanie sporu o TK. Każdą osobę gra osobny agent AI. Wszyscy piszą w jednym wątku, po jednej wypowiedzi naraz. Zadanie przy stole: wypracować porozumienie (brak porozumienia jest dozwolonym wynikiem). Osobny arbiter, który nie negocjuje, sprawdza głosy i procedurę. Opis: issue #46.

## Zadanie

Ustal, kogo zaprosić. Zasada: tylko osoby, które mają realną możliwość wpłynięcia na kształt lub wynik rozwiązania. Każdy nadmiarowy gość jest błędem, ale pominięcie kogoś z realnym wetem też.

1. **Ścieżki rozwiązania.** Dla każdej ścieżki (zwykła ustawa; ustawa przy wecie Prezydenta; zmiana Konstytucji; porozumienie polityczne bez ustawy, np. ślubowania; inne, jeśli repozytorium je wskazuje) wypisz, kto ma w niej weto albo jest niezbędny: osoby i instytucje, z liczbą głosów i podstawą prawną.
2. **Kandydaci.** Dla każdego kandydata (np. Prezydent, Premier i lider KO, lider PiS, liderzy PSL, Lewicy, Polski 2050, Centrum, Rozwoju Plus, Konfederacji, Razem, Marszałek Sejmu, Marszałek Senatu, Prezes TK lub sędziowie TK, inni wskazani w repozytorium): czy zaprosić, w jakiej roli, dlaczego, i co się stanie, jeśli go zabraknie. Rozstrzygnij, kto reprezentuje dany obóz (osoba z imienia i nazwiska, według repozytorium, z datą stanowiska). Gdy partia ma wielu decydentów, wybierz jednego i uzasadnij.
3. **Skład podstawowy** i ewentualnie **składy wariantowe** (np. inny skład dla ścieżki konstytucyjnej i dla porozumienia bez ustawy), z uzasadnieniem, ile osób i dlaczego nie mniej i nie więcej.
4. **Warianty symulacji:** jakie warianty motywacji i składu proponujesz uruchomić i w jakiej kolejności, jeśli budżet pozwala na około 9-12 przebiegów łącznie (każdy przebieg kilkadziesiąt wypowiedzi). Punkt wyjścia do oceny: (a) dobro państwa ponad wszystko; (b) ugraj jak najwięcej dla swojego środowiska i jak najmniej strać, ale ostatecznie kieruj się dobrem państwa; (c) czysty interes polityczny.
5. **Czego nie wiemy:** luki w repozytorium, które utrudniają przygotowanie kart postaci (np. brak stanowiska danej osoby).

## Format

Po polsku, Markdown, najwyżej około 2500 słów. Fakty z nazwą pliku; oceny oznaczaj jako oceny. Liczby przy pełnej sali. Pisz dla osoby bez wiedzy prawniczej. Nie używaj długiego myślnika ani półpauzy, tylko zwykłego łącznika; proste apostrofy.
