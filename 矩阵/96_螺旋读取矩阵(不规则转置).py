# '''
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ]
#  [ 4, 5, 6 ]
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
# '''
#


'''
两步操作: 先取矩阵第一行到结果，再将剩余部分转置+颠倒,再取矩阵第一行到结果...
'''


class Solution:
    def printMatrix(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = self.turn(matrix)  # 逆时针旋转矩阵
        return result

    '''
    m*n 转置+上下颠倒
    '''

    def turn(self, matrix):
        if not matrix:
            return
        num_r = len(matrix)
        num_c = len(matrix[0])
        # print(matrix)
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        # print(newmat)
        return newmat


if __name__ == '__main__':
    # a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    so = Solution()
    print(so.printMatrix(a))
