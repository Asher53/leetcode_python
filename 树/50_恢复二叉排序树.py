'''
recover-binary-search-tree
'''
'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
'''

'''
还是利用中序遍历是有序的这一特点，一个list存着节点，只需改变它指向的值即可
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root, list, listp):
        if not root:
            return
        self.inorder(root.left, list, listp)
        list.append(root.val)
        listp.append(root)
        self.inorder(root.right, list, listp)

    def recoverTree(self, root):
        list = []
        listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
        return root


if __name__ == '__main__':
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(6)
    node4 = TreeNode(1)
    node5 = TreeNode(5)
    node6 = TreeNode(3)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    so = Solution()
    print(so.recoverTree(node1).val)
