osoby = {}

rekordy = [{"imie": "Adam", "nazwisko": "kowalski", "wiek": 32},
{"imie": "Anna", "nazwisko": "nowak", "wiek": 23},
{"imie": "jan", "nazwisko": "twardowski", "wiek": 65},
{"imie": "zenek", "nazwisko": "babalina", "wiek": 70}]

for indeks, rekord in enumerate(rekordy):
    osoby[indeks] = rekord

print(osoby)