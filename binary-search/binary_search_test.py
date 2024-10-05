import unittest

import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        expected = 4

        actual = binary_search.binary_search([-1, 0, 3, 5, 9, 12], 9)

        self.assertEqual(expected, actual)

    def test_not_found(self):
        expected = -1

        actual = binary_search.binary_search([-1, 0, 3, 5, 9, 12], 2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
