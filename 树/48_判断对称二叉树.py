'''
symmetric-tree
'''
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def help(self, p, q):
        if not p and not q:
            return True
        if p.val == q.val:
            return self.help(p.left, q.right) and self.help(p.right, q.left)
        return False

    # 第一次时把一棵树变成两棵树传进来
    def isSymmetrical(self, root):
        if not root:
            return True
        return self.help(root.left, root.right)


if __name__ == '__main__':
    #     node1 = TreeNode(1)
    #     node2 = TreeNode(2)
    #     node3 = TreeNode(3)
    #     node4 = TreeNode(4)
    #     node5 = TreeNode(5)
    #     node6 = TreeNode(6)
    #     node7 = TreeNode(7)

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    so = Solution()
    print(so.isSymmetrical(node1))
