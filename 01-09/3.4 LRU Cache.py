class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key -> node

        # initialising head and tail nodes, as a doubly linked list before our actual nodes
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        value = -1
        if key in self.hashmap:
            node = self.hashmap[key]
            value = node.val
            self.remove_node(node)
            self.add_to_tail(node)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove_node(hashmap[key])
        else:
            if len(self.hashmap) == self.capacity:
                lru_node = self.head.next
                self.remove_node(lru_node)
                del self.hashmap[lru_node.key]
        mru_node = DoublyLinkedListNode(key, value)
        self.hashmap[mru_node.key] = mru_node
        self.add_to_tail(mru_node)

    def add_to_tail(self, node: DoublyLinkedListNode) -> None:
        prev_node = self.tail.prev
        self.tail.prev =  node
        node.next = self.tail
        node.prev = prev_node
        prev_node.next = node 
    
    def remove_node(self, node: DoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
