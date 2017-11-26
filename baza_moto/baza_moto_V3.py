import pickle


def verify_user_input(user_input):
    """
    Funkcja sprawdza czy wprowadzony przez uzytkownika string spelnia warunki formatu bazy.
    :param user_input: string wprowadzony przez uzytkownika
    :return: flaga informujaca o spelnieniu warunku lub nie (Truem lub False)
    """
    verify = True
    user_parameters = user_input.split()
    if len(user_parameters) != 3:
        return False
    if user_parameters[0].isdigit() or not user_parameters[0].isalpha():
        return False
    if not user_parameters[1].isalnum():
        return False
    if not user_parameters[2].isdigit() or len(user_parameters[2]) <= 1 or len(user_parameters[2])> 4:
        return False
    else:
        return verify


def file_to_list(file_name):
    """
    Funkcja otwiera plik bazy danych i zapisuje jej zawartosc do nowej listy.
    :param file_name: nazwa pliku bazy
    :return: tworzy listę z odczytanego pliku
    """
    with open(file_name, 'rb') as file:
        list_from_file = pickle.load(file, encoding="UTF-8")
    return list_from_file


def show_records(list_from_file):
    """
    Funkcja interuje sie po liscie z parametru, a z kazdego elemntu bedacego slownikiem wyswietla jego klucz i wartosc
    :param list_from_file: lista slownikow
    :return: nic nie zwraca
    """
    for item in list_from_file:
        for key, value in item.items():
            print(f"{key:<10} : {value:<10}", end=" ")
        print(" ")


def check_existing(list_from_file, usr_input):
    """
    Do funkcji przekazany jest string podany przez uzytkownika, ktory dzielony jest [funkcja split] na liste (po spacji)
    Lista zawiera 3 elemety poz. [0] MARKA, [1] MODEL, [2] POJ. Porownuje te elementy do wartosci slownikow (wg. kluczy)
    Index_of_existing zwraca nam index znalezionego motocykla (wykorzystane pozniej przy usuwaniu go z bazy)
    :param list_from_file: lista slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :return: index_of_existing - zawraca index slownika zawierajacego szukany motocylk
    """

    index_of_existing = -1
    find_moto_param = usr_input.split()
    usr_make = find_moto_param[0]
    usr_mod = find_moto_param[1]
    usr_cap = find_moto_param[2]
    for count, elem in enumerate(list_from_file):
        # enumerate numeruje elementy z listy; count jest indeksem elementu z listy
        if usr_make == elem["make"] and usr_mod == elem["model"] and usr_cap == elem["capacity"]:
                index_of_existing = count
                print(f"{usr_input} jest w bazie", end=" ")
    if index_of_existing == -1:
        print(f"Podany motocykl {usr_input} nie znajduje sie w bazie.", end=" ")
    return index_of_existing


def add_moto(list_from_file, usr_input, file_name):
    """
    Funkcja wykorzystuje funkcje check_existing by określić czy podany ciąg MARAKA MODEL POJ. jest juz w bazie.
    Jezli nie ma, to dzieli (po spacji) usr_input i dodaje elementy do listy jako nowy slownik.
    Zapisuje do pliku (nadpisujac go). Drukuje bazę z dodanym nowym wpisem uzywając do tego fikcji show_records.
    :param list_from_file: list slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :param file_name: nazwa pliku bazy
    :return: Nic nie zwraca
    """
    index = check_existing(list_from_file, usr_input)
    if index != -1:
        print("!! NIE MOŻNA GO DODAć ;) !!")
    else:
        find_moto_param = usr_input.split()
        usr_make = find_moto_param[0]
        usr_mod = find_moto_param[1]
        usr_cap = find_moto_param[2]
        list_from_file.append({"make": usr_make, "model": usr_mod, "capacity": usr_cap})
        print(f"DODAJĘ >> {usr_input} << DO BAZY :) ")
        with open(file_name, 'wb') as file:
            pickle.dump(list_from_file, file)
        print("Aktualny stan bazy: ")
        show_records(list_from_file)


def record_count(new_list):
    """
    Funkcja zlicza i wyświetla ilość elementow bazy na podstawie ilości slowników na liscie.
    :param new_list: plik bazy
    :return: Nic
    """
    print("Liczba motocykli w bazie to: %d" % len(new_list))


def del_moto(list_from_file, usr_input, file_name):
    """Funkcja wywołuje najpierw funkcje check_existing, zwracany przez nią index_of_existing jest przypisany do index.
    Jesli index wynosi -1 to oznacza ze w bazie nie ma takiego motocykla. W przeciwnym razie usuwa z listy slownik o
    indexie jaki zwrocila funkcja chceck_existing. Zapsuje baze do pliku z wykozystaniem "pickle".
    Wyświetlenie bazy po kasowaniu wywołaniem funkcji show_records.
    :param list_from_file: nazwa listy slownikow
    :param usr_input: motocykl podany przez uzytkownika
    :param file_name: nazwa pliku bazy
    :return: Nic
    """
    index = check_existing(list_from_file, usr_input)
    if index == -1:
        print(" Nie mozna go usunąć.")
    else:
        print(f"** USUWAM {usr_input} **")
        del list_from_file[index]
        print("Stan bazy po usunięciu.")

    with open(file_name, 'wb') as file:
        pickle.dump(list_from_file, file)
    show_records(list_from_file)


user_choice = True
possible_choice = ["A", "D", "S", "E", "K", "X"]
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
    # sprawdzenie czy user wybral tylko dozwolone litery odpowiadajace poleceniom
    if  user_input not in possible_choice:
        print("WYBIERZ DOSTEPNE POLECENIE")
    elif user_input == "S":
        new_list = file_to_list("moto_base.pickle")
        show_records(new_list)
    elif user_input == "A":
        find_moto = str.upper(input("Podaj dane motocykla, ktory chcesz dodac: MARKA MODEL POJEMNOSC: \n"))
        # linia 145 to to samo co - verify_user_input(find_moto) == False:
        if not verify_user_input(find_moto):
            print("Podaj poprawne dane.")
        else:
            new_list = file_to_list("moto_base.pickle")
            file_name = "moto_base.pickle"
            add_moto(new_list, find_moto, file_name)
    elif user_input == "K":
        new_list = file_to_list("moto_base.pickle")
        record_count(new_list)
    elif user_input == "E":
        find_moto = str.upper(input("Podaj dane motocykla: MARKA MODEL POJEMNOSC: \n"))
        # linia 157 to to samo co - verify_user_input(find_moto) == False:
        if not verify_user_input(find_moto):
            print("Podaj poprawne dane.")
        else:
            new_list = file_to_list("moto_base.pickle")
            check_existing(new_list, find_moto)
    elif user_input == "D":
        find_moto = str.upper(input("Podaj dane motocykla do usuniecia: MARKA MODEL POJEMNOSC: \n"))
        # linia 165 to to samo co - verify_user_input(find_moto) == False:
        if not verify_user_input(find_moto):
            print("Podaj poprawne dane.")
        else:
            new_list = file_to_list("moto_base.pickle")
            file_name = "moto_base.pickle"
            del_moto(new_list, find_moto, file_name)
    elif user_input == "X":
        print("-= OPUSZCZASZ BAZĘ =- Do widzenia :)")
        exit(666)
else:
    user_choice = False
