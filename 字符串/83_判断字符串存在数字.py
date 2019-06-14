'''
valid-number
'''
'''
Validate if a given string is numeric.
Some examples:
"0"=>true
" 0.1 "=>true
"abc"=>false
"1 a"=>false
"2e10"=>true
Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
'''


class Solution(object):
    def isNumber(self, s):
        begin, last = 0, len(s) - 1

        # 将字符串前后的空格去掉
        while begin <= last and s[begin] == ' ':
            begin += 1
        while begin <= last and s[last] == ' ':
            last -= 1

        # 数字前为正号或者负号的情况，首位后移
        if begin < last and (s[begin] == '+' or s[begin] == '-'):
            begin += 1

        num, dot, exp = False, False, False

        while begin <= last:

            # 该字符为数字
            if s[begin] >= '0' and s[begin] <= '9':
                num = True

            # 若首位为"."则返回false，否则标记为小数
            elif s[begin] == '.':
                if dot or exp:
                    return False
                dot = True

            # 若首位为"e"或"E",则返回false，否则标记为科学计数
            elif s[begin] == 'e' or s[begin] == 'E':
                if exp or not num:
                    return False
                exp, num = True, False  # 后面必须有数字才行啊

            # 若遇到正负号，则判断前一位是否为字符"e"或"E"
            elif s[begin] == '+' or s[begin] == '-':
                if s[begin - 1] != 'e':
                    return False
            else:
                return False
            begin += 1
        return num


if __name__ == '__main__':
    a = ' .1e9'
    so = Solution()
    print(so.isNumber(a))
