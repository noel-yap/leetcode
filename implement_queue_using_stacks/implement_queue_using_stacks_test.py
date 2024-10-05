import unittest

import implement_queue_using_stacks


class TestImplementQueueUsingStacks(unittest.TestCase):
    def test_1(self):
        q = implement_queue_using_stacks.MyQueue()

        q.push(0)
        self.assertEqual([0], q.stack1)
        self.assertEqual([], q.stack2)

        q.push(1)
        self.assertEqual([0, 1], q.stack1)
        self.assertEqual([], q.stack2)

        q.push(2)
        self.assertEqual([0, 1, 2], q.stack1)
        self.assertEqual([], q.stack2)

        n = q.pop()
        self.assertEqual([], q.stack1)
        self.assertEqual([2, 1], q.stack2)
        self.assertEqual(0, n)

        n = q.peek()
        self.assertEqual([], q.stack1)
        self.assertEqual([2, 1], q.stack2)
        self.assertEqual(1, n)

        q.push(3)
        self.assertEqual([3], q.stack1)
        self.assertEqual([2, 1], q.stack2)

        n = q.pop()
        self.assertEqual([3], q.stack1)
        self.assertEqual([2], q.stack2)
        self.assertEqual(1, n)


if __name__ == '__main__':
    unittest.main()
