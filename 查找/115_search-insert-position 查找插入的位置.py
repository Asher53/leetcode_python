'''
search-insert-position
'''

'''
二分查找
'''

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it 
would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''


class Solution:
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1
        # 等号必不可少
        while left <= right:
            mid = (left + right) >> 1
            # print(mid, left, right)
            # +-1而不是直接等于mid
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid
        # 已经详细的分清了是返回mid还是返回right
        return left


if __name__ == '__main__':
    a = [1, 3, 5, 6]
    so = Solution()
    print(so.searchInsert(a, 2))
