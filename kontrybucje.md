# Jak pomóc w projekcie

Możesz użyć swojego modelu AI, żeby sprawdzić nasze ustalenia albo znaleźć pominięte argumenty i dokumenty. Nie musisz zgadzać się z dotychczasowym wynikiem.

## Co trzeba zrobić

1. Wybierz pytanie z zakładki **Issues** na GitHubie. Jeśli chcesz zbadać coś nowego, dodaj tam zgłoszenie z krótkim opisem pytania.
2. Przekaż modelowi pytanie i wskazane dokumenty. Możesz też szukać dodatkowych źródeł. Zaznacz, które materiały dodałeś.
3. Zapisz odpowiedź i informacje wymienione poniżej w [szablonie analizy](szablony/analiza.md).
4. Prześlij pliki jako **Pull Request (PR)**, czyli propozycję dodania ich do repozytorium. Opiekun projektu sprawdzi je przed przyjęciem.

Docelowo przygotujemy gotową instrukcję dla AI, która pomoże zebrać materiały i przygotować pliki do wysłania. Jeszcze jej nie ma; najpierw sprawdzamy proces na pierwszym badaniu.

## Co dołączyć do analizy

- Link do badanego pytania w Issues.
- Nazwę modelu, datę analizy i ustawienia, które znasz.
- Dokładną treść polecenia przekazanego AI oraz listę użytych dokumentów i narzędzi.
- Odpowiedź z uzasadnieniem: co ją potwierdza, co jej przeczy i czego nie udało się ustalić.
- Linki do źródeł ze wskazaniem konkretnego miejsca, np. artykułu ustawy, strony wyroku lub minuty nagrania.
- Informację, ile razy uruchamiałeś analizę. Jeśli ją powtarzałeś, zachowaj wcześniejsze odpowiedzi i wyjaśnij dlaczego. Nie wybieraj tylko wyniku, który Ci odpowiada.

Jeśli czegoś nie znasz, napisz „nie wiem”. Nie wymyślaj brakujących danych. Potrzebujemy uzasadnienia odpowiedzi, nie ukrytego toku rozumowania modelu.

W szablonie jest też pole **SHA-256**. To techniczny identyfikator pozwalający sprawdzić, czy porównywane analizy dostały dokładnie te same materiały. Dla zestawu dostarczonego przez projekt przepisz podany identyfikator. Jeśli go nie ma, zaznacz brak; sposób jego wyliczania dopracujemy w pilotażu.

## Jak sprawdzamy zgłoszenie

Sprawdzamy, czy dokumenty rzeczywiście wspierają odpowiedź, czy uwzględniono argumenty przeciwne i czy opisano sposób wykonania analizy. Program dodatkowo sprawdza m.in. odnośniki i niezmienność zapisanych źródeł. Nie potrafi jednak dowieść, że użyto deklarowanego modelu ani że ujawniono wszystkie próby.

Dlatego przy wyniku zaznaczamy, czy mamy tylko opis autora, również zapis wykonania analizy, czy sami powtórzyliśmy badanie. Jeśli odrzucimy zgłoszenie, podamy powód. Odmienny wniosek sam w sobie nie jest powodem odrzucenia.

W podsumowaniach podajemy, ile analiz wykonano, jakich modeli użyto i ile wyników sami sprawdziliśmy przez powtórzenie. Sto zgodnych odpowiedzi może powielać ten sam błąd, więc sama liczba nie rozstrzyga sprawy.

## Czego nie wysyłać

Nie dołączaj haseł, kluczy API, danych prywatnych ani programów do uruchomienia. Przesyłasz dokumenty do oceny. Propozycje zmian w narzędziach projektu zgłaszaj osobno.

Dla opiekunów: przed uruchomieniem automatycznych kontroli zewnętrznego zgłoszenia sprawdźcie jego zawartość. Kod z takiego zgłoszenia nie może otrzymać sekretów ani uprawnień do zapisu w repozytorium.
