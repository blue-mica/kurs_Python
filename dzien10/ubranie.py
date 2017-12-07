class Ubranie(object):
    def __init__(self, id, kolor, marka):
        self.nazwa = id
        self.kolor = kolor
        self.marka = marka


class But(Ubranie):
    def __init__(self, id, kolor, marka, rozmiar, plec):
        super().__init__(id, kolor, marka) # tutaj sa zawsze parametry dziedziczone z klasy nadrzednej
        self.rozmiar = rozmiar
        self.plec = plec

    def __str__(self):
        return f"But {self.kolor} marki {self.marka}"


class OdziezWierzchnia(Ubranie):
    def __init__(self, id, kolor, marka, material):
        super().__init__(id, kolor, marka)
        self.material = material


class Szpilka(But):
    def __init__(self, wysokosc):
        super().__init__("czarny", 45, "K")
        self.wysokosc = wysokosc

class Polbut(But):
    pass


class Plaszcz(OdziezWierzchnia):
    pass


bucik = But(1,"czarny", "Nike", 45, "K")
print(bucik)
