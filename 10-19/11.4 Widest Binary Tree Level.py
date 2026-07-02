from ds import TreeNode
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def widest_binary_tree_level(root: TreeNode) -> int:
    # indexing each node, tracking width for every level
    if not root:
        return 0 

    max_width = 0
    queue = deque([(root, 0)]) # tuple of node, index

    # level order traversal
    while queue:
        level_size = len(queue)

        leftmost = queue[0][1]
        rightmost = queue[0][1]

        for _ in range(level_size):
            node, i = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * i))
            if node.right:
                queue.append((node.right, 2 * i + 1))
            
            # keep incrementing rightmost index
            # rightmost += 1, doing this would mean it only counts the non null nodes
            # correct is to move with index of nodes
            rightmost = i
        
        curr_width = rightmost - leftmost + 1
        max_width = max(max_width, curr_width)
        
    return max_width