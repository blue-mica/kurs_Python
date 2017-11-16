imie = "Ola"

def wypisz_imie():
    global imie # odwołanie do zmiennej globalnej (spoza funkcji); nalezy tego raczej unikac!!!
    duze_imie = imie.upper()
    return duze_imie

print(wypisz_imie())