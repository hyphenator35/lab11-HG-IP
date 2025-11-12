import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2), 6)
        self.assertEqual(mul(4,0), 0)
        self.assertNotEqual(mul(5,2), 7)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,6), 2.0)
        self.assertAlmostEqual(div(3,1), 0.33333, places = 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,3)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(6, 8), 10)
        self.assertNotEqual(hypotenuse(3,7), 1)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(36), 6)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
