import dzien7.moj_modul.odwracacz

def czy_palindrom(wyraz):
    """
    Sprawdza czy podany ciag znakow jest palindromem
    (str) -> Bool
    """
    wyraz = wyraz.upper()
    odwrocony = dzien7.moj_modul.odwracacz.odwroc_string(wyraz)

    if wyraz == odwrocony:
        return True
    else:
        return False
print(czy_palindrom("kajak"))

    # Ten sposob jest poprawny ale NIEWLASCIWY !!! na importowanie modulow