import unittest

from max_profit import max_profit


class TestMaxProfit(unittest.TestCase):
    def test_1(self):
        expected = 5

        actual = max_profit([7, 1, 5, 3, 6, 4])

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = 0

        actual = max_profit([7,6,4,3,1])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
