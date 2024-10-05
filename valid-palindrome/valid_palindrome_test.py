import unittest

from valid_palindrome import valid_palindrome

class TestValidPalindrome(unittest.TestCase):
    def test_empty(self):
        expected = True

        actual = valid_palindrome("")

        self.assertEqual(expected, actual)

    def test_not_palindrome(self):
        expected = False

        actual = valid_palindrome("aoeu")

        self.assertEqual(expected, actual)

    def test_odd_length(self):
        expected = True

        actual = valid_palindrome("aoa")

        self.assertEqual(expected, actual)

    def test_even_length(self):
        expected = True

        actual = valid_palindrome("aooa")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()