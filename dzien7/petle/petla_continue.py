# wypisz liczby od 1 do 100 bez podzielnych przez 7

for x in range(100):
    if x % 7 == 0:
        continue
    else:
        print(x)

        