'''
triangle
'''
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row
below.For example, given the following triangle
[
     [2],
    [3,4],
   [6,7,5],
  [4,1,8,3]
]
The minimum path sum from top to bottom is11(i.e., 2 + 3 + 6 + 1 = 12).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

'''
给定一个三角形，找出从顶到底的最小路径和，每一步可以从上一行移动到下一行相邻的数字
    [                   
         [2],                 [2],              
        [3,4],               [3, 4],            [2],
       [6,5,7],      ==>   [7, 6, 10]     ==>  [9, 10]   ==>     [11]
      [4,1,8,3]
    ]
 
/**思路:
    * 自底向上 dp: 不需要额外的空间
    * dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    * dp[i][j]: 表示到达 (i, j)最小路径的总和
*/
 
'''


class Solution:
    def minimumTotal(self, triangle):
        cum = triangle[-1]  # 最开始就是最后一排（长度最长），不需要管边界，管前不管后
        for row in triangle[-2::-1]:  # todo 从倒数第二个[6, 7, 5]开始
            # print(row)
            for j in range(len(row)):
                cum[j] = min(cum[j], cum[j + 1]) + row[j]
            # print(cum)
        return cum[0]


if __name__ == '__main__':
    a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # a = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    so = Solution()
    print(so.minimumTotal(a))
