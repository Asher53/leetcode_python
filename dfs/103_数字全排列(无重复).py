'''
permutations-ii
'''
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2]have the following unique permutations:
[1,1,2],[1,2,1], and[2,1,1].
'''

'''
找出有可能有重复数字的一个数组的所有全排列。
'''

'''
是没有重复数字的，这个题有重复数字。我的做法很简单，就是在以前的基础上加了一个判断条件：
path not in res。这样的做法是在每个path生成之后才去做的判断，因此效率一点都不高。最后竟然也能通过了
'''


class Solution(object):
    def permuteUnique(self, nums):
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        if not nums and path not in self.res:
            self.res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]])


if __name__ == '__main__':
    ss = [1, 1, 2]
    so = Solution()
    print(so.permuteUnique(ss))
