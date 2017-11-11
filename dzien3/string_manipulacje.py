# a. string wejściowy: „Ala ma kota, kot ma Ale”
# b. manipulujemy wejściem w dowolny sposób, tak aby otrzymać string
# wyjściowy. NIE MOŻNA DOSTARCZYĆ LITER, muszą one być wynikiem
# manipulacji (polecam zerknąć na tablicę ASCII i przypomnieć sobie
# wtorkowe spotkanie, być może przyda się funkcja ord() ;) )
# c. string wyjściowy „Arek woli psy, a najbardziej boksery”
# d. w razie pytań i wątpliwości służę pomocą – zapraszam na Slacka

zdanie_wejsciowe = "Ala ma kota, kot ma Ale"

print(ord("i"))
p = ord("p")
s = ord("s")
y = ord("y")
przecinek = ord(',')
n = ord("n")
j = ord('j')
b = ord('b')
d = ord('d')
z = ord('z')
i = ord('i')
r = ord('r')

nowe_zdanie = zdanie_wejsciowe[:1] + chr(114) + chr(101) + zdanie_wejsciowe[7] + ' ' + chr(119) + zdanie_wejsciowe[8]\
+ chr(108) + chr(105) + zdanie_wejsciowe[3] + chr(p) + chr(s) + chr(y) + chr(przecinek) + zdanie_wejsciowe[3]\
+ zdanie_wejsciowe[2] + zdanie_wejsciowe[3] + chr(n) + zdanie_wejsciowe[10] + chr(j) + chr(b) + zdanie_wejsciowe[10]\
+ chr(114) + chr(d) + chr(z) + chr(i) + zdanie_wejsciowe[22] + chr(j) + zdanie_wejsciowe[3] + chr(b) + zdanie_wejsciowe[8]\
+ zdanie_wejsciowe[7] + chr(s) + zdanie_wejsciowe[22] + chr(r) + chr(y)

print(nowe_zdanie)
