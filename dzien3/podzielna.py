# 3. czy liczba jest podzielna przez 3, 5, 7

liczba = int(input("Podaj liczbę. \n"))
# dzielniki = [3, 5, 7]
#
# for n in dzielniki:
#     if liczba % n == 0:
#         print(f"{liczba} jest podzielna przez {n}")
#     else:
#         print(f"{liczba} nie jest podzielna przez {n}")

if liczba % 3 == 0:
    print(f"Liczba {liczba} jest podzielna przez 3.")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 3.")

if liczba % 5 == 0:
    print(f"Liczba {liczba} jest podzielna przez 5.")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 5.")

if liczba % 7 == 0:
    print(f"Liczba {liczba} jest podzielna przez 7.")
else:
    print(f"Liczba {liczba} nie jest podzielna przez 7.")
