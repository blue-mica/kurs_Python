class Monitor(object):
    def __init__(self, prod, przek, proporcje="16:9"):
        self.producent = prod
        self.przekatna = przek
        self.kolor = "czarny"
        self.proporcje = proporcje
        self.wlaczony = False

    def wlacz(self):
        if not self.wlaczony:
            self.wlaczony = True
            print(f"Monitor zostal {self.producent} zostal wlaczony")
        else:
            print("Monitor jest juz wlaczony")

    def wylacz(self):
        if self.wlaczony:
            self.wlaczony = False
            print(f"Monitor {self.producent} jest wylaczony")
        else:
            print("Monitor jest juz wylaczony")

    def __str__(self):
        return f"Monitor producent: {self.producent}\n" \
               f"        przekatna: {self.przekatna}\n" \
               f"        proporcje: {self.proporcje}"