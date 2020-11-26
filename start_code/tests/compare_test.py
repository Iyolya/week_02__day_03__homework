import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_5_10_returns_5_is_less_than_10(self):
        self.assertEqual("5 is less than 10", compare(5, 10))

    def test_compare_4_4_returns_numbers_are_the_same(self):
        self.assertEqual("numbers are the same", compare(4, 4))
        