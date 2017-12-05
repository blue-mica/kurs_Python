from dzien10.czekolada import Czekolada
from dzien10.producent import Producent

prod1 = Producent("Wedel", "Kraków")

czekol1 = Czekolada(400, "15", prod1)
czekol2 = Czekolada(600, "1,5", prod1)

print(czekol1)
print(czekol2)

print(czekol1 + czekol2)