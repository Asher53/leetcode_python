'''
rotate-image
'''
'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
'''

'''
解题思路：先将矩阵转置，然后将矩阵的每一行翻转，就可以得到所要求的矩阵了。
'''
'''
此题分为两个操作
'''

# todo 转置和列表反转的操作
class Solution:
    def rotate(self, matrix):
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # # print(matrix)
        # for i in range(n):
        #     matrix[i].reverse()
        # return matrix
        # print(matrix[::-1])
        return list(map(list, list(zip(*matrix[::-1]))))


if __name__ == '__main__':
    # a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(a)
    so = Solution()
    print(so.rotate(a))
