'''
unique-paths-ii
'''
'''
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
Note: m and n will be at most 100.
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:  # 如果第一个格子有障碍，就无法走
            return 0

        m = len(obstacleGrid)  # 纵向
        n = len(obstacleGrid[0])  # 横向

        dp = [[0 for __ in range(n)] for __ in range(m)]  # 初始化，所有为0
        # 第一个可以走设置为1
        dp[0][0] = 1
        # 检查第一行和第一列是否有障碍
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    so = Solution()
    a = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    print(so.uniquePathsWithObstacles(a))
