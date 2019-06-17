'''
4sum
'''

'''
实际上转换为了2sum
'''

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.
Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

'''
哈希表用空间换时间，以增加空间复杂度的代价来降低时间复杂度。首先建立一个字典dict，字典的key值为数组中每两个元素的和，
每个key对应的value为这两个元素的下标组成的元组，元组不一定是唯一的。 
如对于num=[1,2,3,2]来说，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}。 
这样就可以检查target-key这个值在不在dict的key值中，如果target-key在dict中并且下标符合要求，那么就找到了这样的一组解。
由于需要去重，这里选用set()类型的数据结构，即无序无重复元素集。最后将每个找出来的解(set()类型)转换成list类型输出即可。
'''


class Solution:
    def fourSum(self, nums, target):

        n = len(nums)
        res = set()
        adict = {}

        # 如果输入数字不够直接返回空列表
        if n < 4:
            return []

        # 构建哈希表
        nums = sorted(nums)
        for i in range(n):
            for j in range(i + 1, n):
                adict[nums[i] + nums[j]] = adict.get(nums[i] + nums[j], []) + [[i, j]]
        # print(adict)

        for i in range(n):
            for j in range(i + 1, n - 2):
                digit = target - nums[i] - nums[j]
                if digit in adict:
                    for item in adict[digit]:
                        if item[0] > j:  # 必须大于j，不能与数本身重复
                            # todo 使用res.add 方法
                            res.add((nums[i], nums[j], nums[item[0]], nums[item[1]]))
        # print(res)
        # return [list(k) for k in res]
        return list(map(list, res))


if __name__ == '__main__':
    so = Solution()
    numbers = [1, 0, -1, 0, -2, 2]
    # numbers = [1, 2, 3, 2]
    target = 0
    print(so.fourSum(numbers, target))
