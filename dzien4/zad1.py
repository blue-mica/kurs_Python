# obliczyc ilosc liczb przystych i nieparzystych w zakresie

zakres = range(23746)

parzyste = 0
nparzyste = 0

for liczba in zakres:
    if liczba % 2 == 0:
        parzyste += 1  # parzyste=parzyste+1
    else:
        nparzyste += 1

print(f"Liczb parzystch {parzyste}, liczb nieparzystych: {nparzyste}")