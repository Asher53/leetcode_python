'''
surrounded-regions
'''
'''
Given a 2D board containing'X'and'O', capture all regions surrounded by'X'.
A region is captured by flipping all'O's into'X's in that surrounded region.
For example
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
'''

'''
题目大意
给出一个铺满O或者X的区域，将被X围住的O都换成X
'''

'''
使用BFS或DFS从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。
而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，没有改变。然后遍历一遍，
将'O'置换为'X'，将'D'置换为'O'。 
'''

'''
技巧: DFS和BFS两种方法都可以，区别: 队列
'''


# 不需要返回值
class Solution:
    def __init__(self, board):
        self.board = board
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.queue = []  # 存储的未被包围的‘O’

    def solve(self):
        if not self.board:
            return

        # 怎样只搜索边界(分两次)
        for i in range(self.n):
            self.bfs(0, i)  # 第一行(边界)
            self.bfs(self.m - 1, i)  # 最后一行(边界)

        for j in range(1, self.m - 1):  # 中间部分的边界
            self.bfs(j, 0)  # 第0列
            self.bfs(j, self.n - 1)  # 最后一列

        for i in range(self.m):
            self.board[i] = list(map(lambda x: 'X' if x == 'O' else x, self.board[i]))

        for i in range(self.m):
            self.board[i] = list(map(lambda x: 'O' if x == 'D' else x, self.board[i]))

    def bfs(self, x, y):
        if x < 0 or y < 0 or x > self.m - 1 or y > self.n - 1 or self.board[x][y] != 'O':
            return
        self.board[x][y] = 'D'
        self.queue.append([x, y])
        while self.queue:
            t = self.queue.pop(0)
            t1 = t[0]
            t2 = t[1]
            self.bfs(t1 - 1, t2)
            self.bfs(t1 + 1, t2)
            self.bfs(t1, t2 - 1)
            self.bfs(t1, t2 + 1)

    def dfs(self, x, y):
        if x < 0 or y < 0 or x > self.m - 1 or y > self.n - 1 or self.board[x][y] != 'O':
            return
        self.board[x][y] = 'D'
        self.dfs(x - 1, y)
        self.dfs(x + 1, y)
        self.dfs(x, y - 1)
        self.dfs(x, y + 1)


if __name__ == '__main__':
    a = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    so = Solution(a)
    so.solve()
    print(a)
