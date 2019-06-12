'''
subsets-ii
'''
'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S =[1,2,2], a solution is:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    def subsetsWithDup(self, S):
        S.sort()
        self.res = []
        self.dfs(0, [])
        return self.res

    def dfs(self, start, valuelist):
        if valuelist not in self.res:
            self.res.append(valuelist)
        # 经典dfs
        for i in range(start, len(S)):
            # print(valuelist + [S[i]])
            self.dfs(i + 1, valuelist + [S[i]])


if __name__ == '__main__':
    so = Solution()
    S = [1, 2, 3]
    print(so.subsetsWithDup(S))
