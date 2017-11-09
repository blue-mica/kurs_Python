# nazwisko = "Kowalska"

nazwisko = input("Podaj nazwisko:\n")
# usunąć whitespace'y z początku i końca
nazwisko = nazwisko.strip() #tak lub:
# nazwisko = nazwisko.strip() #tak

# jeśli w stringu są cyfry, napisać komunikat
#sprawdzamy na poczatku linie: 5
if not nazwisko.isalpha():
        print("Musza być tylko litery")
        exit(99) #w nawiasie podajemy wymyslony numer  (kod) błędu


# zamienić wszystkie litery na duże
naz_czyste = nazwisko.upper()


#i przerwać program

print(naz_czyste)


if naz_czyste[-1] == "A":
    print("Chyba jesteś kobietą.")

elif naz_czyste.endswith("SKI"):
    print("Jesteś facetem")

# elif nazwisko.isupper():
#     print("Chyba jestes zlosliwa ;)")

print(">>KONIEC PROGRAMU<<")