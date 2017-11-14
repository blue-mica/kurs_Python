
nieprawidlowe = True

while nieprawidlowe:
    nazwisko = input("Podaj nazwisko drukoanymi literami lub Q aby wyjść: ")

    if nazwisko.upper() == "Q":
        quit(1)
    if nazwisko.isalpha() and nazwisko.isupper():
            nieprawidlowe = False

print("Dobrze podales")