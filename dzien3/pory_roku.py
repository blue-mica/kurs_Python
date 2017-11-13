# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku
#
# wiosna: od 9 marca do 8 czerwca
# lato: od 9 czerwca do 8 września
# jesień: od 8 września do 8 grudnia
# zima: od 9 grudnia do 9 marca

miesiac_input = str(input("Podaj miesiąc. [bez polskich znakow] \n"))
miesiac_input.strip(" ")
miesiac_input = miesiac_input.upper()

dzien_input = str(input("Podaj dzień. \n"))

if not dzien_input.isdigit():
    print("Tylko liczby")
    exit(2)

dzien_input = int(dzien_input)

if dzien_input > 31 or dzien_input < 1:
    print("Dzien spoza zakresu 1 do 31.")
    exit(1)


# dzien_input.strip(" ")

#wiosna = "MARZEC, KWIECIEN, MAJ, CZERWIEC"
if miesiac_input == "KWIECIEN" or miesiac_input == "MAJ" or miesiac_input == "MARZEC" and dzien_input >= 9 or miesiac_input == "CZERWIEC" and dzien_input <= 8:
    print('Wiosna')
    exit(111)
# if miesiac_input == "MARZEC" and dzien_input >= 9:
#     print('Wiosna')
# if miesiac_input == "CZERWIEC" and dzien_input <= 8:
#     print("Wiosna")

#lato = "CZERWIEC, LIPIEC, SIERPIEN, WRZESIEN"
if miesiac_input == "LIPIEC" or miesiac_input == "SIERPIEN" or miesiac_input == "CZERWIEC" and dzien_input >= 9 or miesiac_input == "WRZESIEN" and dzien_input <= 8:
    print("Lato")
    exit(222)

# if miesiac_input == "CZERWIEC" and dzien_input >= 9:
#     print("Lato")
# if miesiac_input == "WRZESIEN" and dzien_input <= 8:
#     print("Lato")

#jesien = "WRZEESIEN, PAZDZIERNIK, LISTOPAD, GRUDZIEN"
if miesiac_input == "PAZDZIERNIK" or miesiac_input == "LISTOPAD" or miesiac_input == "WRZESIEN" and dzien_input >= 9 or miesiac_input == "GRUDZIEN" and dzien_input <= 8:
    print("Jesien :/")
    exit(333)

# if miesiac_input == "WRZESIEN" and dzien_input >= 9:
#     print("Jesien ;/")
# if miesiac_input == "GRUDZIEN" and dzien_input <= 8:
#     print("Jesien ;/")

#zima = "GRUDZIEN, STYCZEN, LUTY, MARZEC"
if miesiac_input == "STYCZEN" or miesiac_input == "LUTY" or miesiac_input == "GRUDZIEN" and dzien_input >= 9 or miesiac_input == "MARZEC" and dzien_input < 9:
    print("Zima")
    exit(444)

# if miesiac_input == "GRUDZIEN" and dzien_input >= 9:
#     print("Zima")
# if miesiac_input == "MARZEC" and dzien_input < 9:
#     print("Zima")


