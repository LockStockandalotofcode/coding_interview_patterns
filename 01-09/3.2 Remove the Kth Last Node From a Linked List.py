from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # CREATE DUMMY NODE AHEAD OF HEAD, TO HANDLE EDGE CASE WHERE HEAD NODE NEEDS TO BE REMOVED
    dummy = ListNode(-1)
    dummy.next = head
    
    # initialise all 
    trailer = dummy
    leader = dummy
    # MOVE LEADER NODE AHEAD OF TRAILER BY K STEPS
    for _ in range(k):
        leader = leader.next
        # in case k is more than length of linked list
        if not leader:
            return head
            
    # MOVE LEADER AND TRAILER BOTH, UNTIL LEADER REACHES END 
    while leader.next:
        trailer = trailer.next
        leader = leader.next

    # REMOVE THE NODE NEXT TO TRAILER, Kth LAST NODE
    trailer.next = trailer.next.next
    return dummy.next # we cannot return HEAD, possibly head could be the Kth last node