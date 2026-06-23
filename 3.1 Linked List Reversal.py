from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_reversal(head: ListNode) -> ListNode:

    if not head:
        return None

    prev_node = None
    curr_node = head
    while curr_node is not None:
        next_node = curr_node.next # saving reference to next node
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    # prev_node is the head to the newly formed list, since curr_node must be None so that while loop terminated
    return prev_node