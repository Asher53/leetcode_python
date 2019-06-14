'''
string-to-integer-atoi
'''
'''
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
all the input requirements up front.
spoilers alert... click to show requirements for atoi.
Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no
 effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of
representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''

'''
实现“atoi”函数，将字符串转换成整数。 
提示：请仔细考虑所有可能的输入情况。
思路方法
通过试错可以总结出要注意的四个点：
输入字符串为空、或其他不合法情况，返回0；
字符串开头的空格要在预处理中删掉；
处理可能出现的正负号“+”，“-”，正负号只能出现一次；
超出整数范围的值取整数范围的边界值。
'''

'''
字符串转化数字，先存到字符串
'''

class Solution(object):
    def myAtoi(self, str):
        if not str:
            return 0
        str = str.strip()
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10*number + ord(c) - ord('0')
            else:
                break
        number = flag * number
        # number = number if number <= 2147483647 else 2147483647
        # number = number if number >= -2147483648 else -2147483648
        return number

if __name__ == '__main__':
    so = Solution()
    print(so.myAtoi('+123'))


