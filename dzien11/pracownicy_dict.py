from dzien11.pola_klasy import Pracownik

prac1 = Pracownik("John", "Travolta", 5000)
print(prac1)

prac2 = Pracownik("Tom", "Cruse", 235000)
print(prac2)

prac1.roczna_podw = 15

print("Dict prac1:")
print(prac1.__dict__)

print("\n Dict prac2")
print(prac2.__dict__)

print("\n Dict klasa")
print(Pracownik.__dict__)
