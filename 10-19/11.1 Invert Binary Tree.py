from ds import TreeNode

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def invert_binary_tree(root: TreeNode) -> TreeNode:
    # swap every left and right subtree
    # dfs  recursive
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root