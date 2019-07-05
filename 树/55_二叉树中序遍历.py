'''
binary-tree-inorder-traversal
'''
'''
Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree{1,#,2,3},
   1
    \
     2
    /
   3

return[3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?
'''

'''
Given a binary tree, return the postorder traversal of its nodes' values.
'''

'''
序是指根节点的浏览顺序，三种遍历都可以直接递归
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def midTraversal(self, root):  # 左根右
        if not root:
            return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right)
        return self.result


'''
附加: 二叉树的前序遍历 根左右
'''
# class Solution:
#     def __init__(self):
#         self.result = []
#
#     def midTraversal(self, root):  # 根左右
#         if not root:
#             return
#         self.result.append(root)
#         self.midTraversal(root.left)
#         self.midTraversal(root.right)
#         return self.result

'''
后序遍历: 左右根
'''


# class Solution:
#     def __init__(self):
#         self.result = []
#
#     def midTraversal(self, root):  # 左右根
#         if not root:
#             return
#         self.midTraversal(root.left)
#         self.midTraversal(root.right)
#         self.result.append(root)
#         return self.result


if __name__ == '__main__':
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)
    node6 = TreeLinkNode(6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6

    so = Solution()
    res = so.midTraversal(node1)
    [print(i.val) for i in res]
