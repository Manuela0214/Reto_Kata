import unittest

from src.files.challenge_3 import min_change

class TestMinChange(unittest.TestCase):
    def test_given_empty_list(self):
        result = min_change([])
        self.assertEqual(result,1)

    def test_coins_of_consecutive_values(self):
        result = min_change([1,2,3])
        self.assertEqual(result, 7)

    def test_coins_of_non_consecutive_values(self):
        result = min_change([2,4,5])
        self.assertEqual(result, 1)

    def test_unsorted_list(self):
        result = min_change([5,8,1,4,12,9])
        self.assertEqual(result, 2)
if __name__ == "__main__":
    unittest.main()