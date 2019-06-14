'''
Given two numbers represented as strings, return multiplication of the numbers as a string.
Note: The numbers can be arbitrarily large and are non-negative.
'''


class Solution(object):
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    so = Solution()
    num_1 = '10'
    num_2 = '222'
    print(so.multiply(num_1, num_2))
