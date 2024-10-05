import unittest

import insert_interval


class TestInsertInterval(unittest.TestCase):
    def test_1(self):
        expected = [[1, 5], [6, 9]]

        actual = insert_interval.insert_interval([[1, 3], [6, 9]], [2, 5])

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = [[1, 2], [3, 10], [12, 16]]

        actual = insert_interval.insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])

        self.assertEqual(expected, actual)

    def test_before(self):
        expected = [[0, 1], [2, 3]]

        actual = insert_interval.insert_interval([[2, 3]], [0, 1])

        self.assertEqual(expected, actual)

    def test_before_overlap(self):
        expected = [[0, 3]]

        actual = insert_interval.insert_interval([[1, 3]], [0, 2])

        self.assertEqual(expected, actual)

    def test_outside(self):
        expected = [[0, 3]]

        actual = insert_interval.insert_interval([[1, 2]], [0, 3])

        self.assertEqual(expected, actual)

    def test_outside_overlap(self):
        expected = [[0, 4]]

        actual = insert_interval.insert_interval([[1, 2], [3, 4]], [0, 3])

        self.assertEqual(expected, actual)

    def test_inside(self):
        expected = [[0, 1], [2, 5], [6, 9]]

        actual = insert_interval.insert_interval([[0, 1], [2, 5], [6, 9]], [3, 4])

        self.assertEqual(expected, actual)

    def test_after(self):
        expected = [[0, 1], [2, 5], [6, 9]]

        actual = insert_interval.insert_interval([[0, 1], [2, 5]], [6, 9])

        self.assertEqual(expected, actual)

    def test_outside_2(self):
        expected = [[0, 1], [2, 10]]

        actual = insert_interval.insert_interval([[0, 1], [3, 4], [6, 9]], [2, 10])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
