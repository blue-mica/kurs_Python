elementy = {0: "ala", 1: "ola", 2: "ela"}
#
# print(elementy)
# print(elementy[1])

slownik = {"imie": "Adam", "nazwisko": "kowalski", "wiek": 32}
# print(slownik.keys())
# print(slownik.values())
# print(slownik.items())
#
# for klucz, wartosc in slownik.items():
#     print(f"Klucz: {klucz} ma wartość {wartosc}")
#
# if "adres" in slownik.keys():
#     print("Adres dostepny")
# else:
#     print("adres niedostepny")
print(slownik)
slownik["adres"] = "Gdansk"
print(slownik)
slownik["adres"] = "Gdynia" #nadpisze nam wrtość "gdansk" w slowniku
print(slownik)
