#  słowo krowa zamienić na krawat

slowo = "krowa"

# print(ord("a"))
# print(ord("t"))

ascii_code_a = 97
ascii_code_t = 116


litera_a = chr(ascii_code_a)
litera_t = chr(ascii_code_t)

nowe_slowo = slowo[:2] + litera_a + slowo[3:]
# print(nowe_slowo)

ostatnie_slowo = nowe_slowo + litera_t
print(ostatnie_slowo)