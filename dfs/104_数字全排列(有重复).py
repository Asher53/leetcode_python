'''
permutations
'''
'''
Given a collection of numbers, return all possible permutations.
For example,
[1,2,3]have the following permutations:
[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2], and[3,2,1].
'''


class Solution(object):
    def permute(self, nums):
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if not nums:
            self.res.append(path)
        else:
            for i in range(len(nums)):
                # print(nums[:i])
                # print(nums[i + 1:])
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]])


if __name__ == '__main__':
    ss = [1, 2, 3]
    # ss = [1, 1, 2]
    so = Solution()
    print(so.permute(ss))
