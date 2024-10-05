import unittest

from most_freq_int import most_frequent_int


class TestMostFrequentInt(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_most_frequent_int(self):
        expected = 2

        actual = most_frequent_int([2, 1, 2, 3, 2, 3, 2, 3, 2])

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
