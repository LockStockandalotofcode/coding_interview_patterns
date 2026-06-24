from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_midpoint(head: ListNode) -> ListNode:
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow