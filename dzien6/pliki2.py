sciezka = "tekst1.txt"

with open(sciezka) as plik:
    linijka = plik.readline()
    pozycja = plik.tell()
    print(f"Kursor znajduje sie w ozycji nr {pozycja}")
    plik.seek(3)
    print(plik.read())

    # print(plik.readline()) #czyta 1 linie - odczytuje linie po kolei przy kazdym wywolaniu
    #                     # i tam czeka na kolejne polecenie
    # print("Kolejna linijka")
    # print(plik.readline()) # czyta 2 linie, samo read tez tak odczyta
    #                         # tylko pojdzie do konca tekstu