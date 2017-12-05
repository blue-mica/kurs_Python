class Czekolada(object):
    def __init__(self, masa, cena, producent):
        self.masa = masa
        self.cena = cena
        self.producent = producent

    def zjedz(self, ilosc_g):
        if ilosc_g >= self.masa:
            self.masa = self.masa - ilosc_g
        else:
            print(f"Czekolada już jest zjedzona.")

    def __add__(self, other):
        return self.masa + other.masa

    def __lt__(self, other):
        return self.masa < other.masa

    def __str__(self):
        return f"Czekolada  o masie {self.masa} za {self.cena} od {self.producent} zostala zjedzona."
