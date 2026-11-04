# Bilans propozycji: dopisać scenariusze, które rozwiązują spór, z symulacji i rekomendacji modeli

Prośba prowadzącego (2026.11.04), dosłownie:

> to byla tylko ciekaostka - jesli pojawil ysie jakies nowe scenariusze ktore rozwiazuja sprawe to nalezy je uwzglednic w tabelce gdzie rozwazamy wszystkie scenariusze i jak one wplywaja na dana opcje

"Tabelka" to macierz w [bilansie propozycji](https://github.com/gebawkubel/trybunal/blob/main/badania/bilans-propozycji.md) (#38): 14 propozycji z debaty i zysk albo strata każdej z 14 sił.

## Zadanie

1. Ustalić, które nowe scenariusze spoza debaty pojawiły się od powstania bilansu i realnie rozwiązują spór o TK, z uzasadnieniem. Kandydaci do oceny (wykonawca decyduje, które przyjąć, łączyć albo odrzucić):
   - wyniki [symulacji negocjacji](https://github.com/gebawkubel/trybunal/blob/main/badania/symulacja/wyniki.md) (#46): reset z zachowaniem sędziów z 2026 roku (przebieg 1); zmiana Konstytucji bez resetu (przebiegi 2, 8); zwykła ustawa 3/5 z krokami "na teraz" (3, 5, 7, 10); same kroki "na teraz" bez ustawy (4, 6, 9);
   - pakiet z [rekomendacji modeli](https://github.com/gebawkubel/trybunal/blob/main/badania/rekomendacje-modeli.md) (wąska zmiana Konstytucji bez resetu z kompromisem z Prezydentem), który bilans pominął, bo nikt go nie zgłosił w debacie;
   - scenariusze z części "Scenariusze z analiz AI" i "Scenariusze z symulacji negocjacji" w [scenariuszach naprawy](https://github.com/gebawkubel/trybunal/blob/main/badania/scenariusze-naprawy.md), jeśli rozwiązują spór.
2. Dopisać przyjęte scenariusze do macierzy i jako nowe sekcje "Propozycje po kolei", tą samą metodą i w tym samym formacie co istniejące 14 (te same 14 sił, zysk, strata, bilans, akt i próg). Wyraźnie oznaczyć pochodzenie: symulacja (wypowiedzi generowane przez model, nie stanowiska stron) albo analiza modeli, nie debata.
3. Uzupełnić "Wnioski" bilansu, jeśli nowe wiersze je zmieniają. Istniejących ocen 14 propozycji nie zmieniać, chyba że wynika to z nowych faktów; każdą zmianę opisać.

Zasady jak w #38: oceny to oceny wykonawcy, fakty ze źródłem w repozytorium, liczby z `badania/sily-i-glosy.md`. Polecenie wykonawcy to treść tego issue i jawna wiadomość techniczna; wynik przechodzi jawną recenzję przed scaleniem.


---

Wykonujesz zadanie z issue #57 (treść wyżej). Ta wiadomość jest tylko techniczna.

- Katalog roboczy to publiczne repozytorium gebawkubel/trybunal w wersji main 0ed9a42. Masz tylko odczyt, bez internetu. Przeczytaj AGENTS.md, `badania/bilans-propozycji.md` i pliki wskazane w issue.
- Jako ostatnią wiadomość zwróć wyłącznie pełną nową treść pliku `badania/bilans-propozycji.md` w Markdown, od pierwszej linii do ostatniej, gotową do zastąpienia obecnego pliku. Bez komentarza przed ani po. Zmiany względem obecnej wersji opisz w nagłówku pliku (jedno, dwa zdania) albo w nowej krótkiej sekcji na końcu.
- Pisz po polsku, krótko i zrozumiale dla laika. Używaj tylko krótkiego łącznika (-), nigdy pauzy ani półpauzy, i prostych apostrofów. Daty w formacie yyyy.mm.dd.
