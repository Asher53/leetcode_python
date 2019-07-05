'''
binary-tree-preorder-traversal
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def midTraversal(self, root):  # 根左右
        if not root:
            return
        self.result.append(root)
        self.midTraversal(root.left)
        self.midTraversal(root.right)
        return self.result
