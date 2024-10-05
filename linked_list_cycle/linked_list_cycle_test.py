import unittest

import linked_list_cycle

class TestLinkedListCycle(unittest.TestCase):
    def test_empty(self):
        l = linked_list_cycle.ListNode(None)

        actual = linked_list_cycle.linked_list_cycle(l)
    	
        self.assertFalse(actual)

    def test_no_cycle(self):
        l = linked_list_cycle.ListNode(1)

        actual = linked_list_cycle.linked_list_cycle(l)

        self.assertFalse(actual)

    def test_cycle_1(self):
        l1 = linked_list_cycle.ListNode(1)
        l2 = linked_list_cycle.ListNode(2)

        l1.next = l2
        l2.next = l1

        actual = linked_list_cycle.linked_list_cycle(l1)

        self.assertTrue(actual)

    def test_cycle_2(self):
        l1 = linked_list_cycle.ListNode(3)
        l2 = linked_list_cycle.ListNode(2)
        l3 = linked_list_cycle.ListNode(0)
        l4 = linked_list_cycle.ListNode(4)

        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l2

        actual = linked_list_cycle.linked_list_cycle(l1)

        self.assertTrue(actual)



if __name__ == '__main__':
    unittest.main()
