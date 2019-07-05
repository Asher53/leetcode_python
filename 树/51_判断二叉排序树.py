'''
Given a binary tree, determine if it is a valid binary search tree (BST).
'''
'''
解题思路：看到二叉树我们首先想到需要进行递归来解决问题。这道题递归的比较巧妙。让我们来看下面一棵树：

　　　　　　　　　　　　　　　　　　4

　　　　　　　　　　　　　　　　　/    \

　　　　　　　　　　　　　　　　2　　    6

　　　　　　　　　　　　　　/    \   /   \

　　　　　　　　　　　　　1      3  5      7

对于这棵树而言，怎样进行递归呢？root.left这棵树的所有节点值都小于root，root.right这棵树的所有节点值都大于root。
然后依次递归下去就可以了。例如：如果这棵树是二叉查找树，那么左子树的节点值一定处于（负无穷，4）这个范围内，
右子树的节点值一定处于（4，正无穷）这个范围内。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def ValidBST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)

    def isValidBST(self, root):
        return self.ValidBST(root, -2147483648, 2147483647)

if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(5)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    so = Solution()
    print(so.isValidBST(node1))