'''
count-and-say
'''
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...
1 is read off as"one 1"or 11.
11 is read off as"two 1s"or 21.
21 is read off as"one 2, then one 1"or 1211.
Given an integer n, generate the n th sequence.
Note: The sequence of integers will be represented as a string.
'''

'''
题意就是迭代生成字符串：后一个字符串是前一个字符串每个连续出现的数字的个数＋该数字拼凑而成
'''


class Solution(object):
    def countStr(self, s):
        count = 0
        ans = ''
        tmp = s[0]
        for i in range(len(s)):
            if s[i] == tmp:
                count += 1
            else:
                ans += str(count) + tmp
                tmp = s[i]
                count = 1
        ans += str(count) + tmp
        return ans

    def countAndSay(self, n):
        ans = '1'
        while n > 1:
            ans = self.countStr(ans)
            n -= 1
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.countAndSay(3))
