'''
construct-binary-tree-from-inorder-and-postorder-traversal
'''

'''
Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
'''
'''
每次读到的后序的最后一个数一定是根节点，在中序找到这个数，它的左边是左子树，
右边是右子树
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, inorder, postorder):
        if not inorder:
            return
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        guide = inorder.index(postorder[-1])
        root.left = self.reConstructBinaryTree(inorder[:guide], postorder[:guide])
        root.right = self.reConstructBinaryTree(inorder[guide + 1:], postorder[guide + 1:len(postorder) - 1])
        return root


if __name__ == '__main__':
    inorder = [4, 2, 5, 1, 6, 3, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    so = Solution()
    print(so.reConstructBinaryTree(inorder, postorder).right.left.val)
