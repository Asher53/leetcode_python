'''
binary-tree-maximum-path-sum
'''

# '''
# Given a binary tree, find the maximum path sum.
# The path may start and end at any node in the tree.
# For example:
# Given the below binary tree,
#        1
#       / \
#      2   3
# Return6.
# '''
#
#
# '''
# 求一棵二叉树中最大的路径和。该路径可以是二叉树中某一节点到树中任意一个节点的所经过的路径，不允许重复经过一个节点，不必经过根节点。
# '''
#
# '''
# 我们现在要求最大路径和，那么就要分别得到左右两条路径的最大和。而左路径的最大和为左节点的值加上它左右路径中较大的路径和，
# 右路径最大和为右节点的值加上它左右路径中较大的路径和。
# 注意：如果某条子路径的左右节点为负，直接置为0，等于不走这个节点。
# '''


'''
解题思路：这道题是在树中寻找一条路径，这条路径上的节点的和为最大，起点和终点只要是树里面的节点就可以了。这里需要注意的一点是：
节点值有可能为负值。解决这道二叉树的题目还是来使用递归。例如下面这棵树：

　　　　　　　　　　　　1

　　　　　　　　　　/     \

　　　　　　　　　2       3

    　　　　　/    \    /  \

　　　　　　 4     5    6    7

对于这棵树而言，和为最大的路径为：5->2->1->3->7。

那么这条路径是怎么求出来的呢？这里需要用到一个全局变量Solution.max，可以随时被更大的路径和替换掉。在函数递归到左子树时：
最大的路径为：4->2->5。但此时函数的返回值应当为4->2和5->2这两条路径中和最大的一条。右子树同理。
而Solution.max用来监控每个子树中的最大路径和。那么思路就是：
（左子树中的最大路径和，右子树中的最大路径和，以及左子树中以root.left为起点的最大路径（需要大于零）+
右子树中以root.right为起点的最大路径（需要大于零）+root.val），这三者中的最大值就是最大的路径和。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        self.maxSum = 0  # todo 负无穷的表示手法
        self.dfs(root)
        # print(self.maxPathSum)
        return self.maxSum

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # print(left, right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.maxSum = max(self.maxSum, root.val + left + right)   # root的值+左右节点的值
        return max(left, right) + root.val   # 返回左右路径中较大的值+根节点的值


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(-7)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(2)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    # 测试2: 测试为0的意义
    # node1 = TreeNode(1)
    # node2 = TreeNode(-7)
    # node3 = TreeNode(12)
    #
    # node1.left = node2
    # node1.right = node3

    so = Solution()
    res = so.maxPathSum(node1)
    print(res)

'''
附加
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''


# '''
# 思路：
# expectNumber-root.val，递归找
# '''
#
# '''
# 代码：
# 递归的过程（通过此题懂）
# 返回结果 [[root.val]]，[root.val]+i，最终是一个二维列表
# '''
#
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def dfs(self, root, expectNumber):
#         if not root:
#             return []
#         if not root.left and not root.right and root.val == expectNumber:
#             return [[root.val]]
#         res = []
#         left = self.dfs(root.left, expectNumber - root.val)
#         right = self.dfs(root.right, expectNumber - root.val)
#         for i in left + right:  # 两个列表直接相加
#             res.append([root.val] + i)
#         # print(res)
#         return res


# if __name__ == '__main__':
#     node1 = TreeNode(1)
#     node2 = TreeNode(2)
#     node3 = TreeNode(3)
#     node4 = TreeNode(4)
#     node5 = TreeNode(7)
#     node6 = TreeNode(6)
#     node7 = TreeNode(6)
#
#     node1.left = node2
#     node1.right = node3
#
#     node2.left = node4
#     node2.right = node5
#
#     node3.left = node6
#     node3.right = node7
#
#     so = Solution()
#     res = so.dfs(node1, 10)
#     print(res)
