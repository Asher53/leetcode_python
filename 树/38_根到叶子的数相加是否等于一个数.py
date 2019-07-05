'''
path-sum-ii
'''

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path5->4->11->2 which sum is 22.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, expectNumber):
        if not root:
            return []
        if not root.left and not root.right:
            return root.val == expectNumber
        return self.dfs(root.left, expectNumber-root.val) or self.dfs(root.right, expectNumber-root.val)


if __name__ == '__main__':
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node8 = TreeNode(8)
    node11 = TreeNode(11)
    node13 = TreeNode(13)
    node44 = TreeNode(4)
    node7 = TreeNode(7)
    node2 = TreeNode(2)
    node1 = TreeNode(1)

    node5.left = node4
    node5.right = node8

    node4.left = node11
    node11.left = node7
    node11.right = node2

    node8.left = node13
    node8.right = node44
    node44.right = node1

    so = Solution()
    res = so.dfs(node5, 22)
    print(res)