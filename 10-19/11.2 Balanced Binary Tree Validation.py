from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def balanced_binary_tree_validation(root: TreeNode) -> bool:
    # recursive solution 
    #  height = -1 implies imbalance
    return get_height_imbalance(root) != -1

def get_height_imbalance(node: TreeNode) -> int:
    # base case
    if not node:
        return 0
        
    # if any subtree is imbalanced
    left_stree_ht = get_height_imbalance(node.left)
    right_stree_ht = get_height_imbalance(node.right)
    if left_stree_ht == -1 or right_stree_ht == -1:
        return -1
        
    # if this node is imbalanced
    if abs(left_stree_ht - right_stree_ht) > 1:
        return -1
    
    # otherwise propagate height upward
    return 1 + max(left_stree_ht, right_stree_ht)