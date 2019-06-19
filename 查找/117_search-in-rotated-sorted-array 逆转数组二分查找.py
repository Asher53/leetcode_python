'''
search-in-rotated-sorted-array
'''

'''
算法的时间复杂度是O(logn)，空间复杂度是O(1)
算法中log级别的时间复杂度都是由于使用了分治思想,这个底数直接由分治的复杂度决定。 
如果采用二分法,那么就会以2为底数,三分法就会以3为底数,其他亦然。
'''

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e.,0 1 2 4 5 6 7 might become4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''

'''
这道题是二分查找Search Insert Position的变体，看似有点麻烦，其实理清一下还是比较简单的。因为rotate的缘故，当我们切取一半的时候可能会出现误区，
所以我们要做进一步的判断。具体来说，假设数组是A，每次左边缘为l，右边缘为r，还有中间位置是m。在每次迭代中，分三种情况：
（1）如果target==A[m]，那么m就是我们要的结果，直接返回；
（2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，
否则就target在另一半，即把右边缘移到m-1。
（3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是否在这个范围内，相应的移动边缘即可。
根据以上方法，每次我们都可以切掉一半的数据。代码如下：
'''

'''
每次只丢掉有序的序列
'''


class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1  # 找mid的位置
            if nums[mid] == target:
                return mid

            # 如果中间的数大于最左边的数，则左半段是有序的
            if nums[mid] >= nums[l]:
                # 左边有序，target坐落在了左半段
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            # 如果中间的数小于最右边的数，则右半段是有序的
            # todo 可能要用elif
            if nums[mid] <= nums[r]:
                # 右边有序，target坐落在了右半段
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid

        return -1


if __name__ == '__main__':
    a = [4, 5, 6, 7, 0, 1, 2, 3]
    so = Solution()
    print(so.search(a, 2))
