rzeczy = ("pisak", "dlugopis", "szklanka", "portfel", "myszka")

# Przedmiot: x ma indeks nr: y

# while

index = 0
dlugosc = len(rzeczy)

while index < dlugosc:
    print(f"Przedmiot: {rzeczy[index]} ma indeks nr: {index}")
    index += 1

# for

index2 = 0
for rzecz in rzeczy:
    print(f"Przedmiot: {rzecz} ma indeks nr: {index2}")
    index2 += 1

# for + enumerate

for index3, przedmiot in enumerate(rzeczy):
    print(f"Przedmiot: {przedmiot} ma indeks nr: {index3}")

#
