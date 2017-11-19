def dodaj_imie(imie, baza=None):
    """Dodaje imie do bazy jesli baza nie istnieje, tworzy nowa baze
    (str, [list]) -> list"""

    if baza == None:     #doadawanie nowej bazy jezeli podamy tylko pierwszy (jeden) argument
        baza = []

    imie = imie.upper()
    baza.append(imie)
    return baza

anglicy = dodaj_imie("john")
print(anglicy)
francuzi = dodaj_imie("antuan")
print(francuzi)
rosjanie = dodaj_imie("masza")
print(rosjanie)
dodaj_imie("dick", anglicy)
print(anglicy)

