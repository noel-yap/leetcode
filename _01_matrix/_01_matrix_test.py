import unittest

import _01_matrix


class Test01Matrix(unittest.TestCase):
    def test__01_matrix(self):
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

        actual = _01_matrix.update_matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
