'''
maximum-depth-of-binary-tree
'''

'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root):
        if not root:
            return 0
        return max(self.dfs(root.left), self.dfs(root.right)) + 1


if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(3)
    node3 = TreeNode(10)
    node4 = TreeNode(1)
    node5 = TreeNode(6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    so = Solution()
    res = so.dfs(node1)
    print(res)
