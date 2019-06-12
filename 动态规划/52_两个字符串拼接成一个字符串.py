'''
interleaving-string
'''

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example,
Given:
s1 ="aabcc",
s2 ="dbbca",
When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
'''
The problem can be turned into subproblems. That is, Given s1, s2, s3, if we are to find whether s3 is formed by the 
interleaving(交错) of s1 and s2. We can firstly find whether s3[:-1] is formed by the interleaving of s1 and s2[:-1]
 (or s1[:-1] and s2), if so, and it happenes that the last character of s3 equals the last character of s2(or s1), 
 we can say the answer of the origin problem is True.
So, we use a 2d array dp[len(s1) + 1][len(s2) +1] to store mid answers. dp[i][j] means whether s1[:i] and s2[:j]
can form s3[i+j];
'''

'''
思路: dp[i][j]表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]
'''


class Solution:
    def isInterleave(self, s1, s2, s3):
        # if s1 == '':
        #     return s2 == s3
        # if s2 == '':
        #     return s1 == s3
        # if s3 == '':
        #     return s1 == s2 == ''
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len3 != len1 + len2:
            return False

        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        for i in range(1, len1 + 1):
            dp[i][0] = s1[:i] == s3[:i]

        for j in range(1, len2 + 1):
            dp[0][j] = s2[:j] == s3[:j]

        # dp[i][j]表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]) or (
                            dp[i][j - 1] and s3[i + j - 1] == s2[j - 1])
        return dp[len1][len2]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s3 = "aadbbbaccc"
    so = Solution()
    print(so.isInterleave(s1, s2, s3))
