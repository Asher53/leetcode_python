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
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedarray(nums)

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
    node1 = ListNode(1)
    node3 = ListNode(3)
    node6 = ListNode(6)
    node8 = ListNode(8)
    node10 = ListNode(10)

    node1.next = node3
    node3.next = node6
    node6.next = node8
    node8.next = node10

    so = Solution()
    res = so.sortedListToBST(node1)
    print(res.val)

    print(so.NodeList(res))

'''
附加
'''

'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
二叉搜索树的中序遍历即是有序的
树转化成了双向链表(结构是相同的)
先中序遍历，再转化为链表
'''

'''
代码
学习中序遍历（递归）
两边节点的设置
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     # 中序遍历
#     def NodeList(self, pRootOfTree):
#         if not pRootOfTree:
#             return []
#         return self.NodeList(pRootOfTree.left) + [pRootOfTree] + self.NodeList(pRootOfTree.right)  # 直接括上对象
#
#     def Convert(self, pRootOfTree):
#         res = self.NodeList(pRootOfTree)  # 没有给出双向链表的类，改造res(现在是一个对象列表)
#         # 注：最后应该变成[1,3,6,8,10,14]
#         # for i in range(6):
#         #     print(res[i].val)
#         if not res:
#             return None
#         if len(res) == 1:
#             return pRootOfTree
#
#         # 两边的节点
#         res[0].left = None
#         res[0].right = res[1]
#         res[-1].left = res[-2]
#         res[-1].right = None
#
#         # todo 就利用树的结构即可，都有左右指针，就是把列表的东西加上指针
#         for i in range(1, len(res)-1):
#             res[i].left = res[i-1]
#             res[i].right = res[i+1]
#         return res[0]
#
# if __name__ == '__main__':
#     node1 = TreeNode(8)
#     node2 = TreeNode(3)
#     node3 = TreeNode(10)
#     node4 = TreeNode(1)
#     node5 = TreeNode(6)
#     node6 = TreeNode(14)
#
#
#
#     node1.left = node2
#     node1.right = node3
#
#     node2.left = node4
#     node2.right = node5
#
#     node3.right = node6
#
#     so = Solution()
#     res = so.Convert(node1)
#     print(res)
