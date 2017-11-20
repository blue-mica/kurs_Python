
def show_records(mk, mod, cap):
    """Funkcja wymaga podania jako paramtry trzech list. Wyświetla elementy tych list o tym samym indeksie """
    for makes, models, capacitys, in zip(mk, mod, cap):
        print(f"MARKA: {makes} | MODEL: {models}  | POJ.: {capacitys} cm3")


def check_existing(mk, mod, cap):
    """Funkcja wymaga podania jako parametry trzech list. Pobiera od uzytkownika string ktory dzieli [funkcja split] na
    liste (po spacji). Lista zawiera 3 elemety poz. [0] MARKA, [1] MODEL, [2] POJ.  Porownuje te elementy do elementow
      z list podanych w parametrze. Zmienna is_in_base w przypadku nie znalezienia motocykla pozostaje nie zmieniona.
      Index_of_existing zwraca nam index znalezionego motocykla (wykorzystane poxniej przy usuwaniu go z bazy)."""

    index_of_existing = -1
    find_moto = str.upper(input("Podaj dane motocykla: MARKA MODEL POJEMNOSC: \n"))
        # find_moto_param - lista 3 elementowa: MARKA, MODEL, POJ.
    find_moto_param = find_moto.split()
    usr_make = find_moto_param[0]
    usr_mod = find_moto_param[1]
    usr_cap = find_moto_param[2]
    for count, elem in enumerate(mk):
        # enumerate numeruje elementy z listy; count jest indeksem elementu z listy
        if usr_make == elem:
            if usr_mod == mod[count] and usr_cap == cap[count]:
                index_of_existing = count
                print(f"Motocykl {elem} {mod[count]} {cap[count]} jest w bazie. ", end=" ")
    if index_of_existing == -1:
        print(f"Podany motocykl nie znajduje sie w bazie.", end=" ")
    return index_of_existing, find_moto


def add_moto(mk, mod, cap):
    """Funkcja wukozystuje funkcje check_existing by określić czy podany ciąg MARAKA MODEL POJ. jest kuz w bazie.
    Jezli nie ma, to rozpakowuje Tuple (moto) pobrane z check_existing i dodaje elementy do list.
    Drukuje bazę z dodanym nowym wpisem uzywając do tego fikcji show_records."""

    index, moto = check_existing(mk, mod, cap)
    if index != -1:
        print("!! NIE MOŻNA GO DODAć ;) !!")
    else:
        find_moto_param = moto.split()
        usr_make = find_moto_param[0]
        usr_mod = find_moto_param[1]
        usr_cap = find_moto_param[2]
        mk.append(usr_make)
        mod.append(usr_mod)
        cap.append(usr_cap)
        print(f"DODAJĘ >> {moto} << DO BAZY :) ")
        print("Aktualny stan bazy: ")
        show_records(mk, mod, cap)


def del_moto(mk, mod, cap):
    """Funkcja wywołuje najpier funkcje is_existing, zwracany przez nią Tuple przypisany jest do zmiennych indicator
    (True / False),i inxex (indeks znalezionego motocykla) oraz moto (string podany przez użytkownika).
    Kasowanie elementów z wszystkich list przez odwolanie się do index. Wyświetlenie bazy po kasowaniu wywołaniem
    funkcji show_records."""
    index, moto = check_existing(mk, mod, cap)
    if index == -1:
        print(" Nie mozna go usunąć.")
    else:
        print(f"** USUWAM {moto} **")
        del mk[index]
        del mod[index]
        del cap[index]
        print("Stan bazy po usunięciu.")
        show_records(mk, mod, cap)


make = ['BMW', 'HONDA', 'SUZUKI', "HONDA"]
model = ['F650', 'CBR', 'GS', "XL"]
capacity = ['650', '1000', '500', '650']


print("****************************************")
print("*     WITAJ W BAZIE MOTOCYKLI          *")
print("*                                      *")
print("****************************************")
print("Wybierz, co chesz zrobić:")
print("A - dodanie motocykla")
print("D - usunięcie motocykla")
print("S - wyświetlenie bazy")
print("E - sprawdzanie motocykl czy jest w bazie")
print("K - podanie liczby rekordów")

print("X - wyjście")

user_input = str.upper(input("Wybieram: "))


if user_input == "S":
    show_records(make, model, capacity)
elif user_input == "A":
    add_moto(make, model, capacity)
elif user_input == "K":
    print("Liczba motocykli w bazie: %d" % len(make))
elif user_input == "E":
    check_existing(make, model, capacity)
elif user_input == "D":
    del_moto(make, model, capacity)
elif user_input == "X":
    print("Do widzenia :)")
    exit(1)


