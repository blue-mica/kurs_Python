import pickle
samochody = [{"marka": "OPEL", "model": "CORSA", "rok": "1994"}, {"marka": "FIAT", "model": "126P", "rok": "1990"},\
            {"marka": "OPEL", "model": "ADAM", "rok": "2015"}, {"marka": "TOYOTA", "model": "COROLLA", "rok": "2001"}]

with open("auta.moni", 'wb') as plik:
    pickle.dump(samochody, plik)


#marka_set = set()

#for elem in samochody:
 #   for key in elem.keys():
 #       print(elem[key], end=" ")
  #  print(" ")

#    if elem["marka"] == "Opel":
 #       print(elem["model"])


#marka_set.add(elem["marka"])
#print(marka_set)

# print(slownik.items())
#
# for klucz, wartosc in slownik.items():
#     print(f"Klucz: {klucz} ma wartość {wartosc}")

