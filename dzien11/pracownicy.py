from dzien11.pola_klasy import Pracownik

prac1 = Pracownik("John", "Travolta", 5000)
print(prac1)

prac2 = Pracownik("Tom", "Cruse", 235000)
print(prac2)

prac3 = Pracownik("Cezary", "Pazura", 50)
print(prac3)

# print(prac1.ilosc_instancji)
print(prac1.roczna_podw)
print(prac2.roczna_podw)
print(prac3.roczna_podw)

prac1.roczna_podw = 15
print(f"prac1 dostaje {prac1.roczna_podw}")
print(prac2.roczna_podw)
print(prac3.roczna_podw)

Pracownik.roczna_podw = 25
print("Daje wszystkim")
print(f"Dostaje {prac1.roczna_podw}")
print(prac2.roczna_podw)
print(prac3.roczna_podw)

del prac1.roczna_podw
print("Usuwam podw dla pracownika nr 1")
print(prac1.roczna_podw)
print(prac2.roczna_podw)
print(prac3.roczna_podw)
