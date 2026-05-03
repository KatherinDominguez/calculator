import unittest
from model import suma, resta, multiplicacion, division
class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5, "La suma de 2 y 3 debe ser 5")
        self.assertEqual(suma(0, 0), 0, "La suma de 0 y 0 debe ser 0")
        self.assertEqual(suma(100, 200), 300, "La suma de 100 y 200 debe ser 300")

    def test_resta(self):
        self.assertEqual(resta(10, 3), 7, "La resta de 10 y 3 debe ser 7")
        self.assertEqual(resta(0, 0), 0, "La resta de 0 y 0 debe ser 0")
        self.assertEqual(resta(5, 10), -5, "La resta de 5 y 10 debe ser -5")

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 4), 12, "La multiplicación de 3 y 4 debe ser 12")
        self.assertEqual(multiplicacion(0, 99), 0, "La multiplicación de 0 y 99 debe ser 0")
        self.assertEqual(multiplicacion(-2, 5), -10, "La multiplicación de -2 y 5 debe ser -10")

    def test_division(self):
        self.assertEqual(division(10, 2), 5, "La división de 10 entre 2 debe ser 5")
        self.assertEqual(division(9, 3), 3, "La división de 9 entre 3 debe ser 3")
        self.assertEqual(division(7, 2), 3.5, "La división de 7 entre 2 debe ser 3.5")

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
    
    def test_negativos(self):
        self.assertEqual(suma(-3, -7), -10, "La suma de -3 y -7 debe ser -10")
        self.assertEqual(resta(-5, -2), -3, "La resta de -5 y -2 debe ser -3")
        self.assertEqual(multiplicacion(-4, -4), 16, "La multiplicación de -4 y -4 debe ser 16")
        self.assertEqual(division(-9, 3), -3, "La división de -9 entre 3 debe ser -3")

    def test_decimales(self):
        self.assertAlmostEqual(suma(1.1, 2.2), 3.3, places=1, msg="La suma de 1.1 y 2.2 debe ser 3.3")
        self.assertAlmostEqual(division(1, 3), 0.333, places=3, msg="La división de 1 entre 3 debe ser 0.333")
        self.assertEqual(multiplicacion(0.5, 4), 2.0, "La multiplicación de 0.5 y 4 debe ser 2.0")

    def test_casos_extremos(self):
        self.assertEqual(suma(999999, 1), 1000000, "La suma de 999999 y 1 debe ser 1000000")
        self.assertEqual(multiplicacion(0, 999999), 0, "La multiplicación de 0 y 999999 debe ser 0")
        self.assertEqual(division(0, 5), 0, "La división de 0 entre 5 debe ser 0")
        self.assertAlmostEqual(division(1, 7), 0.142857, places=5, msg="La división de 1 entre 7 debe ser 0.142857")
if __name__ == "__main__":
    unittest.main()