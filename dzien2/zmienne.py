imie = "Joanna"
nazwisko = "Kowalska"
pseudo = "Myszka"
wiek = 34
wzrost = 188
waga = 75

print(imie + nazwisko + str(wiek) + 'lata')

# przed v 3.6 ; formatowanie stringa
print(f"{imie} {nazwisko} ma {wiek} lata.")

print("{0} {1} ma {2} lata. Wzrost {3} cm. Waga: {4} ".format(pseudo, imie, wiek, wzrost, waga))
