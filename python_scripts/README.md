# Moje Skrypty

Ten repozytorium zawiera 10 skryptów Python wykonanych w ramach różnych zadań. Poniżej znajdziesz krótki opis każdego skryptu wraz z linkami do dokumentacji i wynikami działania.

## Lista Skryptów

### Skrypt 1

Opis: Skrypt 1 sprawdza, czy podany znak jest liczbą. Skrypt pokazuje jak można wykonać to za pomocą dwóch metod, wykorzystując funkcję isdigit oraz isinstance. 

Korzysta z [windows-curses](https://pypi.org/project/windows-curses/).

Wynik działania:

```bash
python skrypt1_24006.py

Podaj znak: 23
Sposób isdigit
Podany pierwszy znak to: liczba
Sposób isinstance
Podany pierwszy znak to: liczba

Sposób isdigit
Podany pierwszy znak to: nie liczba
Sposób isinstance
Podany pierwszy znak to: nie liczba
```
### Skrypt 2

Opis: Skrypt 2 sprawdza, czy podany ciąg znaków jest liczbą. Za pomocą funkcji isdigit skrypt sprawdzxa każdy znak po kolei, następnie za pomocą metody all, sprawdza ,czy wszystkie znaki są cyframi. 

Korzysta z [windows-curses](https://pypi.org/project/windows-curses/).

Wynik działania:

```bash
python skrypt2_24006.py

Proszę podać ciąg znaków składającty się conajmniej z dwócz znaków: 23523456
Podany ciąg znaków jest liczbą.

Proszę podać ciąg znaków składającty się conajmniej z dwócz znaków: 1234dftggf2
Podany ciąg znaków nie jest liczbą.
```

### Skrypt 3

Opis: Skrypt 3 znajduje indeks pierwszego pojawienia się szukanego wyrazu w ciągu znaków. Wykorzystuje do tego funkcję find, która zwraca indeks po pierwszym znalezieniu. W przypadku nie znalezienia powtórzenia funkcja ta zwraca -1. 

Korzysta z [find()](https://docs.python.org/3/library/stdtypes.html#string-methods).

Wynik działania:

```bash
python skrypt3_24006.py

Proszę podać ciąg znaków: Cześć hej jak się masz?
Proszę podać szukany ciąg znaków: jak
Szukany ciąg znaków znajduje się na indeksie: 10
```

### Skrypt 4

Opis: Skrypt 4 znajduje indeksy wszystkich powtórzeń szukanego słowa w danym ciągu znaków. Skrypt wykorzystuje funkcję split, która dzieli ciąg na mniejsze ciągico każde wystąpenie danej frazy. Skrypt zlicza długości powstałych ciągów oraz dodaje długość szukanego wyrazu, dzięki czemu może obliczyć wszystkie indeksy szukanego wyrazu.

Korzysta z [split()](https://docs.python.org/3/library/stdtypes.html#string-methods).

Wynik działania:

```bash
python skrypt4_24006.py

Proszę podać ciąg znaków: hej jak tam hej, witam hej co tam 
Proszę podać szukany ciąg znaków: hej
Szukany ciąg znaków znajduje się na indeksach: [0, 12, 23]
```

### Skrypt 5

Opis: Skrypt 5 wypisuje pierwiastki liczb od 1 do 256 (włącznie), jeśli są one podzielne przez 2. Skrypt wykonuje to na dwa sposoby. Pierwszy sposób wykorzystje pętle, natomiast drugi sposób jest skrócony i wykorzystuje tzw. list comprenhension, który zmienia listę na nową według podanych warunków. 

Korzysta z [math](https://docs.python.org/3/library/math.html).

Wynik działania:

```bash
python skrypt5_24006.py

Program szuka pierwiastków liczb od 1 do 256 (włącznie) podzielnych bez reszty przez 2.
Za pomocą math: [2, 4, 6, 8, 10, 12, 14, 16]
Za pomocą list comprehensions: [2, 4, 6, 8, 10, 12, 14, 16]
```

### Skrypt 6

Opis: Skrypt 6 tworzy słownik o kluczach 10-20. Kluczom przypisywane są losowe ciągi znaków generowane za pomocą funkcjom: random i string. Funkcja random pozwala losować znaki z puli zdefiniowanej dzięki funkcji string. 

Korzysta z [random](https://docs.python.org/3/library/random.html) i [string](https://docs.python.org/3/library/string.html).

Wynik działania:

```bash
python skrypt6_24006.py

Program wypisuje random słownik.
Słownik:
{'10': 'KRUvbuj1', '11': 'HfhcV03W', '12': 'bTxgRAnR', '13': '0fg7zIvq', '14': 'Hjfrjj9o', '15': 'W05Z3F4Q', '16': 'w96UbIBb', '17': 'gMZTw9b3', '18': 'w8toMKeP', '19': '2T24wvHA', '20': 'RYdX8rXe'}
```

### Skrypt 7

Opis: Skrypt 7 wykorzystuje funkcje znajdujące się w innym pliku w innym folderze. Funkcje te importowane są klauzulą import. W zadaniu wykorzystano 4 funkcje modułu math. 

Korzysta z [math](https://docs.python.org/3/library/math.html).

Wynik działania:

```bash
python skrypt7_24006.py

Proszę podać liczbę na której wykonane zostaną funkcje: pierwiastek, potęga, cosinus i sinus: 
5
Pierwiastek z liczby 5: 2.23606797749979

Potęga liczby 5: 25.0

Cosinus z liczby 5: 0.28366218546322625

Sinus z liczby 5: -0.9589242746631385
```

### Skrypt 8

Opis: Skrypt 8 genruje ciąg losowych 100 znaków podobnie jak w skrypcie 6. Skrypt następnie za pomocą funkcji Counter tworzy słownik z kluczami o znakach występujących w ciągu i wartościach odpowiadającym ilość powtórzeń się danego znaku. Skrypt tworzy też listę unikalnych znaków tego ciągu.

Korzysta z [Counter()](https://docs.python.org/3/library/collections.html#collections.Counter).

Wynik działania:

```bash
python skrypt8_24006.py

Wygenerowany ciąg 100 randomowych znaków: GYFpddj4dATkTyOtPlOQSVGvenHlJghZR0rT0H8tSehtk4woj5LYgIFdvPX9I1rgb3ZKHEd4y6TYd9wTObwunEEYNKsvTKhsXsG0

Wygenerowany słownik: {'G': 3, 'Y': 4, 'F': 2, 'p': 1, 'd': 6, 'j': 2, '4': 3, 'A': 1, 'T': 6, 'k': 2, 'y': 2, 'O': 3, 't': 3, 'P': 2, 'l': 2, 'Q': 1, 'S': 2, 'V': 1, 'v': 3, 'e': 2, 'n': 2, 'H': 3, 'J': 1, 'g': 3, 'h': 
3, 'Z': 2, 'R': 1, '0': 3, 'r': 2, '8': 1, 'w': 3, 'o': 1, '5': 1, 'L': 1, 'I': 2, 'X': 2, '9': 2, '1': 1, 'b': 2, '3': 1, 'K': 3, 'E': 3, '6': 1, 'u': 1, 'N': 1, 's': 3}

Wygenerowana lista unikalnych znaków: ['G', 'Y', 'F', 'p', 'd', 'j', '4', 'A', 'T', 'k', 'y', 'O', 't', 'P', 'l', 'Q', 'S', 'V', 'v', 'e', 'n', 'H', 'J', 'g', 'h', 'Z', 'R', '0', 'r', '8', 'w', 'o', '5', 'L', 'I', 'X', '9', '1', 'b', '3', 'K', 'E', '6', 'u', 'N', 's']
```

### Skrypt 9

Opis: Skrypt 9 tworzydwie klasy. Klasę Vehicle z atrybutami nazwa, rok_produkcji i przebieg oraz dwoma metodami. Klasa Car dziedziczy po klasie Vehicle. W klasach wykorzystano również decorator @property, który jest getterem atrybutu. Dzięki decoratorowi można dostać się do atrybutu poza klasą. W skrypcie tworzone są 3 obiekty o klasach Vehicler, Car i trzecai dziedziczy po klasie Vehicle i wyświetla o nich informacje.


Wynik działania:

```bash
python skrypt9_24006.py

Pojazd Został wyprodukowany w 2012
Pojazd nie jest stary
Pojazd ma duży przebieg
Samochód Został wyprodukowany w 2008
Samochód jest stary
Samochód ma mały przebieg
Samochód Został wyprodukowany w 2012
Samochód nie jest stary
Samochód ma duży przebieg
```

### Skrypt 10

Opis: Skrypt 10 generuje alfabet, a następnie zapisuje go do plików alfabet1 w jednej linii oraz alfabet2, gdzie każda literka jest pod sobą. Skrypt wykorzystuje funkcje write która zapisuje ciąg znaków do pliku oraz menedżer kontekstu with, dzięki któremu po wykonaniu bloku kodu wewnątrz with, zostaną uwolnione zasoby (w tym przypadku plik alfabet1 i plik alfabet2).

Korzysta z [write()](https://docs.python.org/3/library/io.html#io.TextIOBase.write) i [with](https://docs.python.org/3/reference/compound_stmts.html#with).

Wynik działania:

```bash
python skrypt10_24006.py

Zapisano poprawnie
```

## Uwagi

- Wszystkie skrypty zostały napisane w języku Python w wersji 3.x.
- Wyniki działania skryptów są przedstawione jako przykładowe wywołania z odpowiednimi wynikami.
- Jeśli potrzebujesz dodatkowych informacji, proszę skontaktować się ze mną.
