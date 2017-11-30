file_path = "dane.txt"

try:
    with open(file_path, 'r') as file:
        print(file.read())
# except FileNotFoundError:  # w przypadku konkretnego typu bledu
#     print("Nie ma pliku")
except Exception as e:  # blok except przechwyci typ bledu jaki wystapil i zapisze sie dp "e"
    print("Uuups nastapil blad", e)
finally:
    print("Ta funkcja zawsze sie wykona")

try:
    print("To jest blok try")
    raise ValueError("Sam tworze wyjatek1 typ ValueError")
except ValueError as e:
    print("Zlapalem wyjatek", e)
finally:
    print("Zawsze sie wykonam")