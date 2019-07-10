'''
set-matrix-zeroes
'''

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(m n) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

'''
思路
1、暴力法:设定一个同样大小的矩阵,每次遇到0,然后将第二个矩阵的相应位置置0,空间复杂度为O(mn)。
2、略微优化:每次遇到0的时候,记录需0的行号和列号,空间复杂度为O(m+n)。
3、空间复杂度为1,只需要将2中0的行号列号的记录在第一行和第一列就行了。
 利用第一行和第一列的元素去标记该行或该列是否在更新时要全部变成0。但是这样操作会使得第一行和第一列的原始状态丢失。
 因此,我们需要额外一个变量hasZeros去保存第一列(或者第一行)在更新时是否要变成0,这样就不会有问题了。
'''


class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        if not m or not n:
            return
        # print(matrix)
        hasZeros = 0  # 我们需要额外一个变量hasZeros去保存第一列(或者第一行)在更新时是否要变成0
        for i in range(m):  # 第i行
            if matrix[i][0] == 0:  # 第零列
                hasZeros = 1

            for j in range(1, n):  # 第i行的第j列(除了第0列)
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
            # print(matrix)

        for i in range(m - 1, -1, -1):  # i = 2,1,0
            for j in range(n - 1, 0, -1):  # j = 2,1
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    # 第零列的第i行,或第零行的第i列任一个为零,则将第i行第j列的元素置为零
                    matrix[i][j] = 0
            if hasZeros == 1:
                matrix[i][0] = 0


if __name__ == '__main__':
    so = Solution()
    a = [[1, 3, 5], [10, 0, 16], [23, 30, 34]]  # 二维数组
    so.setZeroes(a)
    print(a)
