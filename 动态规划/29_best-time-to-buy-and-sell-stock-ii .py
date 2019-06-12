'''
best-time-to-buy-and-sell-stock-ii
'''
'''
Say you have an array for which the i th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you
like (ie, buy one and sell one share of the stock multiple times). However, you may not engage
in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

'''
题目大意
允许进行多次交易，即可以多次买入和卖出，但手中最多只能持有一支股票，在再次买入的时候必须将之前的股票卖出，求能获取的最大利润。

解题思路
贪心法，每次在递增序列就算入，一旦降价，就在上一个节点抛出，其实代码就是直接统计递增的序列
'''

'''
不限制买卖股票的次数，只要保证你卖的日期晚于买的日期即可。这个就适合用贪心算法，只要当前比前一天的大，那么我们就卖了股票。
'''


class Solution:
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                maxprofit += prices[i] - prices[i - 1]
        return maxprofit


if __name__ == '__main__':
    a = [2, 3, 1, 2, 6, 5]
    so = Solution()
    print(so.maxProfit(a))
