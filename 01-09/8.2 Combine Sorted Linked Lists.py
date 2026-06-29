from typing import List
from ds import ListNode
import heapq

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    # using min heap, and custom comparator to sort as per value of a node
    
    min_heap = []
    ListNode.__lt__ = lambda self, other: self.val < other.val

    # push initial nodes on heap
    # traverse through, popping min node with pop, and creating res linked list
    D = ListNode(-1, None)
    curr = D
    for head in lists:
        if head:
            heapq.heappush(min_heap, head)
    
    while min_heap:
        # pop minimum node
        smallest_node = heapq.heappop(min_heap)
        curr.next = smallest_node
        curr = curr.next

        if smallest_node.next:
            heapq.heappush(min_heap, smallest_node.next)
        
    return D.next