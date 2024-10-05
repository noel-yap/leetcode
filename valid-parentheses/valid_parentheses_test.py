import unittest

from valid_parentheses import valid_parentheses


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        expected = True

        actual = valid_parentheses("")

        self.assertEqual(expected, actual)

    def test_balanced_braces(self):
        expected = True

        actual = valid_parentheses("{}")

        self.assertEqual(expected, actual)

    def test_too_many_open_braces(self):
        expected = False

        actual = valid_parentheses("{")

        self.assertEqual(expected, actual)

    def test_too_many_close_braces(self):
        expected = False

        actual = valid_parentheses("}")

        self.assertEqual(expected, actual)

    def test_inside_out_braces(self):
        expected = False

        actual = valid_parentheses("}{")

        self.assertEqual(expected, actual)

    def test_interleaved(self):
        expected = False

        actual = valid_parentheses("{[(}])")

        self.assertEqual(expected, actual)

    def test_happy_path(self):
        expected = True

        actual = valid_parentheses("(()[]{})[(()[]{})]{[(()[]{})]}")

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()