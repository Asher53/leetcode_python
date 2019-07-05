'''
balanced-binary-tree
'''
'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.
'''

'''
方案: dfs，和二叉树的最大深度结合，自顶向下验证
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, root):
        if not root:
            return True
        if abs(self.dfs(root.left) - self.dfs(root.right)) > 1:
            return False
        return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)

    def dfs(self, proot):
        if not proot:
            return 0
        return max(self.dfs(proot.left), self.dfs(proot.right)) + 1

if __name__ == '__main__':
    node5 = TreeNode(5)
    node2 = TreeNode(2)
    node8 = TreeNode(8)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node3 = TreeNode(3)



    node5.left = node2
    node5.right = node8

    node2.left = node1
    node2.right = node4

    node4.left = node3


    so = Solution()
    res = so.IsBalanced_Solution(node5)
    print(res)