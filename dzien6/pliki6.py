#skrypt na dopisywanie nowego wpisu ZAWSZE w NOWEJ LINII
sciezka = "tekst1.txt"
tekst = "nowa linijka do dopisania"
with open(sciezka, "r+") as plik: # w "r+" plik otwiera sie w pozycji 0

    plik.read() # idziemy na koniec pliku

    pozycja = plik.tell()
    plik.seek(pozycja - 1)

    ostatni_znak = plik.read()
    print(ostatni_znak)

    if ostatni_znak != "\n":
        plik.write('\n' + tekst + '\n')
    else:
        plik.write(tekst + '\n')