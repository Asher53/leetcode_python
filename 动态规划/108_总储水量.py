'''
trapping-rain-water
'''
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it is able to trap after raining.
For example,
Given[0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

'''
将一个数列看成是一堆高低不一的蓄水墙，数值即这面墙的高度，求总的蓄水最大量。
'''

'''
解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开始遍历，
用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], rightmax)-A[i]就是在第i个bar可以储存的水量。
例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
'''

'''
例如，针对A=[0,1,0,2,1,0,1,3,2,1,2,1]这个例子，A[4]=1这一点，其左边出现过的最高墙是A[3]=2，其右边出现过的最高墙是A[7]=3，
因此两者中的最小者就就是A[3]=2，因此A[4]的蓄水高度就是A[3]-A[4]=1，乘以底边1，即A[4]蓄水量为1。
'''


class Solution:
    def trap(self, A):
        n = len(A)
        leftmosthigh = [0] * n
        leftmax = 0

        # leftmosthigh[i]为A[i]之前的最高的bar值
        for i in range(n):
            if A[i] > leftmax:
                leftmax = A[i]
            leftmosthigh[i] = leftmax
        # print(leftmosthigh) # [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]

        sum = 0
        rightmax = 0
        for i in reversed(range(n)):
            if A[i] > rightmax:
                rightmax = A[i]
            if min(rightmax, leftmosthigh[i]) > A[i]:
                sum += min(rightmax, leftmosthigh[i]) - A[i]
        return sum


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(nums))
