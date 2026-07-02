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

def binary_search_tree_validation(root: TreeNode) -> bool:
    return dfs_helper(root, float('-inf'), float('inf'))

    # recursive method
def dfs_helper(node: TreeNode, lowerbound: int, upperbound: int) -> bool:
    # base case : reaching leaf node
    if not node:
        return True
    
    # wherever false encountered, propagate upward
    if not lowerbound < node.val < upperbound:
        return False
    
    # if a child node does not comply, propagate it 
    if not dfs_helper(node.left, lowerbound, node.val):
        return False
    if not dfs_helper(node.right, node.val, upperbound):
        return False
    
    return True