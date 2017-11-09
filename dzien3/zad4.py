# po podaniu nazwy m-ca podaj ilosc dni

miesiac = input("Podaj nazwe miesiaca: ")

if miesiac == "kwiecien" or miesiac == "czerwiec" or miesiac == "wrzesień" \
    or miesiac == "listopad":
    print(f"Miesiąc {miesiac} ma 30 dni")

elif miesiac == "luty":
    print(f"Miesiac {miesiac} ma 28 lub 29 dni")

else:
    print(f"Miesciac {miesiac} ma 31 dni")