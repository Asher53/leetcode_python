'''
palindrome-partitioning
'''
'''
如果要求输出所有可能的解，往往都是要用dfs。如果是要求找出最优的解，或者解的数量，往往可以使用动态规划。
'''
'''
Given a string s, partition s such that every substring of the partition is a palindrome(回文).
Return all possible palindrome partitioning of s.
For example, given s ="aab",
Return
  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''


class Solution:
    def __init__(self):
        self.res = []

    def isPalindrome(self, s):
        return True if s == s[::-1] else False

    def dfs(self, s, stringlist=[]):
        if not s:
            self.res.append(stringlist)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist + [s[:i]])
        return self.res


if __name__ == '__main__':
    s = 'aab'
    so = Solution()
    print(so.dfs(s))
