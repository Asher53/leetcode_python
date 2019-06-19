'''
search-in-rotated-sorted-array-ii
'''

'''
算法的时间复杂度是O(logn)，空间复杂度是O(1)
'''

'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
'''

'''
这道是之前那道 Search in Rotated Sorted Array 在旋转有序数组中搜索 的延伸，现在数组中允许出现重复数字，这个也会影响我们选择哪半边继续搜索，
由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，
则左半段是有序的。而如果可以有重复值，就会出现下面两种情况，[3 1 1] 和 [1 1 3 1]，对于这两种情况中间值等于最右值时，目标值3既可以在左边又可以在右边，
'''

'''
很明显的二分查找的题目，是search-in-rotated-sorted-array的拓展题目，变的是加了一个可能含有重复数字。
这样的话，如果直接进行左右指针的比较就不知道向哪个方向搜索了，所以，需要在正式比较之前，先移动左指针(右指针)，
使他指向一个和右指针(左指针)不同的数字上。
然后再做查找。
'''


class Solution(object):
    def search(self, nums, target):
        N = len(nums)
        l, r = 0, N - 1

        # todo 只需改动这一部分
        while l <= r:
            while l < r and nums[l] == nums[r]:
                l += 1

            mid = (l + r) >> 1
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


if __name__ == '__main__':
    a = [2, 5, 6, 0, 0, 1, 2]
    so = Solution()
    print(so.search(a, 1))
