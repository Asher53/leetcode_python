'''
construct-binary-tree-from-preorder-and-inorder-traversal
'''
'''
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
'''

'''
每次读到的前序的第一个数一定是根节点，在中序找到这个数，它的左边是左子树，
右边是右子树
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, preorder, inorder):
        if not inorder:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(preorder[0])
        guide = inorder.index(preorder[0])
        root.left = self.reConstructBinaryTree(preorder[1: guide + 1], inorder[:guide])
        root.right = self.reConstructBinaryTree(preorder[guide + 1:], inorder[guide+1:])
        return root




if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    so = Solution()
    print(so.reConstructBinaryTree(preorder, inorder).right.left.val)