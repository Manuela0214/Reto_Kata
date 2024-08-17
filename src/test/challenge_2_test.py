import unittest

from src.files.challenge_2 import get_squares

class TestGetSquares(unittest.TestCase):
    def test_given_empty_list(self):
        result = get_squares([],8)
        self.assertEqual(result, 'la lista esta vacía')

    def test_square_out_of_range(self):
        result = get_squares([-10,10], 8)
        self.assertEqual(result,[])

    def test_numbers_within_allowed_range(self):
        result = get_squares([1,2,3,5,6,8,9,10],8)
        self.assertEqual(result, [1,4,9,25,36,64,81])

if __name__ == "__main__":
    unittest.main()