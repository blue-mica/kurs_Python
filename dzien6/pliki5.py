sciezka = "tekst1.txt"

# with open(sciezka, 'w') as plik:  #w trybie 'w' po otwarciu pliku cała zawartość zostaje usunięta (nawet bez zapisywania)
#     print(plik.tell())

tekst = """To jest tekst. Zachowam jego formsatowanie. 
Bo mam go 
w potrojnym czydzyslowiu."""

with open(sciezka, 'r+') as plik:
    print(plik.tell())
    plik.write(tekst)
    plik.seek(0)
    plik.read() # w trzbie 'w" nie mozna czytac pliku