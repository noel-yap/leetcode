import unittest

import lowest_common_ancestor_of_a_binary_search_tree


class TestLowestCommonAncestorOfABinarySearchTree(unittest.TestCase):
    def test_1(self):
        expected = 6

        actual = lowest_common_ancestor_of_a_binary_search_tree.lowest_common_ancestor_of_a_binary_search_tree(
            [6, 2, 8, 0, 4, 7, 9, 3, 5],
            2,
            8)

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = 2

        actual = lowest_common_ancestor_of_a_binary_search_tree.lowest_common_ancestor_of_a_binary_search_tree(
            [6, 2, 8, 0, 4, 7, 9, 3, 5],
            0,
            5)

        self.assertEqual(expected, actual)

    def test_3(self):
        expected = 6

        actual = lowest_common_ancestor_of_a_binary_search_tree.lowest_common_ancestor_of_a_binary_search_tree(
            [6, 2, 8, 0, 4, 7, 9, 3, 5],
            6,
            2)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
