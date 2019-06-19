'''
divide-two-integers
'''
'''
Divide two integers without using multiplication, division and mod operator.
'''

'''
解题思路：不许用乘、除和求余实现两数的相除。那就只能用加和减了。正常思路是被除数一个一个的减除数，直到剩下的数比除数小为止，
就得到了结果。这样是无法ac的，因为时间复杂度为O(n)，比如一个很大的数除1，就很慢。这里我们可以用二分查找的思路，可以说又是二分查找的变种。
'''


class Solution:
    def divide(self, dividend, divisor):
        a = abs(dividend)
        b = abs(divisor)
        # 被除数小于除数
        if a < b:
            return 0

        res = 0
        while a >= b:
            sum = b
            count = 1
            # todo 很聪明的解法，加快速度
            while sum + sum <= a:
                sum += sum
                # 并非加1，而是加count
                count += count
            a -= sum
            # print(a)
            res += count

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res


if __name__ == '__main__':
    so = Solution()
    a, b = 19, 3
    print(so.divide(a, b))
