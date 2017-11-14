# podaj liste unikalnych wartosci

lista_a = [10, 20, 30, 333, 10, 234, 10, 435, 35, 7654,]

unikalne = []

for element in lista_a:
    if element not in unikalne:
        unikalne.append(element)

posortowane = sorted(unikalne)
print(unikalne)
print(posortowane)


# unikalne = sorted(unikalne)
# print(sorted(unikalne))