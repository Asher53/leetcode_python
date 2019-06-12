'''
多个小朋友站成一圈(第一个和第n个相连)，根据他们的得分分发糖果，得分高的小朋友要比旁边得分低的小朋友得到的糖果多，每个小朋友至少得到一枚糖果，
问最少要准备多少糖果？
'''

class Solution:
    def candy(self, values, a):
        # 开环
        ratings = values + values
        n = 2 * a
        res = n * [1]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i-1] + 1
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                res[j] = max(res[j+1] + 1, res[j])
        for i in range(a):
            res[i] = max(res[i], res[i+a])
        res = res[:a]
        return sum(res)

if __name__ == '__main__':
    # a = [1, 2, 5, 7, 10]
    # a = [1, 2, 5, 5, 10]
    # a = [1, 2]
    a = [1, 2, 3, 3]
    so = Solution()
    print(so.candy(a, len(a)))