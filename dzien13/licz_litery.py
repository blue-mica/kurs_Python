import sys

print(sys.argv)

if len(sys.argv) != 3:
    print("Bledna liczba argumentow")
    exit()

zdanie = sys.argv[1]
litera = sys.argv[2]

assert isinstance(zdanie, str)
# sprawdzi czy zdanie jest typem str i zwraca boola (True lub False)

print(zdanie.count(litera))

