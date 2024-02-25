class Produkt:
    def __int__(self, rozmiar, waga):
        self.rozmiar = rozmiar
        self.waga = waga

    def inf(self):
        print(f"Rozmiar: {self.rozmiar}")
        print(f"Waga: {self.waga}")


class Manga(Produkt):
    def __init__(self, rozmiar, waga, nazwa, numer_wydania, fabula):
        super.__init__(rozmiar, waga)
        self.nazwa = nazwa
        self.numer = numer_wydania
        self.fabula = fabula

    def inf(self):
        super(Manga, self).inf()
        print(f"Nazwa: {self.nazwa}")
        print(f"Numer wydania: {self.numer}")
        print(f"Fabula: {self.fabula}")


class Figurki(Produkt):
    def __init__(self, rozmiar, waga, wyglad):
        super.__init__(rozmiar, waga)
        self.wyglad = wyglad

    def inf(self):
        super(Figurki, self).inf()
        print(f"Wyglad: {self.wyglad}")