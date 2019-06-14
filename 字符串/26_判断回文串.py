'''
valid-palindrome
'''
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
'A man, a plan, a canal: Panama'is a palindrome.
'race a car'is not a palindrome.
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
'''

'''
组成新字符串，保留字母和数字，最后小写
两个函数 isdigit() 判断字母 isalpha() 判断字符
lower全部变为小写
字符串相加
'''


class Solution:
    def isPalindrome(self, s):
        a = ''
        for x in s:
            # print(x)
            if x.isalpha() or x.isdigit():
                a = a + x
        a = a.lower()
        # a = ''.join([x for x in s if x.isalpha() or x.isdigit()]).lower()
        if a == a[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    # s = 'race a car'
    so = Solution()
    print(so.isPalindrome(s))

    # #  isdigit() 方法检测字符串是否只由数字组成。
    # ss = '123456'
    # print(str.isdigit(ss))

    # isalpha() 方法检测字符串是否只由字母组成, 如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False
    # ss = "runoob"
    # print(ss.isalpha())
    #
    # ss = "Runoob example....wow!!!"
    # print(ss.isalpha())

    # ss = "runo1ob"
    # print(ss.isalpha())
