# sprawdz czy jest wygrana w kolko i krzyzyk
# input: string 9 znaków x, o, n
# znaki oznaczja pozycje wierszami od gornego

slowo = str(input("Podaj ciąg 9-ciu znakow X, O lub N \n"))
# slowo = "OOXONOXXO"

while len(slowo) != 9:
    print("Podany ciąg nie ma 9 znaków\n")
    slowo = str(input("Podaj ciąg 9-ciu znakow X, O lub N \n"))

slowo = slowo.upper()

wygrana_X = "XXX"
wygrana_O = "OOO"

# print(slowo.count('X'))
# print(slowo.find('X'))

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