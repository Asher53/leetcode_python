'''
combination-sum
'''
'''
Given a collection of candidate numbers ( C ) and a target number ( T ), find all unique combinations in C where the candidate numbers sums to T .

Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a 1, a 2, … , a k) must be in non-descending order. (ie, a 1 ≤ a 2 ≤ … ≤ a k).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

'''
解题思路：和上一道题类似。只不过这道题要求candidate中的每个数只能使用一次。也是使用dfs。
增加了i+1，以及判定答案重复的步骤
'''


class Solution:
    def dfs(self, target, start, path):
        if not target and path not in self.res:
            return self.res.append(path)
        for i in range(start, self.n):
            if target < self.candidates[i]:
                return
            self.dfs(target - self.candidates[i], i + 1, path + [self.candidates[i]])

    def combinationSum(self, candidates, target):
        self.candidates = sorted(candidates)
        self.n = len(self.candidates)
        self.res = []
        self.dfs(target, 0, [])
        return self.res


if __name__ == '__main__':
    so = Solution()
    # a = [2, 3, 6, 7]
    a = [10, 1, 2, 7, 6, 1, 5]
    t = 7
    print(so.combinationSum(a, t))
