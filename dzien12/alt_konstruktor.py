class Pracownik(object):

    ilosc_instancji = 0
    roczna_podw = 7

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        Pracownik.ilosc_instancji += 1

    @classmethod
    def zmien_roczna_podwyzka(cls, nowa_wartosc):
        if type(nowa_wartosc) != type(int):
            return
        if nowa_wartosc > 18:
            cls.roczna_podw = 18
        else:
            cls.roczna_podw = nowa_wartosc

    @staticmethod
    def sprawdz_pesel(pesel):
        if len(pesel) != 11:
            print("Nieprawidlowy PESEL")
        else:
            print("PESEL OK")

    @classmethod  # alternatywny konstruktor
    def Pracownik(cls, imie, nazwisko,):
        # tworzymy obiekt tymczasowy
        temp_pracownik = Pracownik(imie, nazwisko, 13)
        # dostosowujemy
        temp_pracownik.roczna_podw = 10
        # zwracamy go
        return temp_pracownik


    # def __str__(self):
    #     return f" Pracownik {self.nazwisko} ma {self.stawka} PLN nr {Pracownik.ilosc_instancji}" \
    #            f"dostanie "

    def __str__(self):
        return f" Pracownik {self.imie}  {self.nazwisko} ma {self.stawka}"

    def __del__(self):
        Pracownik.ilosc_instancji -= 1
        print(f"Pracownik {self.nazwisko} zostal usuniety")
