'''
regular-expression-matching
'''
'''
Implement regular expression matching with support for'.'and'*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

'''
这道题目定义了两个正则表达式规则。’.’代表任意字符，’*’代表前一个字符出现任意次。输入两个字符串s，p。如果s可以被p完全匹配则返回True，
否则返回False。比如’.*’可以匹配任意字符串。
'''

import re


class Solution:
    def isMatch(self, s, p):
        res = re.match(p, s)
        if not res:
            return False
        else:
            return res.group() == s


if __name__ == '__main__':
    so = Solution()
    s1, s2 = 'aab', 'c*a*b'
    print(so.isMatch(s1, s2))
