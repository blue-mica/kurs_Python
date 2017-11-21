import pickle


baza = [{"imie": "Adam", "nazwisko": "kowalski", "wiek": 32},
{"imie": "Anna", "nazwisko": "nowak", "wiek": 23},
{"imie": "jan", "nazwisko": "twardowski", "wiek": 65},
{"imie": "zenek", "nazwisko": "babalina", "wiek": 70}]

# zapisujemy do pliku

with open("baza.pickle", 'wb') as plik:
    pickle.dump(baza, plik)

# otwarcie pliku

odczytana_baza = None

with open("baza.pickle", 'rb') as plik:
    odczytana_baza = pickle.load(plik, encoding="UTF-8")

print(odczytana_baza)
