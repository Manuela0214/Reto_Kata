import unittest

from src.files.challenge_1 import delete_digits

class TestDeleteDigits(unittest.TestCase):
    def test_given_empty_list(self):
        result = delete_digits([], 8)
        self.assertEqual(result, 'la lista esta vacía')

    def test_remove_digits_larger_than_s(self):
        result = delete_digits([129,25,1,9], 8)
        self.assertEqual(result,[1,25])

    def test_remove_digits_equals_to_s(self):
        result = delete_digits([84, 35, 8, 81, 8],8)
        self.assertEqual(result, [1,35,4])

    def test_evaluate_numbers_greater_than_100(self):
        result = delete_digits([129, 101, 85, 99, 100], 8)
        self.assertEqual(result,[100,5])

if __name__ == "__main__":
    unittest.main()