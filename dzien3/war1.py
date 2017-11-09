# if True:
#     pass

# if 5 == 10/2:
#     print("Wnętrze ifa")

if 5 != 20 / 4: #False
    print("Drugi if")
elif 5 == 5 and 20 % 2 == 1: #False
    print("Drugi if, elif")
elif 45 % 3 == 12:  #F
    print("elif modulo")
else:
    print("Instrukcja domyslna")

if 5 != 20 / 4: #F
    print("Drugi if")
# elif 5 == 5 and 20 % 2 == 1: #False
#     print("Drugi if, elif")
# elif 45 % 3 == 12:  #F
#     print("elif modulo")
else:
    print("Instrukcja czy moze byc else") # else moze byc zawsze niezależnie czy sa elif-y

# print("Pierwsza instrukcja po if")