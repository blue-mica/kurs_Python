# # napisz program sumujący wszystkie elementy w liscie
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
# suma = lista_a[0]
# for counter in range(1, len(lista_a)):
#     suma += lista_a[counter]
# print(suma)
#
#
# # znajdz najwiekszy / najmniejszy element w liscie
# mini = lista_a[0]
# maxi = lista_a[0]
# for counter in range(1, len(lista_a)):
#     if lista_a[counter] > maxi:
#         maxi = lista_a[counter]
#     if lista_a[counter] < mini:
#         mini = lista_a[counter]
# print(mini)
# print(maxi)
# #gotowe funkcje
# print(min(lista_a))
# print(max(lista_a))
#
#
# # program ktory zmieni zdanie w liste wyrazow
# zdanie = "Ala ma kota, kot ma Ale"
#
# lista_z = zdanie.replace(",", "").split()
# print(lista_z)
#
# # znajdz liczbe stringow dl. min. 2, ktore zaczynaja sie i koncza na te same znaki
# # ['abc', 'xyz', 'aba', '1221'] - odp = 2
# lista_1 = ['abc', 'xyz', 'aba', '1221']
#
# for string in lista_1:
#     if len(string) >= 2 and string[0] == string[-1]:
#         print(string)
#
# # program znajdujacy wartosci, ktre wystepuja tylko raz
# lista_a = [10,20,30,20,10,50,60,40,80,50,40]
#
# for wartosc in lista_a:
#     if lista_a.count(wartosc) == 1:
#         print(wartosc)



# program usuwajacy zduplikowane wartosci w liscie (w miejscu! - tzn bez drugiej listy)
lista_b = [10,20,30,20,10,50,60,40,80,50,40]

for wart in lista_b:
    if lista_b.count(wart) == 2:
        print(wart)

print(lista_b)

# program sprawdza czy dwie listy maja co najmniej jeden wspolny element,
# jesli tak wypisuje True

