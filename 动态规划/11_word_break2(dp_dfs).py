'''
word-break-ii
'''
'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s ='catsanddog',
dict =['cat', 'cats', 'and', 'sand', 'dog'].
A solution is['cats and dog', 'cat sand dog'].
'''

'''
dp+dfs： 这道题不只像word break那样判断是否可以分割，而且要找到所有的分割方式，那么我们就要考虑dfs了。
不过直接用dfs解题是不行的，为什么？因为如果全部遍历一遍，时间复杂度太高，无法通过oj。
使用word break题中的动态规划的结果，在dfs之前，先判定字符串是否可以被分割，如果不能被分割，直接跳过这一枝。实际上这道题是dp+dfs。
'''


class Solution(object):
    def __init__(self, wordDict):
        self.res = []
        self.wordDict = wordDict

    def dfs(self, s, stringlist=''):
        if self.check(s):
            # 如果s已经切完，则加入最后结果集
            if not s:
                self.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in self.wordDict:
                    self.dfs(s[i:], stringlist + ' ' + s[:i])
        return self.res

    # def nocheck_dfs(self, s, stringlist=''):
    #     if not s:
    #         self.res.append(stringlist[1:])
    #     for i in range(len(s)):
    #         if s[:i+1] in self.wordDict:
    #             self.dfs(s[i+1:], stringlist+' '+ s[:i+1])

    def check(self, s):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1):
                if dp[j] and s[j:i + 1] in self.wordDict:
                    dp[i + 1] = True
                    break
        return dp[n]


if __name__ == '__main__':
    s = 'catsanddog'
    dict = ['cat', 'cats', 'and', 'sand', 'dog']
    so = Solution(dict)
    print(so.dfs(s))
