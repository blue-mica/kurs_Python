def wypisz_dane(imie, nazwisko, kurs="Python", il_dni=15):
    print(f"Kursant {imie} {nazwisko}, kurs: {kurs} trwa {il_dni} dni.")

wypisz_dane("Szymon", "Kukla")
wypisz_dane("Szymon", "Kukla", "Java")
wypisz_dane("Szymon", "Kukla", "PHP", 35)

wypisz_dane("Monika", "D", il_dni=12) # przypisanie 12 do własciwego argumentu czylu il_dni (4 pozycja)

wypisz_dane(il_dni=23, imie="Jan", nazwisko="Babalina", kurs="JS") # dowolna kolejnosc podawania argumentow

