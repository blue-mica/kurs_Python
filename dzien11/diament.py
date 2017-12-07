class Zwierz(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def mow(self):
        print(f"Zwierzak {self.nazwa} nie mowi")

    def ruszaj_sie(self):
        print(f"Zwierzak {self.nazwa} rusza sie")


class Kon(Zwierz):
    def __init__(self, nazwa, umaszczenie):
        # super().__init__(nazwa)
        Zwierz.__init__(self, nazwa)
        self.umaszczenie = umaszczenie

    def mow(self):
        print(f"Kon {self.nazwa} mowi: iiiihaaaa")

    def ruszaj_sie(self):
        print(f"Kon {self.nazwa} hasa po lace")


class Osiol(Zwierz):
    def __init__(self, nazwa, st_upartosci):
        super().__init__(nazwa)
        self.st_upartosci = st_upartosci

    def ruszaj_sie(self):
        print(f"Osiol {self.nazwa} nie che sie ruszyc "
              f"przez najblizsze {self.st_upartosci} minut")


class Mul(Kon, Osiol):
    def __init__(self, nazwa, umaszczenie):
        Kon.__init__(self, nazwa, umaszczenie)
