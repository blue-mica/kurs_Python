# policz samogloski i spolgloski
zdanie = input("Podaj jakies zdanie: ")

samogloski = 0
spolgloski = 0

lsta_samogl = "aeiouy"

for litera in zdanie:
    if litera.isalpha():
        if litera in lsta_samogl:
            samogloski += 1
        else:
            spolgloski += 1

print(f"Samoglosek: {samogloski}, spolglosek {spolgloski}")