import unittest
from model import suma, resta, multiplicacion, division
class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(100, 200), 300)

    def test_resta(self):
        self.assertEqual(resta(10, 3), 7)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(5, 10), -5)
