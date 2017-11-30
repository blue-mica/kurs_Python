from dzien9.samochod import Samochod
from dzien9.silnik import Silnik

silnik_v4 = Silnik(1998, "benzyna")

bmw = Samochod("BMW", "3")

bmw.silnik = silnik_v4

print(bmw.silnik)

bmw.silnik.wlaczony = True