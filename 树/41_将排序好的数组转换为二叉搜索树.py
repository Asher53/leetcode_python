'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

'''
convert-sorted-list-to-binary-search-tree
'''
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

'''
可以用快慢指针，也可以转化为数组做,每次找中间的点设置左右子树
'''

'''
二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，
则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。
此外，二叉搜索树的中序遍历是有序的
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedarray(self, nums):
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(nums[0])
        size //= 2
        root = TreeNode(nums[size])
        root.left = self.sortedarray(nums[:size])
        root.right = self.sortedarray(nums[size + 1:])
        return root

    def NodeList(self, pRootOfTree):
        if not pRootOfTree:
            return []
        return self.NodeList(pRootOfTree.left) + [pRootOfTree.val] + self.NodeList(pRootOfTree.right)  # 直接括上对象


if __name__ == '__main__':
    a = [1, 3, 6, 8, 10]
    so = Solution()
    res = so.sortedarray(a)
    print(res.val)
    print(so.NodeList(res))
