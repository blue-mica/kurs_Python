from dzien9.monitor import Monitor

monitor1 = Monitor("Dell", 19)
print(f"Monitor {monitor1.producent} ma przekatna {monitor1.przekatna} cali")

monitor1.kolor = "czarny"

print(monitor1.kolor)

monitor2 = Monitor("HP",24)
print(f"Monitor {monitor2.producent} ma przekatna {monitor2.przekatna} cali")
