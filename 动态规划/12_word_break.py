'''
word-break
'''
'''
dynamic programmin 动态规划
'''

'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of 
one or more dictionary words.
For example, given
s ='leetcode',
dict =['leet', 'code'].
Return true because'leetcode'can be segmented as'leet code'.
'''

'''
dp[0] = True 是为了处理空串
循环字符串的每一个字符
第二程循环: 找到true的位置开始计算
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        # dp[i] = true means that s[0, i -1] can be constructed by the words in wordDict.
        # So, dp[0] must be ture. 因为要处理空串的情况
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1):
                # 如果dp[j]为True
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break  # 直接跳出，不用判断其子串
        print(dp)
        return dp[n]


if __name__ == '__main__':
    s = 'leetcode'
    # s = ''
    dict = ['leet', 'code']
    # s = 'applepenapple'
    # dict = ['apple', 'pen']
    # s = 'catsandog'
    # dict = ['cat', 'cats', 'and', 'sand', 'dog']
    so = Solution()
    print(so.wordBreak(s, dict))
