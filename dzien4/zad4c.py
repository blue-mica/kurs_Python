 # INNA WERSJA
 # fizz buzz
 # wypisz liczby od 1 do 100 (włącznie)
 # liczba podzielna przez 3 = Fizz
 # liczba podzielna przez 5 = Buzz
 # liczba podzielna przez 3 i 5 = FizzBuzz

zakres = range(1,101)

for liczba in zakres:
     if liczba % 3 == 0:
         print("Fizz", end="")
     if liczba % 5 == 0:
         print("Buzz", end="")
     if liczba % 3 != 0 and liczba % 5 != 0:
         print(liczba, end="")

    print("\n", end="")

