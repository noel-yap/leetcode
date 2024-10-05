#!/usr/bin/env python3

import unittest
import invert_binary_tree


class TestBinTree(unittest.TestCase):
    def test_to_list(self):
        expected = [4, 2, 7, 1, 3, 6, 9]

        n = invert_binary_tree.BinTree([4, 2, 7, 1, 3, 6, 9])

        actual = list(n)

        self.assertEqual(expected, actual)


class TestInvertBinaryTree(unittest.TestCase):
    def test_1(self):
        expected = [4, 7, 2, 9, 6, 3, 1]

        actual = invert_binary_tree.invert_binary_tree([4, 2, 7, 1, 3, 6, 9])

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = [2, 3, 1]

        actual = invert_binary_tree.invert_binary_tree([2, 1, 3])

        self.assertEqual(expected, actual)

    def test_3(self):
        expected = []

        actual = invert_binary_tree.invert_binary_tree([])

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
