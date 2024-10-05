import unittest

import maximum_subarray


class TestSquash(unittest.TestCase):
    def test_zero(self):
        expected = []

        actual = maximum_subarray.squash([0])

        self.assertEqual(expected, actual)

    def test_squash_positives_and_negatives(self):
        expected = [17, -3, 13]

        actual = maximum_subarray.squash([9, 8, -1, -2, 7, 6])

        self.assertEqual(expected, actual)

    def test_remove_negative_start_values(self):
        expected = [2]

        actual = maximum_subarray.squash([-1, 2])

        self.assertEqual(expected, actual)

    def test_remove_negative_end_values(self):
        expected = [2]

        actual = maximum_subarray.squash([2, -1])

        self.assertEqual(expected, actual)

    def test_remove_negative_start_sums(self):
        expected = [4]

        actual = maximum_subarray.squash([1, -3, 4])

        self.assertEqual(expected, actual)

    def test_remove_negative_end_sums(self):
        expected = [4]

        actual = maximum_subarray.squash([4, -3, 1])

        self.assertEqual(expected, actual)

    def test_1(self):
        expected = [4, -1, 3]

        actual = maximum_subarray.squash([-2, 1, -3, 4, -1, 2, 1, -5, 4])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
