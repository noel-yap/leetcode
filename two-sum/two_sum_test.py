import unittest

import two_sum


class Test(unittest.TestCase):
    def test_1(self):
        expected = (0, 1)

        actual = two_sum.two_sum([2, 7, 11, 15], 9)

        self.assertEqual(actual, expected)

    def test_2(self):
        expected = (1, 2)

        actual = two_sum.two_sum([3, 2, 4], 6)

        self.assertEqual(actual, expected)

    def test_3(self):
        expected = (0, 1)

        actual = two_sum.two_sum([3, 3], 6)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
