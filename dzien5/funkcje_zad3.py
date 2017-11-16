def dodaj_imie(imie, baza=[]):
    imie = imie.upper()
    baza.append(imie)
    return baza

# imiona = ["ANNA", "DAMIAN"]
# imiona = dodaj_imie("andrzej")
# imoina = dodaj_imie("wacek")
#
# print(imiona)

anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antuan")
print(francuzi)
rosjanie = dodaj_imie("masza")
print(rosjanie)


