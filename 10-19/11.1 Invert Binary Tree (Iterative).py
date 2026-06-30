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

    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if not node.left:
            stack.append(node.left)
        if not node.right:
            stack.append(node.right)

    return root