from ds import TreeNode
from typing import Optional

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def max_path_sum(root: TreeNode) -> int:
    # base case 
    if not root: 
        return None

    # global variable
    max_sum = float('-inf')
    
    def helper(node: Optional[TreeNode]) -> int:
        nonlocal max_sum

        if not node:
            return 0

        # process current node's children,
        # take max with 0, to avoid negatives from travelling up the tree
        # if max_sum is -ve, it would get noticed by maX_sum here
        left_gain = max(helper(node.left), 0)
        right_gain = max(helper(node.right), 0)

        current_peak = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_peak)

        return node.val + max(left_gain, right_gain)
    
    helper(root)
    return max_sum
