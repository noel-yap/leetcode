from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def linked_list_cycle(head: ListNode) -> bool:
    slow = head
    fast = head.next

    try:
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
    except AttributeError:
        return False

    return True