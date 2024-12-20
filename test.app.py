import unittest
from app import reverse_string

class TestStringReversal(unittest.TestCase):
    def test_regular_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_palindrome(self):
        self.assertEqual(reverse_string("madam"), "madam")

    def test_numbers_and_symbols(self):
        self.assertEqual(reverse_string("12345!@#"), "#@!54321")

if __name__ == "__main__":
    unittest.main()