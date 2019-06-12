'''
combination-sum-ii
'''
'''
Given a set of candidate numbers ( C ) and a target number ( T ), find all unique combinations in C where the candidate
numbers sums to T . The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a 1, a 2, … , a k) must be in non-descending order. (ie, a 1 ≤ a 2 ≤ … ≤ a k).
The solution set must not contain duplicate combinations.
For example, given candidate set2,3,6,7and target7,
A solution set is:
[7]
[2, 2, 3]
'''

'''
解题思路：和上一道题类似。只不过这道题要求candidate中的每个数只能使用一次。也是使用dfs。
'''


class Solution:
    def dfs(self, target, start, path):
        if not target:
            return self.res.append(path)

        for i in range(start, self.n):
            if target < self.candidates[i]:
                return
            self.dfs(target - self.candidates[i], i, path + [self.candidates[i]])

    def combinationSum(self, candidates, target):
        self.candidates = sorted(candidates)
        self.n = len(self.candidates)
        self.res = []
        self.dfs(target, 0, [])
        return self.res


if __name__ == '__main__':
    so = Solution()
    a = [2, 3, 6, 7]
    # a = [10,1,2,7,6,1,5]
    t = 7
    print(so.combinationSum(a, t))
