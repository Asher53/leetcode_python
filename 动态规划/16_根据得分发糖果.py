'''
candy
'''
'''
多个小朋友站成一排，根据他们的得分分发糖果，得分高的小朋友要比旁边得分低的小朋友得到的糖果多，每个小朋友至少得到一枚糖果，问最少要准备多少糖果？
'''

'''
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
'''

'''
进行两次扫描，一次从左往右，一次从右往左。第一次扫描的时候维护对于每一个小孩左边所需要最少的糖果数量，存入数组对应元素中，
第二次扫描的时候维护右边所需的最少糖果数，并且比较将左边和右边大的糖果数量存入结果数组对应元素中。
这样两遍扫描之后就可以得到每一个所需要的最最少糖果量，从而累加得出结果。
方法只需要两次扫描，所以时间复杂度是(O(2*n)=On)。空间上需要一个长度为n的数组，复杂度是O(n)。代码如下： 
'''


class Solution:
    def candy(self, ratings):
        n = len(ratings)
        result = [1] * n  # 空间复杂度O(n)

        # 从前面开始升序遍历，所有升序的从1开始给
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        # 从后面开始升序遍历，所有升序的就从1开始给
        for j in range(n - 2, -1, -1):  # 细节，n-2开始, 步长-1
            if ratings[j] > ratings[j + 1]:
                # max 保证两边都是最大
                result[j] = max(result[j], result[j + 1] + 1)
        if ratings[n - 1] >= ratings[0]:
            result[n - 1] = max(result[n-1], result[0] + 1)
        print(result)
        return sum(result)


if __name__ == '__main__':
    # a = [1, 2, 11, 7, 10]
    # a = [1, 2, 5, 5, 10]
    a = [1, 1, 2]
    # a = [1, 2, 3, 3]
    so = Solution()
    print(so.candy(a))
