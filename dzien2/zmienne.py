imie = "Joanna"
nazwisko = "Kowalska"
wiek = 34

print(imie + nazwisko + str(wiek) + 'lata')

print(f"{imie} {nazwisko} ma {wiek} lata.")
# przed v 3.6 ; formatowanie stringa^^^

print("{0} {1} ma {2} lata".format(imie, nazwisko, wiek))