import unittest

import balanced_binary_tree


class TestBalancedBinaryTree(unittest.TestCase):
    def test_balanced(self):
        n1 = balanced_binary_tree.TreeNode(15)
        n2 = balanced_binary_tree.TreeNode(7)
        n3 = balanced_binary_tree.TreeNode(20, left=n1, right=n2)
        n4 = balanced_binary_tree.TreeNode(9)
        n5 = balanced_binary_tree.TreeNode(3, left=n4, right=n3)

        actual = balanced_binary_tree.balanced_binary_tree(n5)

        self.assertTrue(actual)

    def test_unbalanced(self):
        n1 = balanced_binary_tree.TreeNode(4)
        n2 = balanced_binary_tree.TreeNode(4)
        n3 = balanced_binary_tree.TreeNode(3, left=n1, right=n2)
        n4 = balanced_binary_tree.TreeNode(3)
        n5 = balanced_binary_tree.TreeNode(2, left=n3, right=n4)
        n6 = balanced_binary_tree.TreeNode(2)
        n7 = balanced_binary_tree.TreeNode(1, left=n5, right=n6)

        actual = balanced_binary_tree.balanced_binary_tree(n7)

        self.assertFalse(actual)

    def test_empty(self):
        n = balanced_binary_tree.TreeNode(None)

        actual = balanced_binary_tree.balanced_binary_tree(n)

        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
