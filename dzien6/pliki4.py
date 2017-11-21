sciezka = "tekst1.txt"

with open(sciezka, 'a') as plik: #w trybie 'a' kursor w otwartym pliku po otwarciu jest na koncu ostaniej linii
    print(plik.tell())

    plik.write("Moja kolejna linijka \n")