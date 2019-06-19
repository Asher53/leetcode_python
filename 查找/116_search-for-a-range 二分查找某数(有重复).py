'''
search-for-a-range
'''

'''
已指定用二分查找 算法的时间复杂度是O(logn)，空间复杂度是O(1)
'''

'''
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return[-1, -1].
For example,
Given[5, 7, 7, 8, 8, 10] and target value 8,
return[3, 4].
'''


class Solution(object):
    def searchRange(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start <= end and start >= 0 and end <= len(nums) - 1:
            mid = (start + end) >> 1
            if nums[mid] == target:
                start = mid
                end = mid
                while start > 0 and nums[start - 1] == nums[start]:
                    start = start - 1
                while end < len(nums) - 1 and nums[end] == nums[end + 1]:
                    end = end + 1
                return [start, end]
            else:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = start + 1
        return [-1, -1]


if __name__ == '__main__':
    a = [5, 7, 7, 8, 8, 8, 10]
    so = Solution()
    print(so.searchRange(a, 8))
