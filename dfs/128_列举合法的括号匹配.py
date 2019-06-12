'''
generate-parentheses
'''
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

'''
解题思路：列举出所有合法的括号匹配，使用dfs。如果左括号的数量大于右括号的数量的话，就不能产生合法的括号匹配。
'''


class Solution:
    def dfs(self, l, r, item):
        # print(item)
        if l > r:
            return
        if not l and not r:
            self.res.append(item)
        if l > 0:
            self.dfs(l - 1, r, item + '(')
        if r > 0:
            self.dfs(l, r - 1, item + ')')

    def generateParenthesis(self, n):
        if not n:
            return []
        self.res = []
        self.dfs(n, n, '')
        return self.res


if __name__ == '__main__':
    so = Solution()
    print(so.generateParenthesis(2))
