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
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12)
        self.assertEqual(multiplicacion(0, 99), 0)
        self.assertEqual(multiplicacion(-2, 5), -10)
    
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(9, 3), 3)
        self.assertEqual(division(7, 2), 3.5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(10, 0)

    def test_negativos(self):
        self.assertEqual(suma(-3, -7), -10)
        self.assertEqual(resta(-5, -2), -3)
        self.assertEqual(multiplicacion(-4, -4), 16)
        self.assertEqual(division(-9, 3), -3)

    def test_decimales(self):
        self.assertAlmostEqual(suma(1.1, 2.2), 3.3, places=1)
        self.assertAlmostEqual(division(1, 3), 0.333, places=3)
        self.assertEqual(multiplicacion(0.5, 4), 2.0)

    def test_casos_extremos(self):
        self.assertEqual(suma(999999, 1), 1000000)
        self.assertEqual(multiplicacion(0, 999999), 0)
        self.assertEqual(division(0, 5), 0)
        self.assertAlmostEqual(division(1, 7), 0.142857, places=5)
if __name__ == "__main__":
    unittest.main()