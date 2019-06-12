'''
palindrome-partitioning-ii
'''
'''
如果要求输出所有可能的解，往往都是要用dfs。如果是要求找出最优的解，或者解的数量，往往可以使用动态规划
'''

'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
For example, given s ="aab",
Return1since the palindrome partitioning["aa","b"]could be produced using 1 cut.
'''

'''
使用动态规划进行求解：用数组dp[i]记录从第0位到i位最小割数，使用i-1对第i个位置进行初始化，
如果子串s[j:i]是回文串，则dp[i] = min(dp[i],dp[j]+1)
'''


class Solution:
    def minCut(self, s):
        n = len(s)
        dp = [(i - 1) for i in range(n + 1)]  # [-1, 0, 1, 2, 3, 4] -> [-1, 0, 0, 1, 2, 2]
        for i in range(1, n + 1):
            for j in range(i):
                tmp = s[j:i]
                if self.isPalindrome(tmp):
                    dp[i] = min(dp[i], dp[j] + 1)
                    print(dp)
        return dp[n]

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False


if __name__ == '__main__':
    s = 'aabcc'
    # s = 'aabaa'
    so = Solution()
    print(so.minCut(s))
