# napisz program wydajacy reszte z zakupow
# zakupy - wartosc, place banknotem
# wydac monetami o nominalach 5 - 0.1
# wydac jak najmniej monet

monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

wartosc_zakupow = 11.30
banknot = 20

reszta = banknot - wartosc_zakupow

print("Wydaj:", reszta)
if reszta < 0:
    print("Za mala wartosc banknotu")
    quit()
elif reszta == 0:
    print("Bez reszty")
    quit()

for moneta in monety.keys():
    if reszta >= moneta:
        ilosc = reszta // moneta
        monety[moneta] = ilosc
        reszta = round(reszta - (moneta * ilosc), 2)
        print("Tyle reszty jeszce jest:", reszta)

print("Wydac:")
for moneta, ilosc in monety.items(): # dodajemy do slownika wartosci
    print(f"moneta: {moneta:>4} - {ilosc:>4} sztuk.")