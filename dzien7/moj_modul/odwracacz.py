def odwroc_string(zdanie):
    """
    Zwraca odwrocony string. Jesli argument jest pustym stringiem lub None - zwraca None
    :param zdanie: Zdanie do odwrocenia
    :return: Odwrocone zdanie lub None
    """
    if zdanie == "" or zdanie == None:
        return None
    else:
        return zdanie[::-1]

def main():
    imie = "ala"
    odwr_imie = odwroc_string(imie)
    spr_imie = imie[::-1]

    if odwr_imie == spr_imie:
        print(f"Imie {imie} zostalo prawodlowo odwrocone na {odwr_imie}")
    else:
        print(f"Nieprawidłowo {imie} != {odwr_imie}")

if __name__ == '__main__':
    main()