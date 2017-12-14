import os, shutil, send2trash

# print(shutil.disk_usage("c:/"))

# pliki = os.listdir("E:\RepozytoriumGIT\kurs_Python\dzien12")
# print(pliki)

# send2trash.send2trash(E:\RepozytoriumGIT\kurs_Python\test.txt)

ilosc = 0

for biezacy_folder, podfoldery, pliki in os.walk("E:\RepozytoriumGIT\kurs_Python\dzien12"):
    # print("Obecny katalog:", biezacy_folder)
    #
    # for podfolder in podfoldery:
    #     print(f"podfolder {podfolder} w katalogu {biezacy_folder}")

    for plik in pliki:
        # print(f"plik {plik} w folderze {biezacy_folder}")
        ilosc += 1
print(f"Jest {ilosc} plikow")