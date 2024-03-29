'''
decode-ways
'''
'''
A message containing letters fromA-Zis being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
For example,

Given encoded message"12", it could be decoded as"AB"(1 2) or"L"(12).
The number of ways decoding"12"is 2.
'''

'''

解题思路：解码有多少种方法。一般求“多少”我们考虑使用dp。假设dp[i]为以i为结尾的字符串解码方式数量的总和：
　　　　　当s[i-2:i]这两个字符是10~26但不包括10和20这两个数时，比如21，那么可以有两种编码方式（BA，U），所以dp[i]=dp[i-1]+dp[i-2]
　　　　　当s[i-2:i]等于10或者20时，由于10和20只有一种编码方式，所以dp[i]=dp[i-2]
　　　　  当s[i-2:i]不在以上两个范围时，如09这种，编码方式为0，而31这种，dp[i]=dp[i-1]。
　　　　  注意初始化时：dp[0]=1,dp[1]=1
'''


class Solution:
    def numDecodings(self, s):
        if s == "" or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':
                dp.append(dp[i - 1] + dp[i - 2])
            elif s[i - 2:i] == '10' or s[i - 2:i] == '20':
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        print(dp)
        return dp[len(s)]


if __name__ == '__main__':
    so = Solution()
    s = '12'
    print(so.numDecodings(s))
