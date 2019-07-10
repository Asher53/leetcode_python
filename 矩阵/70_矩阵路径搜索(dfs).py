'''
word-search
'''

'''
Given a 2D self.a and a self.s, find if the self.s exists in the grid.
The self.s can be constructed from letters of sequentially adjacent cell, where 'adjacent' cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given self.a =
[
  ['ABCE'],
  ['SFCS'],
  ['ADEE']
]
self.s ='ABCCED', -> returns true,
self.s ='SEE', -> returns true,
self.s ='ABCB', -> returns false.
'''


# 矩阵dfs
class Solution:
    def __init__(self, a, s):
        self.a = a
        self.m = len(a)
        self.n = len(a[0])
        self.s = s

    # 先找初始位置

    def ini(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.a[i][j] == self.s[0]:
                    if self.dfs(0, i, j):
                        return True
        return False

    def dfs(self, index, row, col):
        if row < 0 or row >= self.m or col < 0 or col >= self.n:  # 出界
            return False

        if self.s[index] == self.a[row][col]:
            self.a[row][col] = '#'  # 把这个位置置为#, 沿这个位置搜索
            if index == len(self.s) - 1 or self.dfs(index + 1, row + 1, col) or \
                    self.dfs(index + 1, row - 1, col) or \
                    self.dfs(index + 1, row, col + 1) or \
                    self.dfs(index + 1, row, col - 1):
                return True
            self.a[row][col] = self.s[index]  # 需要恢复
        return False


if __name__ == '__main__':
    marix = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    # st = ['S', 'E', 'E']
    st = ['A', 'B', 'C', 'B']
    # st = ['A', 'B', 'C', 'C', 'E', 'D']
    so = Solution(marix, st)
    print(so.ini())
