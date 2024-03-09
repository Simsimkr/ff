class Osoba: 
    def __init__(self, imie, nazwisko, wiek) -> None: 
        self.imie = imie 
        self.nazwisko = nazwisko 
        self.wiek = wiek

    def info(self):
        print(f"Imie - {self.imie}")
        print(f"Nazwisko - {self.nazwisko}")
        print(f"Wiek - {self.wiek}")

    def edytuj_imie(self, nowe_imie):
        self.imie = nowe_imie

    def edytuj_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def edytuj_wiek(self, nowe_wiek):
        self.wiek = nowe_wiek


class Pracownik:
    def __init__(self, osoba: Osoba, obowiazki):
        self.osoba = osoba
        self.obowiazki = obowiazki

    def info(self):
        self.osoba.info()
        print(f"Obowiazki - {self.obowiazki}")

    def edytuj_obowiazki(self, nowe_obowiazki):
        self.obowiazki = nowe_obowiazki


class Manager:
    def __init__(self, pracownik: Pracownik, zarzadzane_dzialy):
        self.pracownik = pracownik
        self.zarzadzane_dzialy = zarzadzane_dzialy

    def info(self):
        self.pracownik.info()
        print(f"Zarzadzane dzialy - {self.zarzadzane_dzialy}")

    def edytuj_zarzadzane_dzialy(self, nowe_zarzadzane_dzialy):
        self.zarzadzane_dzialy = nowe_zarzadzane_dzialy


class Developer:
    def __init__(self,  pracownik: Pracownik, jezyk_programowania):
        self.pracownik = pracownik
        self.jezyk_programowania = jezyk_programowania

    def info(self):
        self.pracownik.info()
        print(f"Jezyk programowania - {self.jezyk_programowania}")

    def edytuj_jezyk_programowania(self, nowy_jezyk_programowania):
        self.jezyk_programowania = nowy_jezyk_programowania


class Ksiegowosc:
    def __init__(self, pracownik: Pracownik, doswiadczenie):
        self.pracownik = pracownik
        self.doswiadczenie = doswiadczenie

    def info(self):
        self.pracownik.info()
        print(f"Doswiadczenie - {self.doswiadczenie} lat")

    def edytuj_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie


class PomocSprzatajaca:
    def __init__(self, pracownik: Pracownik, staz):
        self.pracownik = pracownik
        self.staz = staz

    def info(self):
        self.pracownik.info()
        print(f"Staz - {self.staz} miesiecy")

    def edytuj_staz(self, nowy_staz):
        self.staz = nowy_staz


class Hardware:
    def __init__(self, pracownik: Pracownik, specjalizacja):
        self.pracownik = pracownik
        self.specjalizacja = specjalizacja

    def info(self):
        self.pracownik.info()
        print(f"Specjalizacja - {self.specjalizacja}")

    def edytuj_specjalizacja(self, nowa_specjalizacja):
        self.specjalizacja = nowa_specjalizacja


class Admin:
    def __init__(self, pracownik: Pracownik, narzedzia_administracyjne):
        self.pracownik = pracownik
        self.narzedzia_administracyjne = narzedzia_administracyjne

    def info(self):
        self.pracownik.info()
        print(f"Narzedzia administracyjne - {self.narzedzia_administracyjne}")

    def edytuj_narzedzia_administracyjne(self, nowe_narzedzia_administracyjne):
        self.narzedzia_administracyjne = nowe_narzedzia_administracyjne


osoba1 = Osoba("John", "Germanski", 50)
pracownik1 = Pracownik(osoba1, "pracowac")
pracownik1.info()
