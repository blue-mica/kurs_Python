# wypisz czy liczby w zakresie

liczby = [2,43,343,43,1,3535,664,43,578,5,87]

# x - tak
# y - nie

def czy_w_zakresie(liczba, zakres=range(100)):
    """
    Sprawdza czy podana liczba jest w zakresie
    :param liczba: liczba do sprawdzenia
    :param zakres: range
    :return: Non
    """
    if liczba in zakres:
        print(f"{liczba} - YES")
    else:
        print(f"{liczba} - NO")

for x in liczby:
    czy_w_zakresie(x)