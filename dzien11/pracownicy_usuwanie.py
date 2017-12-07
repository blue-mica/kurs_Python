from dzien11.pola_klasy import Pracownik

prac1 = Pracownik("John", "Travolta", 5000)
print(prac1)

prac2 = Pracownik("Tom", "Cruse", 235000)
print(prac2)

prac3 = Pracownik("Cezary", "Pazura", 50)
print(prac3)

print(prac1.roczna_podw)
print(prac2.roczna_podw)
print(prac3.roczna_podw)

prac1.zmien_roczna_podwyzka(13)
Pracownik.zmien_roczna_podwyzka(23)

print(prac1.roczna_podw)
print(prac2.roczna_podw)
print(prac3.roczna_podw)


# print(prac1.ilosc_instancji)
# print(prac2.ilosc_instancji)
# print(prac3.ilosc_instancji)
#
# del prac2
#
# print(Pracownik.ilosc_instancji)