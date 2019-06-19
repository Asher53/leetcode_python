'''
search-a-2d-matrix
'''
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,
Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target =3, return true.
'''


class Solution:
    def Find(self, target, array):
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while i >= 0 and j <= cols:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False


if __name__ == '__main__':
    array = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]  # 二维数组
    print(array)
    target = int(input())
    print(target)
    s = Solution()
    print(s.Find(target, array))
