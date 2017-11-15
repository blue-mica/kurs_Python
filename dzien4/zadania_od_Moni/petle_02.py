    #
    # wypisz liczby od 1 do 100
# zakres = range(1, 101)
#
# for liczba in zakres:
#     print(liczba)
#
# liczba_1 = 1
# while liczba_1 <= 100:
#     print(liczba_1)
#     liczba_1 += 1

    # wypisz liczby od 8 do 50
# zakres_1 = range(8, 50)
#
# for liczba in zakres_1:
#     print(liczba, end=" ")
#
# liczba_od  = 8
# print("\n")
# while liczba_od <= 50:
#     print(liczba_od)
#     liczba_od += 1


    # wypisz liczby parzyste od 2 to 50

# zakres = range(2, 49, 2)
# zakres_2 = [50]
# for liczba in zakres:
#     print(liczba, end="_")
# for liczba in zakres_2:
#     print(liczba)

    # wypisz liczby od 100 do 1

# start = 100
# while start >= 1:
#     print(start)
#     start -= 1

    # wypisz liczby podzielne przez 8 ( w zakresie 1..100)

# zakres = range(1, 101)
# for liczba in zakres:
#     if liczba % 8 == 0:
#         print(liczba, end=" ")

    # wypisz liczby podzielne przez 3 lub 5 ( w zakresie 1..100)

# zakres = range(1, 101)
#
# for liczba in zakres:
#      if liczba % 3 == 0 or liczba % 5 == 0:
#         print(liczba, end=" ")

    # wypisz liczby podzielne przez 3 albo 5 ( w zakresie 1..100) (nie wypisuj tych podzielnych jednocześnie przez 3 i 5)

# zakres = range(1,101)
#
# for liczba in zakres:
#     if liczba % 3 == 0 and liczba % 5 == 0:
#         continue
#     elif liczba % 3 == 0 or liczba % 5 == 0:
#         print(liczba, end=" ")

    # wypisz największą liczbę niepodzielną przez 2,3,5,7 ale mniejszą od 1000

zakres = range(1, 1001)
naj = 0
for liczba in zakres:
    if liczba % 2 != 0 and liczba % 3 != 0 and liczba % 5 != 0 and liczba % 7 != 0:
        if liczba > naj:
            naj = liczba

print(naj, end=" ")





    # sprawdź czy podana jako parametr liczba jest parzysta
    # sprawdź czy podana jako parametr liczba jest liczbą pierwszą. (podzielna tylko przez 1 i przez samą siebie) (opis tutaj
    # wylicz największy wspólny dzielnik 2 liczb podanych jako parametry (opis tutaj)
    # wylicz najmniejszą wspólną wielokrotność liczb podanych jako parametry (opis tutaj)
    # ile jest liczb pierwszych w zakresie od a do b podanym jako parametry
    # sprawdź czy 2 liczby podane jako parametr są liczbami względnie pierwszymi. (opis tutaj)
    # sprawdź czy pesel ( jako parametr) jest prawidłowym peselem (tutaj opis)
    # oblicz silnię n (n – podane jako parametr) (tutaj opis)
    # oblicz n-tą liczbę ciągu fibonacciego (n – podane jako parametr) (tutaj opis)
    # oblicz n-tą liczbę pierwszą (n – podane jako parametr)

