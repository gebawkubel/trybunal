> Treść issue #46 z komentarzami, pobrana z GitHuba w chwili zlecenia etapu 1 i przekazana wykonawcy jako polecenie. Tekst pod linią jest identyczny z oryginałem. SHA-256 oryginału: `87b17221569d2b4c2fb0229d72aa7f1f4c2e64a9c8a1c5155da663b2deb3dfe8`.

---

# Issue #46: Symulacja negocjacji: zamknięte spotkanie kluczowych graczy sporu o TK

Pobrano z https://github.com/gebawkubel/trybunal/issues/46 (treść i komentarze, stan na chwilę zlecenia).

## Pomysł

Symulujemy zamknięte spotkanie osób, od których naprawdę zależy rozwiązanie sporu o TK. Każdą osobę gra osobny agent AI. Wszyscy piszą w jednym wspólnym wątku, po jednej wypowiedzi naraz: po swojej wypowiedzi agent czeka na odpowiedź innych. Zadanie przy stole: wypracować porozumienie. Wynik "brak porozumienia" też jest dozwolony i uczciwy.

To nie jest przewidywanie, co zrobią prawdziwi ludzie. Symulacja sprawdza, które porozumienia w ogóle da się złożyć, gdy każda strona broni swojego interesu i ma realne narzędzia.

## Zasady

- **Skład stołu ustala model w ramach zadania**, nie człowiek. Najpierw analizuje, kto ma realne weto albo wpływ na wynik w każdej ścieżce (zwykła ustawa, zmiana Konstytucji, porozumienie bez ustawy). Zaprasza tylko takie osoby, bez zbędnych gości. Uzasadnienie składu publikujemy. Model może zaproponować różne składy dla różnych wariantów.
- **Prawdziwe nazwiska.** Każda wypowiedź jest podpisana np. "Karol Nawrocki (postać symulowana przez AI)". Każdy zapis zaczyna się informacją, że to symulacja, a nie słowa tych osób. Stanowiska wyjściowe postaci mają źródła z prawdziwych wypowiedzi.
- **Karty postaci.** Jest wspólny pakiet wiedzy dla wszystkich i prywatna karta, którą widzi tylko dana postać. Karta zawiera:
  - kim postać jest i jakimi narzędziami dysponuje;
  - ile ma głosów;
  - czerwone linie;
  - co zyskuje, jeśli porozumienia nie będzie;
  - przed kim odpowiada.
- **Pakiet wiedzy:** historia sporu, propozycje z debaty, siły i głosy, warunki prawne. Bez internetu, ze stanem wiedzy na stały dzień. Bez rekomendacji modeli, bilansu i scenariuszy AI, żeby nie zakotwiczać. Wynik porównamy z nimi dopiero potem.
- **Arbiter.** Osobny agent, który nie negocjuje. Pilnuje kolejności wypowiedzi i sprawdza, czy uzgodniony pakiet ma głosy (231, 276, 307, Senat) i jest zgodny z procedurą.
- **Równe modele** dla wszystkich postaci (np. Claude Opus 5.5). Seria kontrolna na innym modelu sprawdzi, czy wynik nie zależy od modelu.
- **Warianty motywacji**, np.:
  - (a) dobro państwa ponad wszystko;
  - (b) ugraj jak najwięcej dla swojego środowiska i jak najmniej strać, ale ostatecznie kieruj się dobrem państwa;
  - (c) czysty interes polityczny jako punkt odniesienia.
- **Kilka przebiegów na wariant**, bo jeden przebieg to anegdota.

## Budżet

- Limit zatwierdzony 2026.11.04: najwyżej około 100$ z kredytów API. Seria kontrolna na innym modelu przez Codex, poza tym limitem.
- **Najpierw jeden pełny przebieg**, nie skrócona próba: pełny skład, pełne karty, wariant (b), do porozumienia albo jawnego braku porozumienia. Po nim prowadzący decyduje, czy uruchamiamy kolejne, na podstawie tego, czy symulacja działa i ile realnie kosztowała.
- **Lista wszystkich planowanych przebiegów powstaje od razu**, przed pierwszym przebiegiem: wariant motywacji, skład, model, kolejność, szacowany koszt każdego. Docelowo 3 warianty po 3 przebiegi, chyba że analiza składu uzasadni inny plan.
- Szacunek kosztu robi agent, który buduje skrypt: przed próbą z założeniami (liczba postaci i wypowiedzi, kontekst, cache), po próbie z kosztem zmierzonym z `usage` w odpowiedziach API. Na tej podstawie proponuje liczbę przebiegów w limicie.
- Przekroczenie limitu wymaga nowej zgody.

## Przejrzystość

- Jedynym źródłem wytycznych jest ten issue. Agent wykonujący etap dostaje jako polecenie dosłowną treść tego issue (z komentarzami) i krótką wiadomość techniczną: gdzie jest repozytorium, gdzie zapisać wynik. Obie publikujemy razem z wynikiem, z sumami SHA-256.
- Nikt, także prowadzący projekt i koordynator, nie przekazuje agentom wytycznych poza tym issue. Uwaga albo zmiana (np. "dodaj osobę X") trafia najpierw jako publiczny komentarz tutaj, z uzasadnieniem, i dopiero wtedy obowiązuje.
- Wyniki etapów (skład, karty, plan) nie są przez nikogo poprawiane merytorycznie poza jawną recenzją. Poprawki po recenzji robi autor etapu, a raport recenzji jest publiczny.

## Etap 1: skład stołu i plan przebiegów

Wykonawca:
1. Dla każdej ścieżki rozwiązania (zwykła ustawa, ustawa przy wecie Prezydenta, zmiana Konstytucji, porozumienie polityczne bez ustawy, inne wskazane w repozytorium) wypisuje, kto ma w niej weto albo jest niezbędny, z liczbą głosów i podstawą prawną.
2. Wybiera, kto siedzi przy stole i kto reprezentuje dany obóz (z imienia i nazwiska, według repozytorium), z uzasadnieniem dla każdej osoby i dla każdej pominiętej osoby, która mogłaby wydawać się potrzebna.
3. Proponuje skład podstawowy i ewentualne składy wariantowe.
4. Przygotowuje listę wszystkich planowanych przebiegów zgodnie z sekcją "Budżet".
5. Wypisuje luki w repozytorium, które utrudnią karty postaci.

Materiał: repozytorium w wersji podanej w wiadomości technicznej, bez internetu. Wykonawca nie czyta wniosków, które mogłyby zakotwiczyć symulację: `badania/rekomendacje-modeli.md`, `badania/rekomendacje/`, `badania/bilans-propozycji.md`, `badania/odpowiedz.md`. Fakty z nazwą pliku, oceny oznaczone jako oceny. Pisze dla osoby bez wiedzy prawniczej, po polsku, zwykłym łącznikiem.

## Etapy

- [ ] Analiza składu stołu i wariantów (model), z recenzją
- [ ] Pakiet wiedzy i karty postaci ze źródłami (w tym materiał z #45), z recenzją
- [ ] Skrypt prowadzący rozmowę i arbitra
- [ ] Lista wszystkich planowanych przebiegów z szacunkiem kosztu
- [ ] Jeden pełny przebieg; raport: czy działa, koszt zmierzony z `usage`, co poprawić
- [ ] Decyzja prowadzącego o kolejnych przebiegach
- [ ] Pozostałe przebiegi z listy, w limicie budżetu
- [ ] Publikacja zapisów z kartami, poleceniami i sumami kontrolnymi; porównanie wyników z rekomendacjami modeli i bilansem (#38)




## Komentarze

(brak)
