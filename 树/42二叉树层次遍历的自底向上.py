'''
binary-tree-level-order-traversal-ii
'''

'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
For example:
Given binary tree{3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7]
  [9,20],
  [3],
]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def bfs(self, root):
        if not root:
            return []
        q = [root]
        while q:
            a = []
            for i in range(len(q)):
                t = q.pop(0)
                a.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            self.res.append(a)
        # self.res = list(reversed(self.res))
        return self.res[::-1]


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node3.left = node4
    node3.right = node5


    so = Solution()
    print(so.bfs(node1))