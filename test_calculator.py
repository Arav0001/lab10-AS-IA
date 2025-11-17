# https://github.com/Arav0001/lab10-AS-IA
# Partner 1: Arav Sonawane
# Partner 2: Ismail Akdeniz
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertEqual(6, add(5, 1))
        self.assertEqual(7, add(-3, 10))

    def test_subtract(self):
        self.assertEqual(-6, subtract(2, 8))
        self.assertEqual(6, subtract(4, -2))
        self.assertEqual(7, subtract(11, 4))

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 1), 0)
        self.assertEqual(mul(-14, 6), -84)
        self.assertEqual(mul(10, 3), 30)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4.0, 12.4), 3.1)
        self.assertEqual(div(4, 0), 0)
    # ##########################

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(2, logarithm(10, 100))
        self.assertAlmostEqual(3, logarithm(2, 8))
        self.assertAlmostEqual(5, logarithm(3, 243))

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-4, 64)
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(100, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(9, 40), 41)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
            square_root(-2)
            square_root(-5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()