from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # case 1 - null node or one node is parent of another 
    if not root or root == p or root == q:
        return root

    # case 2 p and q both exist, present in subtrees of current node
    # p and q are non null, in subtrees of current node
    left_child = lowest_common_ancestor(root.left, p, q)
    right_child = lowest_common_ancestor(root.right, p, q)

    if left_child and right_child:
        return root

    # if one is null node, then return the other one
    return left_child if left_child else right_child