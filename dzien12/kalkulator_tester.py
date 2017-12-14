from unittest import TestCase
from dzien12.kalkulator import *


class KalkulatorTesty(TestCase):

    def setUp(self):
        self.a = 33
        self.b = 3

    def test_dodaj(self):
        # arrange
        wynik_oczekiwany = self.a + self.b
        # act
        wynik_rzeczywisty = dodaj(self.a, self.b)

        #assert
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany, msg="Wartosci obliczone sa rozne")

    def test_odejmij(self):
        # arrange
        wynik_oczekiwany = self.a - self.b

        #act
        wynik_rzeczywisty = odejmi(self.a, self.b)

        #asser
        self.assertEqual(wynik_rzeczywisty, wynik_oczekiwany)