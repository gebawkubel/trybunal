# Najlepsze rozwiązanie sporu o TK: odpowiedź na pytanie

Stan na 2026.11.04. Podsumowanie prac z [issue #38](https://github.com/gebawkubel/trybunal/issues/38).

Projekt sam nie wydaje rekomendacji. Ta notatka zbiera to, co powiedziały dwa modele AI, i to, co pokazuje bilans propozycji z debaty. Oceny są przypisane modelom, a liczby pochodzą z [notatki o siłach i głosach](sily-i-glosy.md).

## Pytanie

Gdybyś miał wybrać najlepsze i najbardziej sprawiedliwe rozwiązanie sporu o TK, które (1) zostałoby wdrożone zgodnie z prawem, tak żeby nikt go zaraz znowu nie zakwestionował, i (2) miałoby realną szansę, że strony sporu się na nie zgodzą, to co by to było?

## Odpowiedź modeli

Dwa modele, Fable High i Astra High, pracowały osobno i wskazały ten sam kierunek ([porównanie](rekomendacje-modeli.md)):
- **zmiana Konstytucji**, a nie zwykła ustawa;
- **bez resetu**: prawidłowo wybrani sędziowie, także ci z 2026 roku, zachowują urząd;
- **pakiet z Prezydentem**:
  - termin na ślubowanie, a po nim ślubowanie pisemne, gdy Prezydent go nie odbierze;
  - wybór sędziów większością 3/5 z losowaniem przy blokadzie;
  - ogłaszanie wyroków bez rządu;
  - ponowne rozpoznanie na wniosek spraw rozstrzygniętych z udziałem osób wybranych na zajęte miejsca.

Oba modele uzasadniają to warunkami z pytania.
- **Warunek 1, trwałość.** Zwykłą ustawę Prezydent może zawetować, a TK napisał w uzasadnieniu wyroku Kp 3/24, że ingerencja w skład TK wymaga zmiany Konstytucji ([warunki rozwiązań](warunki-rozwiazan.md)). Według modeli zmiana Konstytucji nie podlega zwykłemu wetu (Fable: "według przeważającego odczytania"; sporne jest, czy Prezydent może ją skierować do TK), a następna większość nie cofnie jej zwykłą ustawą.
- **Warunek 2, zgoda.** Zmiana Konstytucji wymaga 307 głosów przy pełnej sali. Bez KO wszyscy pozostali mają 304, więc KO jest niezbędna. Fable dodaje, że w resecie KO traci wszystkie swoje nominacje; Astra mówi ogólniej o koszcie ustępstwa dla KO. Najprostsza większość dla pakietu bez resetu to KO, PiS i PSL (335).

Oba modele oceniają szansę na zgodę stron nisko. Fable: "niska do średniej, około jeden na trzy". Astra: niska. Przeszkody, które wskazują:
- premier woli rozwiązanie bez zmiany Konstytucji (Astra);
- Marszałek Czarzasty zmiany Konstytucji odmawia (oba);
- Prezydent odkłada rozwiązanie do 2027 roku (oba);
- PiS może woleć poczekać na wybory (Fable).

## Co pokazuje bilans propozycji

[Bilans propozycji](bilans-propozycji.md) (GPT-6.1 Sol) ocenia 14 propozycji z debaty dla 14 sił. Wszystkie dostały ocenę szansy "niska", z jednym wyjątkiem: utrzymanie obecnej blokady ma szansę "wysoką", ale to nie jest naprawa. (Przy nowej ustawie bez zmiany Konstytucji bilans dodaje, że wysoka jest szansa na samo uchwalenie jej przez Sejm, ale nie na skuteczną reformę.) Wnioski bilansu:
- **KO jest konieczna dla każdej zmiany Konstytucji**, a w każdym konkretnym projekcie resetu (propozycje 3-9) jej bilans jest ujemny.
- **PiS nie jest arytmetycznie konieczny**, ale bez niego wskazana w bilansie konfiguracja (koalicja, Rozwój Plus, Konfederacja, Razem) ma 300 głosów i potrzebuje jeszcze 7. Wymaga też zgody Lewicy, która reset odrzuca.
- **Rozwój Plus jest języczkiem u wagi przy odrzucaniu weta.** Koalicja z nim ma 279, a bez niego i bez PiS jest 273, o 3 za mało do 276.

Bilans powstał później i niezależnie od rekomendacji, ale jego wynik zgadza się z ich głównym argumentem przeciw resetowi: KO, bez której nie ma 307 głosów, traci w każdym konkretnym projekcie resetu z debaty. A reset to większość propozycji z debaty.

W [issue #57](https://github.com/gebawkubel/trybunal/issues/57) bilans uzupełniono o dwie propozycje spoza debaty:
- **15. Reset z zachowaniem sędziów z 2026 roku**, z [symulacji negocjacji](symulacja/wyniki.md). Bilans KO jest tu mieszany, a nie ujemny;
- **16. Pakiet modeli**, czyli wąska zmiana Konstytucji bez resetu i kompromis z Prezydentem. Bilans KO jest dodatni.

Obie propozycje mają według bilansu szansę "niską". Brakuje tekstu przepisów i potwierdzonej zgody stron, a porozumienie postaci AI w symulacji nie jest porozumieniem prawdziwych stron.

## Czego to nie przesądza

- To opinie modeli. Zgodność dwóch modeli nie dowodzi, że mają rację, a oba czytały to samo repozytorium.
- Nie znamy stanowiska PiS wobec zmiany Konstytucji ani gotowości Prezydenta do firmowania takiego pakietu.
- Ocena może się zmienić po:
  - zmianie stanowiska KO albo Lewicy wobec zmiany Konstytucji;
  - deklaracji PiS;
  - nowej opinii Komisji Weneckiej;
  - zbliżaniu się wyborów w 2027 roku.

Uwagi i inne odpowiedzi można zgłaszać w [Issues](https://github.com/gebawkubel/trybunal/issues). Instrukcja: [jak możesz pomóc](../wspolpraca.md).
