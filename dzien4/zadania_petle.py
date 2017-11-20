# program wydający resztę z dostępnych monet: 5, 2, 1, 0.5, 0.2, 0.1

# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
#
#   #
#  ###
# #####
#

# program, ktory obliczy ilosc liczb parzystych i nieparzystych w danym zakresie
even = 0
odd = 0
for number in range(0, 21):
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Parzystych: {even} Nie parzystych: {odd}")


# program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4

# for liczba in range(0, 21):
#     if liczba % 4 != 0:
#         print(liczba)



# program, ktory wypisze liczby (0 do 100) z ciagu Fibonacciego
# 0, 1, 1, 2, 3, 5, 8, 13, 21
a, b = 1, 2
print(a, b)
# program wypisujący tabliczkę mnozenia (1 do 10) dla podanej liczby
# uzyc formatowania stringow!

for number_1 in range(1, 11):
    for number_2 in range(1, 11):
        multiply = number_1 * number_2
        print(f"{number_1}*{number_2}={multiply}")

# if elif else
# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata

