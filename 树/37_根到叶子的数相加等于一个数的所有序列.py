'''
path-sum-ii
'''
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left+right:  # 两个列表直接相加
            res.append([root.val]+i)
        return res

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
    node55 = TreeNode(5)


    node5.left = node4
    node5.right = node8

    node4.left = node11
    node11.left = node7
    node11.right = node2

    node8.left = node13
    node8.right = node44
    node44.right = node1
    node44.left = node55

    so = Solution()
    res = so.FindPath(node5, 22)
    print(res)