import unittest

import valid_anagram

class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        actual = valid_anagram.valid_anagram("aoeuaoeu", "aaooeeuu")

        self.assertTrue(actual)

    def test_invalid_anagram(self):
        actual = valid_anagram.valid_anagram("aoeuaoeu", "aoeu")

        self.assertFalse(actual)



if __name__ == '__main__':
    unittest.main()
