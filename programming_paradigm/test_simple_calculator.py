# test_simple_calculator.py
import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add (5, 2) , 7)
        self.assertEqual(self.calc.add (-1, 1) , 0)
        self.assertEqual(self.calc.add (-2, -2) , -4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract (5, -2) , 7)
        self.assertEqual(self.calc.subtract (7, 2) , 5)
        self.assertEqual(self.calc.subtract (-4, 3) , -1)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply (7, 2) , 14)
        self.assertEqual(self.calc.multiply (7, -5) , -35)
        self.assertEqual(self.calc.multiply (-2, -2) , 4)

    def test_division(self):
        self.assertEqual(self.calc.divide (14, 2) , 7)
        self.assertEqual(self.calc.divide (-7, 2) , -3.5)
        self.assertEqual(self.calc.divide (-10, -2) , 5)
        self.assertIsNone(self.calc.divide (-10, 0))
        self.assertAlmostEqual(self.calc.divide (10, 3) , 3.33333, places=5)




        