#klasa Vehicle
class Vehicle:

    #konstruktor klasy Vehicle
    def __init__(self, nazwa: str, rok_produkcji: int, przebieg: int):
        self.nazwa = nazwa
        self._rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    #wykorzystanie dekoratora który jest getterem, dzięki czemu można dostać się do atrybutu również w miejscu wykorzystania klasy
    #a nie tylko w samej klasie
    @property
    def rok_produkcji(self):
        return self._rok_produkcji
    
    #definicje funkcji klasy
    def is_old(self):
        if (self.rok_produkcji < 2010):
            return "Pojazd jest stary"
        else:
            return "Pojazd nie jest stary"
        
    def is_long_mileage(self):
        if (self.przebieg > 100000):
            return "Pojazd ma duży przebieg"
        else:
            return "Pojazd ma mały przebieg"
        
#kklasa Car dziedziczy po klasie Vehicle
class Car(Vehicle):
    
    def __init__(self, nazwa: str, rok_produkcji: int, przebieg: int):
        super().__init__(nazwa, rok_produkcji, przebieg)

    @property
    def rok_produkcji(self):
        return self._rok_produkcji

    def is_old(self):
        if (self.rok_produkcji < 2010):
            return "Samochód jest stary"
        else:
            return "Samochód nie jest stary"
        
    def is_long_mileage(self):
        if (self.przebieg > 100000):
            return "Samochód ma duży przebieg"
        else:
            return "Samochód ma mały przebieg"
        

if __name__ == '__main__':

    #utworzenie trzech obiektów utworzonych klas
    pojazd = Vehicle('Volvo', 2012, 130000)
    print(f"Pojazd Został wyprodukowany w {pojazd.rok_produkcji}")
    print(pojazd.is_old())
    print(pojazd.is_long_mileage())

    samochod = Car('Skoda', 2008, 60000)
    print(f"Samochód Został wyprodukowany w {samochod.rok_produkcji}")
    print(samochod.is_old())
    print(samochod.is_long_mileage())

    samochod_dziedziczacy = Car(pojazd.nazwa, pojazd.rok_produkcji, pojazd.przebieg)
    print(f"Samochód Został wyprodukowany w {samochod_dziedziczacy.rok_produkcji}")
    print(samochod_dziedziczacy.is_old())
    print(samochod_dziedziczacy.is_long_mileage())