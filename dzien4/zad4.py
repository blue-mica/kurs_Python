 # fizz buzz
 # wypisz liczby od 1 do 100 (włącznie)
 # liczba podzielna przez 3 = Fizz
 # liczba podzielna przez 5 = Buzz
 # liczba podzielna przez 3 i 5 = FizzBuzz

zakres = range(1,101)

for liczba in zakres:
    if liczba % 3 == 0 and liczba % 5 == 0:
        print("FizzBuzz")
    elif liczba % 5 == 0:
        print("Buzz")
    elif liczba % 3 == 0:
        print("Fizz")
    else:
        print(liczba)