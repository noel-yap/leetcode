import unittest

import clone_graph


class TestCloneGraph(unittest.TestCase):
    def test_clone_graph(self):
        input_n1 = clone_graph.Node(1)
        input_n2 = clone_graph.Node(2)
        input_n3 = clone_graph.Node(3)
        input_n4 = clone_graph.Node(4)

        input_n1.neighbors = [input_n2, input_n4]
        input_n2.neighbors = [input_n1, input_n3]
        input_n3.neighbors = [input_n2, input_n4]
        input_n4.neighbors = [input_n1, input_n3]

        actual = clone_graph.NodeCloner().clone_graph(input_n1)
        
        expected_n1 = clone_graph.Node(1)
        expected_n2 = clone_graph.Node(2)
        expected_n3 = clone_graph.Node(3)
        expected_n4 = clone_graph.Node(4)

        expected_n1.neighbors = [expected_n2, expected_n4]
        expected_n2.neighbors = [expected_n1, expected_n3]
        expected_n3.neighbors = [expected_n2, expected_n4]
        expected_n4.neighbors = [expected_n1, expected_n3]

        self.assertEqual(expected_n1, actual)

    def test_empty_1(self):
        actual = clone_graph.NodeCloner().clone_graph(None)

        self.assertIsNone(actual)



if __name__ == '__main__':
    unittest.main()
