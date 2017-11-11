# 1. sprawdź czy jest wygrana w kółko i krzyżyk
#   input: string 9 znaków x, o, n
#   znaki oznaczają pozycje wierszami od gornego
slowo = str(input("Podaj ciąg 9-ciu znakow X, O lub N \n"))
# slowo = "OOXONOXXO"

while len(slowo) != 9:
    print("Podany ciąg nie ma 9 znaków\n")
    slowo = str(input("Podaj ciąg 9-ciu znakow X, O lub N \n"))

slowo = slowo.upper()

wygrana_X = "XXX"
wygrana_O = "OOO"

if (wygrana_O in slowo[0:3]) or (wygrana_O in slowo[3:6]) or (wygrana_O in slowo[6:9]):
    print("Wygrało O ! :)")

elif (wygrana_X in slowo[0:3]) or (wygrana_X in slowo[3:6]) or (wygrana_X in slowo[6:9]):
    print("Wygrał X ! :)")

elif slowo[0] != "N" and (slowo[0] == slowo[3] and slowo[0] == slowo[6]):
    print("Wygrana " + slowo[0] + " ! :)")

elif slowo[1] != "N" and (slowo[1] == slowo[4] and slowo[1] == slowo[7]):
    print("Wygrana " + slowo[1] + " ! :)")

elif slowo[2] != "N" and (slowo[2] == slowo[5] and slowo[2] == slowo[8]):
    print("Wygrana " + slowo[2] + " ! :)")

elif slowo[0] != "N" and (slowo[0] == slowo[4] and slowo[0] == slowo[8]):
    print("Wygrana " + slowo[0] + " ! :)")

elif slowo[2] != "N" and (slowo[2] == slowo[4] and slowo[2] == slowo[6]):
    print("Wygrana " + slowo[2] + " ! :)")

else:
    print("Nikt nie wygrał. Czyli remis.")

# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

# 3. czy liczba jest podzielna przez 3, 5, 7

# 4. oblicz ocenę na podstawie progu procentowego

# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

# 6. blackjack - na inpucie wejście 2 karty
#   wartości: 2-9, J Q K = 10, A = 1 lub 11
#   określ ruch jaki powinien być wykonany:
#   jeszcze jedna karta, stop,

# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku


# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32
