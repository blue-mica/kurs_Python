
def show_records(base_name):
    """
    Funkcja interuje sie po liscie z parametru, a z kazdego elemntu bedacego slownikiem wyswietla jego klucz i wartosc
    :param base_name: nazwa listy slownikow
    :return: nic nie zwraca
    """
    for item in base_name:
        for key, value in item.items():
            print(f"{key:<10} : {value:<10}", end=" ")
        print(" ")


def check_existing(base_name, usr_input):
    """
    Do funkcji przekazany jest string podany przez uzytkownika, ktory dzielony jest [funkcja split] na liste (po spacji)
    Lista zawiera 3 elemety poz. [0] MARKA, [1] MODEL, [2] POJ. Porownuje te elementy do wartosci slownikow (wg. kluczy)
    Index_of_existing zwraca nam index znalezionego motocykla (wykorzystane pozniej przy usuwaniu go z bazy)
    :param base_name: nazwa listy slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :return: index_of_existing - zawraca index slownika zawierajacego szukany motocylk
    """
    index_of_existing = -1
    find_moto_param = usr_input.split()
    usr_make = find_moto_param[0]
    usr_mod = find_moto_param[1]
    usr_cap = find_moto_param[2]
    for count, elem in enumerate(base_name):
        # enumerate numeruje elementy z listy; count jest indeksem elementu z listy
        if usr_make == elem["make"] and usr_mod == elem["model"] and usr_cap == elem["capacity"]:
                index_of_existing = count
                print(f"{usr_input} jest w bazie", end=" ")
    if index_of_existing == -1:
        print(f"Podany motocykl {usr_input} nie znajduje sie w bazie.", end=" ")
    return index_of_existing


def add_moto(base_name, usr_input):
    """
    Funkcja wykorzystuje funkcje check_existing by określić czy podany ciąg MARAKA MODEL POJ. jest juz w bazie.
    Jezli nie ma, to dzieli (po spacji) usr_input i dodaje elementy do listy jako nowy slownik.
    Drukuje bazę z dodanym nowym wpisem uzywając do tego fikcji show_records.
    :param base_name: nazwa listy slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :return: Nic nie zwraca
    """
    index = check_existing(base_name, usr_input)
    if index != -1:
        print("!! NIE MOŻNA GO DODAć ;) !!")
    else:
        find_moto_param = usr_input.split()
        usr_make = find_moto_param[0]
        usr_mod = find_moto_param[1]
        usr_cap = find_moto_param[2]
        base_name.append({"make": usr_make, "model": usr_mod, "capacity": usr_cap})
        print(f"DODAJĘ >> {usr_input} << DO BAZY :) ")
        print("Aktualny stan bazy: ")
        show_records(base_name)


def del_moto(base_name, usr_input):
    """Funkcja wywołuje najpierw funkcje check_existing, zwracany przez nią index_of_existing jest przypisany do index.
    Jesli index wynosi -1 to oznacza ze w bazie nie ma takiego motocykla. W przeciwnym razie usuwa z listy slownik o
    indexie jaki zwrocila funkcja chceck_existing. Wyświetlenie bazy po kasowaniu wywołaniem funkcji show_records.
    :param base_name: nazwa listy slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :return: Nic nie zwraca
    """
    index = check_existing(base_name, usr_input)
    if index == -1:
        print(" Nie mozna go usunąć.")
    else:
        print(f"** USUWAM {usr_input} **")
        del base_name[index]
        print("Stan bazy po usunięciu.")
        show_records(base_name)


moto_base = [{"make": "BMW", "model": "F650", "capacity": "650"}, {"make": "HONDA", "model": "CBR", "capacity": "1000"},
             {"make": "SUZUKI", "model": "GS", "capacity": "500"}, {"make": "HONDA", "model": "XL", "capacity": "650"}]


user_choice = True
while user_choice:
    print("\n")
    print("****************************************")
    print("*     WITAJ W BAZIE MOTOCYKLI          *")
    print("*                                      *")
    print("****************************************")
    print("****** DOSTĘPNE POLECENIA: *************")
    print("A - dodanie motocykla")
    print("D - usunięcie motocykla")
    print("S - wyświetlenie bazy")
    print("E - sprawdzanie motocykl czy jest w bazie")
    print("K - podanie liczby rekordów")

    print("X - wyjście")
    user_input = str.upper(input("Wybierz polecenie : "))
    if user_input == "S":
        show_records(moto_base)
    elif user_input == "A":
        find_moto = str.upper(input("Podaj dane motocykla, ktory chcesz dodac: MARKA MODEL POJEMNOSC: \n"))
        add_moto(moto_base, find_moto)
    elif user_input == "K":
        print("Liczba motocykli w bazie to: %d" % len(moto_base))
    elif user_input == "E":
        find_moto = str.upper(input("Podaj dane motocykla: MARKA MODEL POJEMNOSC: \n"))
        check_existing(moto_base, find_moto)
    elif user_input == "D":
        find_moto = str.upper(input("Podaj dane motocykla do usuniecia: MARKA MODEL POJEMNOSC: \n"))
        del_moto(moto_base, find_moto)
    elif user_input == "X":
        print("-= OPUSZCASZ BAZĘ =- Do widzenia :)")
        exit(666)
else:
    user_choice = False
