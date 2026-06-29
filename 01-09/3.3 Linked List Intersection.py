from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    ptrA = head_A
    ptrB = head_B

    while ptrA != ptrB:
        ptrA = ptrA.next if ptrA else head_B
        ptrB = ptrB.next if ptrB else head_A
    
    # either both nodes are at the intersection (if it exists) 
    # or both point to None, end of linked lists
    return ptrA
