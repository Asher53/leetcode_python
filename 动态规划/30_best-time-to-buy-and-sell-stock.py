'''
best-time-to-buy-and-sell-stock
'''
'''
Say you have an array for which the i th element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
'''

'''
假设你有一个数组，里面存放的第i个元素表示第i天的股票的价格，如果你最多只允许进行一次交易（买进和卖出股票视为一次交易）
请设计一个算法得到最大利润。
'''

'''
思路：假设第i天卖出股票能得到最大利润，第i天价格为prices[i],那么买进股票应该是在第0~i天的价格是最小值的情况下，才有最大利润。
遍历一遍就能找到所有第i天卖出股票获得利润中的最大值。
'''


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        low = prices[0]
        maxprofit = 0
        #  找到第0~i天买进股票最小花费的price
        for i in prices:
            low = min(i, low)
            # 那么prices[i] - min_buy就是第i天卖出得到的最大利润，再和之前的做比较，求所有中的最大值
            maxprofit = max(maxprofit, i - low)
            # print(maxprofit)
        return maxprofit


if __name__ == '__main__':
    a = [2, 3, 1, 2, 6, 5]
    so = Solution()
    print(so.maxProfit(a))
