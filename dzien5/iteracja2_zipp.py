rzeczy = ("pisak", "dlugopis", "szklanka", "portfel", "myszka")
kolory = ["czerwony", "zielony", "niebieski", "filoetowy"] # "myszka")


# x jest koloru: y

# while

indeks = 0
# dlugosc = len(rzeczy) tylko jak listy sa rownej dlugosci
dlugosc = min(len(rzeczy), len(kolory))

while indeks < dlugosc:
    print(f"{rzeczy[indeks]} jest koloru: {kolory[indeks]}")
    indeks += 1

# for + zip

for rzecz, kolor, in zip(rzeczy, kolory):
    print(f"{rzecz} jest koloru: {kolor}")

