'''
longest-palindromic-substring
'''
'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
'''

'''
求最长的回文子字符串
'''

'''
中心扩展法：
step 1:遍历每个字符,把每个字符当做中心逐步向两边扩展,每扩展一步就得到一个新的子串。这里针对输入字符串的长度，扩展方式需要根据长度奇偶性质做判断。
Step 2:判断子串是否为回文串，更新当前最长回文串
Step 3:返回最长回文串
'''


class Solution(object):
    def longestPalindrome(self, s):
        lens = len(s)
        maxlen = 0
        start = 0

        # 长度为奇数
        # 以某个点为中心
        for i in range(lens):
            j = i - 1
            k = i + 1
            while j >= 0 and k < lens and s[j] == s[k]:
                if k - j + 1 > maxlen:
                    maxlen = k - j + 1
                    start = j
                j -= 1
                k += 1

        # 长度为偶数
        for i in range(lens):
            j = i
            k = i + 1
            while j >= 0 and k < lens and s[j] == s[k]:
                if k - j + 1 > maxlen:
                    maxlen = k - j + 1
                    start = j
                j -= 1
                k += 1

        if maxlen > 0:
            return s[start:start + maxlen]
        return None


if __name__ == '__main__':
    s = 'dabae'
    so = Solution()
    print(so.longestPalindrome(s))
