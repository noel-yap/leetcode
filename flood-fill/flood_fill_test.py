import unittest

import flood_fill


class TestFloodFill(unittest.TestCase):
    def test_flood_fill(self):
        expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

        actual = flood_fill.flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)

        self.assertEqual(expected, actual)

    def test_wide_grid(self):
        expected = [[2, 2, 1], [1, 2, 2]]

        actual = flood_fill.flood_fill([[0, 0, 1], [1, 0, 0]], 1, 1, 2)

        self.assertEqual(expected, actual)

    def test_tall_grid(self):
        expected = [[1, 2], [2, 2], [2, 1]]

        actual = flood_fill.flood_fill([[1, 0], [0, 0], [0, 1]], 1, 1, 2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
