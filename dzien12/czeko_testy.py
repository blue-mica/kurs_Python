from unittest import TestCase
from dzien10.czekolada import Czekolada
from tools.catch_print import *


class CzekoTesty(TestCase):

    def test_podaj_mase(self):
        czekolada = Czekolada(150, "mleczna", "wedel")
        oczekiwana_masa = 150

        rzeczywista_masa = czekolada.podaj_mase()

        self.assertEqual(rzeczywista_masa, oczekiwana_masa)

    def test_podaj_producenta(self):
        czekolada = Czekolada(150, "mleczna", "wedel")
        oczekiwany_prod = "wedel"

        rzeczywisty_prod = get_print_output(czekolada.podaj_producenta)

        self.assertEqual(rzeczywisty_prod, oczekiwany_prod)
