import unittest
from src.calculator import *

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        # self.assertEqual(5, add(2, 3))

        expected = 5
        actual = add(2, 3)
        self.assertEqual(expected, actual)

