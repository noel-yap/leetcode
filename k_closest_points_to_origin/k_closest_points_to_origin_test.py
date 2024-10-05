import unittest

import k_closest_points_to_origin


class TestKClosestPointsToOrigin(unittest.TestCase):
    def test_k_closest_points_to_origin(self):
        expected = [[3, 3], [-2, 4]]

        actual = k_closest_points_to_origin.k_closest_points_to_origin([[3, 3], [5, -1], [-2, 4]], 2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
