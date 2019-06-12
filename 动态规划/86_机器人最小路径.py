'''
Minimum Path Sum
'''
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''

'''
注: 只能从局部考虑
用一个二维矩阵a[i][j]代表从(0，0)到(i，j)的最小和。那么a[i][j] = min(a[i-1][j],a[i][j -1]) + nums[i][j]。
那么这题也是一个动态规划问题，只需要把a的整个表打出来就可以了。时间复杂度是O(m×n)。
'''


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # 初始化边缘
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # print(dp) [[1, 4, 9, 16], [11, 0, 0, 0], [34, 0, 0, 0]]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        print(dp)
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    so = Solution()
    a = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print(so.minPathSum(a))
