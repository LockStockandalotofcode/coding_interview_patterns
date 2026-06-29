from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:

    # BASE CASE
    if not head or not head.next:
        return head
    
    immediate_next = head.next
    new_head = linked_list_reversal(head.next)
    immediate_next.next = head
    head.next = None
    return new_head