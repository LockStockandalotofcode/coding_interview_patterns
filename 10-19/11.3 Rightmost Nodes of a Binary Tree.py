from ds import TreeNode
from typing import List
from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def rightmost_nodes_of_a_binary_tree(root: TreeNode) -> List[int]:
    if not root:
        return []

    queue = deque([root])
    level_size = 1
    res = []

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()
            # append child nodes
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # process current node
            if i == level_size - 1:
                res.append(node.val)
    
    return res