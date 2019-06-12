'''
combinations
'''
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n, k):
        self.n = n
        self.k = k
        self.ret = []
        self.count = 0
        self.dfs(1, [])
        return self.ret

    def dfs(self, start, valuelist):
        if self.count == self.k:
            self.ret.append(valuelist)
            return
        for i in range(start, self.n + 1):
            self.count += 1
            self.dfs(i + 1, valuelist + [i])
            self.count -= 1


if __name__ == '__main__':
    so = Solution()
    print(so.combine(4, 2))
