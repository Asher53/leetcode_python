'''
best-time-to-buy-and-sell-stock-iii
'''
'''
Say you have an array for which the i th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

'''
123是由121演变而来的，原来是只能有一次，现在是可以有两次，这里有要求是说你不能买一次再买一次然后卖出去两次，只能买卖买卖。
'''


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        # pre_profit[i]表示i天之前的最大利润
        pre_max_profit = [0] * n
        # pro_profit[i]表示i天之后的最大利润
        pro_max_profit = [0] * n
        max_profit = 0

        low = prices[0]
        for i in range(1, n):
            low = min(prices[i], low)
            pre_max_profit[i] = max(pre_max_profit[i - 1], prices[i] - low)

        print(pre_max_profit)

        high = prices[n - 1]
        for k in range(n - 2, -1, -1):
            high = max(high, prices[k])
            pro_max_profit[k] = max(pro_max_profit[k + 1], high - prices[k])

        print(pro_max_profit)

        for j in range(n):
            max_profit = max(max_profit, pre_max_profit[j] + pro_max_profit[j])
        return max_profit


if __name__ == '__main__':
    a = [2, 3, 1, 2, 6, 5]
    so = Solution()
    print(so.maxProfit(a))
