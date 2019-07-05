'''
Minimum Depth of Binary Tree
'''

'''
通过此题，学习DFS(递归)和BFS(队列)
'''

'''
Given a binary tree, find its minimum depth.The minimum depth is the number of nodes
along the shortest path from the root node down to the nearest leaf node.
'''

'''
给定一个二叉树，找到它的最小深度，最小深度是从根节点到叶节点的最短路径上的节点数。
'''

'''
DFS和BFS都可以，但是很明显，BFS更快，因为BFS只要找到第一个叶子结点就可以停止遍历了，而DFS需要通过迭代来遍历所有的结点。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
对比题目:给定一个二叉树，求其最大深度。 
最大深度指的是，从根节点到最远的叶子节点的最长路径的节点个数。
'''

# class Solution(object):
#     def maxDepth(self, root):
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
一个节点的最小高度不一定是两个子树的最小高度中较小的，当一个子树为空时，该节点的最小高度等于另一个子树的最小高度
'''
# 方法1: 深度优先搜索(DFS)
# class Solution:
#     def minDepth(self, root):
#         if not root:
#             return 0
#         if not root.left:
#             return self.minDepth(root.right) + 1
#         elif not root.right:
#             return self.minDepth(root.left) + 1
#         else:
#             return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# 方法2： 最优方法 广度优先搜索（BFS），用队列求解


'''
对比题目: 二叉树层次遍历: 队列结构
'''

# class Solution:
#     def minDepth(self, root):
#         l = []
#         if not root:
#             return []
#         q = [root]
#         while len(q):
#             t = q.pop(0)
#             l.append(t.val)
#             if t.left:
#                 q.append(t.left)
#             if t.right:
#                 q.append(t.right)
#         return l

'''
因为BFS只要找到第一个叶子结点就可以停止遍历了
'''
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            depth += 1
            for i in range(len(q)):
                t = q.pop(0)
                if not t.left and not t.right:
                    return depth
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return depth


if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(3)
    node3 = TreeNode(10)
    node4 = TreeNode(1)
    node5 = TreeNode(6)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    so = Solution()
    res = so.minDepth(node1)
    print(res)
