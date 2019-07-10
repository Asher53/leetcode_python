'''
求连通块的数量
'''

'''
利用矩阵idx给矩阵pic编号
'''

class Solution:
    def __init__(self, a):
        self.pic = a
        self.m = len(pic)
        self.n = len(pic[0])
        self.idx = [[0] * self.n for _ in range(self.m)]  # 连通分量编号

    def solve(self):
        cnt = 0  # 连通分量个数
        # 按行遍历
        for i in range(self.m):
            for j in range(self.n):
                # 第一次是第一个有O的位置， 第一个条件: 避免重复访问， 第二个条件：找到入口
                if self.idx[i][j] == 0 and self.pic[i][j] == 'O':
                    cnt += 1
                    self.dfs(i, j, cnt)
        print(self.idx)
        return cnt

    def dfs(self, x, y, cnt_id):
        if x < 0 or x > self.m - 1 or y < 0 or y > self.n - 1 or self.pic[x][y] != 'O' or self.idx[x][y] > 0:  # 出界
            return
        self.idx[x][y] = cnt_id
        self.dfs(x - 1, y, cnt_id)
        self.dfs(x + 1, y, cnt_id)
        self.dfs(x, y - 1, cnt_id)
        self.dfs(x, y + 1, cnt_id)


if __name__ == '__main__':
    pic = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['O', 'X', 'X', 'X']]
    so = Solution(pic)
    print(so.solve())
