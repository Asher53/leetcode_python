'''
subsets
'''

'''
Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S =[1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution:
    def subsets(self, nums):
        self.nums = nums
        self.res = []
        self.dfs(0, [])
        return self.res

    def dfs(self, index, path):
        # print(path)
        self.res.append(path)
        for i in range(index, len(self.nums)):
            self.dfs(i + 1, path + [self.nums[i]])


if __name__ == '__main__':
    s = [1, 2, 3]
    so = Solution()
    print(so.subsets(s))
