import unittest

import longest_substring_without_repeating_characters


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def test_1(self):
        expected = 3

        actual = longest_substring_without_repeating_characters.length_of_longest_substring("abcabcbb")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
