import unittest
from src.calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # self.assertEqual(5, add(2, 3))

        expected = 5
        actual = add(2, 3)
        self.assertEqual(expected, actual)

    def test_subtract(self):
        # self.assertEqual(3, subtract(10, 7))
        
        expected = 3
        actual = subtract(10, 7)
        self.assertEqual(expected, actual)