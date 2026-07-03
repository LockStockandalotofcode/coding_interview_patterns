from ds import TreeNode
from typing import List, Optional

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def build_binary_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    # BASE CASE
    if not preorder or not inorder:
        return None

    # OPTIMISED RECURSIVE SOLUTION DFS
    inorder_map = {value : idx for idx, value in enumerate(inorder)}

    pre_idx = 0 # global tracker

    def helper(instart, inend) -> Optional[TreeNode]:
        nonlocal pre_idx

        if instart > inend:
            return None

        # process current node: make a treenode, increment pre_idx
        node_val = preorder[pre_idx]
        node = TreeNode(node_val)

        pre_idx += 1

        mid = inorder_map[node_val]
        # recurse on left, right child nodes
        node.left = helper(instart, mid - 1)
        node.right = helper(mid + 1, inend)

        return node

    return helper(0, len(inorder) - 1)