'''
maximum-subarray
'''
'''
在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
'''

'''
附加1
思路：
最大和连续子数组一定有如下几个特点：
1、第一个不为负数
2、如果前面数的累加值加上当前数后的值会比当前数小，说明累计值对整体和是有害的；
如果前面数的累加值加上当前数后的值比当前数大或者等于，则说明累计值对整体和是有益的。
步骤：
1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
2、判断累加值是否大于最大值：如果大于最大值，则最大和更新；否则，继续保留之前的最大和
'''


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum = 0
        pre_sum = 0
        for i in array:
            if pre_sum < 0:
                pre_sum = i
            else:
                pre_sum += i
            if pre_sum > max_sum:
                max_sum = pre_sum
        return max_sum


if __name__ == '__main__':
    n = [6, -3, -2, 7, -15, 1, 2, 2]
    n = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    so = Solution()
    print(so.FindGreatestSumOfSubArray(n))
