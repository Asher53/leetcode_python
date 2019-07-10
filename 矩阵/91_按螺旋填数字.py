'''
Given an integer n, generate a square matrix filled with elements from 1 to n 2 in spiral order.
For example,
Given n =3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

'''
详见 https://www.cnblogs.com/Blaxon/p/4725646.html?utm_source=tuicool
'''

'''
在列表前加*号，会将列表拆分成一个一个的独立元素[13, 14, 15, 16] [9, 10, 11, 12] [5, 6, 7, 8] [1, 2, 3, 4]
'''
class Solution:
    def generateMatrix(self, n):
        A, low = [], n * n + 1
        while low > 1:
            low, high = low - len(A), low
            print([list(range(low, high))])
            print(list(zip(*A[::-1])))
            A = [list(range(low, high))] + list(zip(*A[::-1]))
            print(A)
        return A


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(list(zip(*a[::-1])))
    so = Solution()
    print(so.generateMatrix(3))
