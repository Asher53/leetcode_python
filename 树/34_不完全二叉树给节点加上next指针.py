'''
Populating Next Right Pointers in Each Node II
'''

'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

'''
这一题针对于不完全二叉树，用层次遍历的思想做
'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
'''
pre在当前层移动，cur在上一层移动
'''

class Solution:
    def connect(self, root):
        # 当前节点
        cur = root
        # 按层次进行遍历
        while cur:
            # 前一个结点
            pre = None
            # 每一层的第一个结点
            firstNode = None
            # 处理每一层
            while cur:
                # 如果是每一层的第一个结点
                if not firstNode:
                    firstNode = cur.left if cur.left else cur.right
                if cur.left:
                    # 跨越父结点
                    if pre:
                        pre.next = cur.left
                    # 第一个结点
                    pre = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    pre = cur.right
                cur = cur.next  # 可以指向空
            cur = firstNode  # 下一层的第一个节点


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.right = node7

    so = Solution()
    so.connect(node1)
    # print(node1.left.right.next.val)
