import unittest

from merge_two_sorted_lists import merge_sorted_lists


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_1(self):
        expected = [1, 1, 2, 3, 4, 4]

        actual = merge_sorted_lists([1, 2, 4], [1, 3, 4])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = []

        actual = merge_sorted_lists([], [])

        self.assertEqual(expected, actual)

    def test_first_empty(self):
        expected = [0]

        actual = merge_sorted_lists([], [0])

        self.assertEqual(expected, actual)

    def test_second_empty(self):
        expected = [0]

        actual = merge_sorted_lists([0], [])

        self.assertEqual(expected, actual)

    def test_dup(self):
        expected = [0, 0]

        actual = merge_sorted_lists([0], [0])

        self.assertEqual(expected, actual)

    def test_interleaved(self):
        expected = [1, 2, 3, 4]

        actual = merge_sorted_lists([1, 3], [2, 4])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
