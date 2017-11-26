import pickle


def show_all(base_name):
    odczytana_baza = None
    with open(base_name, 'rb') as plik:
        odczytana_baza = pickle.load(plik, encoding="UTF-8")
    for el in odczytana_baza:
        print(el)
        print(" ")


    # for elem in base_name:
    #     for key in elem.keys():
    #         print(key,":", elem[key], " ", end= " ")
    #     print(" ")


#marka_set = set()

#for elem in samochody:
 #   for key in elem.keys():
 #       print(elem[key], end=" ")
  #  print(" ")

#    if elem["marka"] == "Opel":
 #       print(elem["model"])

def if_existing(base_name, searched):
    index_of_existing = -1
    find_moto_param = searched.split()
    usr_make = find_moto_param[0]
    usr_mod = find_moto_param[1]
    usr_cap = find_moto_param[2]
    for ind, elem in enumerate(base_name):
        if usr_make == elem["marka"] and usr_mod == elem["model"] and usr_cap == elem["rok"]:
                index_of_existing = ind
                print(f"Podany sanmochód, {find_moto_param} jest w bazie. ", )
    if index_of_existing == -1:
        print(f"Podany samochód nie znajduje sie w bazie.", end=" ")
    return index_of_existing

def add_car(base_name, added_car):
    index = if_existing(base_name, added_car)
    if index != -1:
        print("!! NIE MOŻNA GO DODAć ;) !!")
    else:
        find_moto_param = added_car.split()
        usr_make = find_moto_param[0]
        usr_mod = find_moto_param[1]
        usr_cap = find_moto_param[2]
        base_name.append({"marka": usr_make, "model": usr_mod, "rok": usr_cap})
        print(f"DODAJĘ >> {added_car} << DO BAZY :) ")
        print("Aktualny stan bazy: ")
        show_all(base_name)

def del_car(base_name, car_name):
        index = if_existing(base_name, car_name)
        if index == -1:
            print(" Nie mozna go usunąć.")
        else:
            print(f"** USUWAM {car_name} **")
            del base_name[index]
            print("Stan bazy po usunięciu.")
            show_all(base_name)
#marka_set.add(elem["marka"])
#print(marka_set)

# print(slownik.items())
#
# for klucz, wartosc in slownik.items():
#     print(f"Klucz: {klucz} ma wartość {wartosc}")

print("****************************************")
print("*     WITAJ W BAZIE SAMOCHODOW         *")
print("*                                      *")
print("****************************************")
print("Wybierz, co chesz zrobić:")
print("A - dodanie samochodu")
print("D - usunięcie samochodu")
print("S - wyświetlenie bazy")
print("E - sprawdzanie czy samochod jest w bazie")
print("K - podanie liczby rekordów")
print("X - wyjście")
user_input = str.upper(input("Wybieram: "))

if user_input == "S":
    show_all("auta.moni")
elif user_input == "A":
    users_car = str.upper(input("Podaj dane samochodu: MARKA MODEL ROK: \n"))
    add_car(samochody, users_car)
elif user_input == "K":
    print("Liczba samochodów w bazie: %d" % len(samochody))
elif user_input == "E":
    searched_car = str.upper(input("Podaj dane samochodu: MARKA MODEL ROK: \n"))
    if_existing(samochody, searched_car)
elif user_input == "D":
    deleted_car = str.upper(input("Podaj dane samochodu: MARKA MODEL ROK: \n"))
    del_car(samochody, deleted_car)
elif user_input == "X":
    print("-= OPUSZCASZ BAZĘ =- Do widzenia :)")
    exit(666)