'''
first-missing-positive
'''
'''
Given an unsorted integer array, find the first missing positive integer.
For example,
Given[1,2,0]return3,
and[3,4,-1,1]return2.
Your algorithm should run in O(n) time and uses constant space.
'''

'''
时间复杂度是 O(n)，空间复杂度是 O(1)
'''

'''
这题是个人觉得是很难的题目，我想了好久都没有想到怎么做。根据网上的答案才做出来的。这个是一个桶排序的扩展。
具体的思想就是把对应的数放到对应的位置，比如第0个数放1，第i个数放i+1. 
具体做法是，从数组第0个数开始，如果这个数不满足nums[i] == i + 1, 
那么他和第nums[i + 1]上的数互换，直到nums[i] == i + 1 或者他小于等于0或者他大于数组的长度。
由于每换一次，至少有一个位置满足nums[i] = i + 1。所以最多要换n次，所以时间复杂度是 O(n)。由于没有用额外的空间，那么满足题目要求。

遍历数组，调整数组中元素所处位置，保证数组中的大于0且小于等于数组长度的数i，都位于i-1的位置，即nums[i-1]=i，然后遍历数组，
第一个满足nums[i-1] != i的数，即为缺失的第一个正数
'''


class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[i] - 1:
                # 关键:tmp的位置
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 0]
    b = [3, 4, -1, 1]
    print(s.firstMissingPositive(b))
