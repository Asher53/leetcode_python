'''
sqrtx
'''
'''
Implementint sqrt(int x).
Compute and return the square root of x.
'''

'''
二分查找 算法的时间复杂度是O(logn)，空间复杂度是O(1)
'''


class Solution:
    def sqrt(self, x):
        if not x:
            return 0
        i = 1
        j = x // 2 + 1
        while i <= j:
            center = (i + j) >> 1
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j


if __name__ == '__main__':
    a = 9
    so = Solution()
    print(so.sqrt(a))
