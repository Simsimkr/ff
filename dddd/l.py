class Osoba:
    def __init__(self, imie, nazwisko, rok):
        self.imie = imie
        self.nazwisko = nazwisko
        self.rok = rok

    def inf(self):
        print(f"Imie: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Rok: {self.rok}")


class Klijent(Osoba):
    def __init__(self, imie, nazwisko, rok, kasa):
        super().__init__(imie, nazwisko, rok)
        self.kasa = kasa

    def pokaz_kase(self):
        print(f"kas: {self.kasa}")


class Pracownik(Osoba):
    licznik = 0
    def __init__(self, imie, nazwisko, rok, zarobek):
        super().__init__(imie, nazwisko, rok)
        Pracownik.licznik += 1
        self.numer = Pracownik.licznik
        self.zarobek = zarobek


class Sprzedawca(Pracownik):
    def __init__(self, imie, nazwisko, rok, numer_kasy, zarobek):
        super().__init__(imie, nazwisko, rok, zarobek)
        self.numer_kasy = numer_kasy

    def inf(self):
        super(Sprzedawca, self).inf()
        print(self.numer_kasy)
        print(f"Zarobek: {self.zarobek}")


class Sprzataczka(Pracownik):
    def __init__(self, imie, nazwisko, rok, zarobek):
        super().__init__(imie, nazwisko, rok, zarobek)

    @staticmethod
    def strantnij():
        print("spranta")