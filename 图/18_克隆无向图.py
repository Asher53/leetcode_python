'''
clone-graph
'''
'''
Clone an undirected graph. Each node in the graph contains avaland a list of itsneighbors.
OJ's undirected graph serialization:
Nodes are valed uniquely.
We use#as a separator for each node, and,as a separator for node val and each neighbor of the node.
As an example, consider the serialized graph{0,1,2# 1,2# 2,2}.
The graph has a total of three nodes, and therefore contains three parts as separated by#.
First node is valed as0. Connect node0to both nodes1and2.
Second node is valed as1. Connect node1to node2.
Third node is valed as2. Connect node2to node2(itself), thus forming a self-cycle.
Visually, the graph looks like the following:
'''

'''
题目解析：给定一个无向图，图内节点包括节点值、节点的邻居；需要复制该图

解题思路：
很明显的广度优先的问题
主要技巧在于如何标记节点已经访问 和 如何复制邻居节点
可以采用一个map，记录 原节点 和 复制节点
该map ：
一 可以用作标记 节点是否访问
二 也可以解决 复制邻居的问题：
访问每个邻居节点时，没访问过 新建其复制节点
访问过，从map中获取其复制节点
每个邻居节点的复制节点 都应该和 当前跟节点的复制节点(从map中获取) 建立 邻居关系
'''


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []


# 图的BFS
class Solution:
    def cloneGraph(self, node):
        if not node:
            return
        q = [node]
        hashtable = {}
        copy = UndirectedGraphNode(node.val)
        # todo 建立map，跟踪已经访问的节点,键为node，值为只有val的node
        hashtable[node] = copy
        while q:
            t = q.pop()
            for i in t.neighbors:
                if i not in hashtable:
                    co = UndirectedGraphNode(i.val)
                    hashtable[i] = co
                    # todo 若邻居未访问过，该邻居节点入队, 否则不需要入队
                    q.append(i)
                # 用hashtable就能添加邻居
                hashtable[t].neighbors.append(hashtable[i])
        # todo 返回值
        return copy


if __name__ == '__main__':
    a = UndirectedGraphNode(0)
    b = UndirectedGraphNode(1)
    c = UndirectedGraphNode(2)

    a.neighbors = [b, c]
    b.neighbors = [c]
    c.neighbors = [c]

    so = Solution()
    print(so.cloneGraph(a).neighbors[1].neighbors[0].val)
