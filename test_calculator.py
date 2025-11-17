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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()