'''
pascals-triangle
'''
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    def p_triangle(self, numRows):
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            pascal = [[] for _ in range(numRows)]  # todo  构造 [[], [], [], [], []]
            # print(pascal)
            for i in range(numRows):
                pascal[i] = [1 for _ in range(i + 1)]  # [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
            for i in range(2, numRows):
                for j in range(1, i):
                    pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            return pascal


if __name__ == '__main__':
    so = Solution()
    print(so.p_triangle(5))
