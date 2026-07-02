from ds import TreeNode
from typing import List

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def build_binary_tree( preorder: List[int], inorder: List[int]) -> TreeNode:
    # RECURSIVE SOLUTION DFS

    # BASE CASE
    if not preorder or not inorder:
        return None

    # PROCESS CURRENT NODE
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)

    # MOVE ON TO CHILDREN NODES
    root.left = build_binary_tree(preorder[ 1 : mid+1], inorder[ : mid])
    root.right = build_binary_tree(preorder[mid+1 : ], inorder[mid + 1 : ])

    return root