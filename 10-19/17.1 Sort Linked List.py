from ds import ListNode

def sort_linked_list(head: ListNode) -> ListNode:
    # split the list at middles
    # sort the two lists
    # merge the sorted lists

    #base case
    if not head or not head.next:
        return head
    
    second_head = split_linked_list(head) 
    # sort the two halves recursilvely
    l1 = sort_linked_list(head)
    l2 = sort_linked_list(second_head)

    # merge the sorted lists
    return merge(l1, l2)

def merge(head1: ListNode, head2: ListNode) -> ListNode:
    dummy = ListNode(0) #ListNode default next node is None
    tail = dummy # To append nodes at the end of dummy, without losing head of the merged linked list
    ptr1 = head1
    ptr2 = head2

    while ptr1 and ptr2:
        if ptr1.val < ptr2.val:
            tail.next = ptr1
            ptr1 = ptr1.next
        else:
            tail.next = ptr2
            ptr2 = ptr2.next
        tail = tail.next
    
    tail.next = ptr1 if ptr1 else ptr2
    return dummy.next
    
def split_linked_list(head: ListNode) -> ListNode:
    # 2 pointer technique
    # for even length, fast.next.next = null
    # for odd lenght, fast.next = null
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # split the list
    mid_head = slow.next
    slow.next = None
    return mid_head