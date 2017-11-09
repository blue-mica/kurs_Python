# oblicz czy rok jest przestępny

# podzielny przez 4, nie podzielny 100 ale podzielny przez 400

# rok = input("Podaj rok: \n")
# rok = int(rok)

rok = int(input("Podaj rok. \n"))

# if not rok.isdigit():
#         print("Musza być tylko cyfy")
#         exit()

if rok % 400 == 0:
    print(f"Rok {rok} jest przestępny.")

elif rok % 4 == 0 and rok % 100 != 0:
    print(f"Rok {rok} jest przestępny.")

else:
    print(f"Rok {rok} NIE jest przestępny.")

