from dzien12.silnik import Silnik

silnik1 = Silnik(1600)
silnik1.podaj_emisje(23)


silnik1.spalanie = 12

print(silnik1.spalanie)


# nie ma dostępu do pseudoprywatnego pol

# silnik1.__co2

# name mangling

# print(silnik1._Silnik__co2)

