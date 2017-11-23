# napisz program sumujący wszystkie elementy w liscie

# znajdz najwiekszy / najmniejszy element w liscie

# program ktory zmieni zdanie w liste wyrazow
zdanie = "Ala ma kota, kot ma Ale"

# znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki- odp = 2
znaki = ['abc', 'xyz', 'aba', '1221']
liczba_element = 0
for element in znaki:
    # print(element)
    # print(len(element))
    if len(element) >= 2:
        if element[0] == element[-1]:
            liczba_element += 1
print(liczba_element)




# program znajdujacy wartosci, ktre wystepuja tylko raz
lista_a = [10,20,30,20,10,50,60,40,80,50,40]


# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

