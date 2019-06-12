'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costscost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can
travel around the circuit once, otherwise return -1.
Note:
The solution is guaranteed to be unique.
'''

'''
在一个圆形路径上有N个加油站，在位置 i 上的汽油的数目为gas[i]；
你有一个汽车，这个汽车的油箱是无限容量的，它从加油站 i 到 加油站 （i+1）需要耗费的汽油数为cost[i]，开始这段旅程的时候，
你的起始状态是在加油站中的一个，油箱为空的.
若一次性完成整个的圆形路途，返回你的其实加油站的序号，若不能完成整个路途，返回-1.
注意：
解决方案保证是唯一的.
'''

'''
解题思路：
贪心算法（Greedy Algorithm)
分析题目可以得到两个隐含的结论：
结论1：若从加油站A出发，恰好无法到达加油站C（只能到达C的前一站）。则A与C之间的任何一个加油站B均无法到达C。

假设从加油站A出发恰好无法到达加油站C，但是A与C之间存在加油站B，从B出发可以到达C。
而又因为从A出发可以到达B，所以A到B的油量收益（储油量 - 耗油量）为正值，进而可以到达C。
推出矛盾，假设不成立。

结论2：若储油量总和sum(gas) >= 耗油量总和sum(cost)，则问题一定有解。
'''

'''
这道转圈加油问题不算很难，只要想通其中的原理就很简单。我们首先要知道能走完整个环的前提是gas的总量要大于cost的总量，这样才会有起点的存在。
假设开始设置起点start = 0, 并从这里出发，如果当前的gas值大于cost值，就可以继续前进，此时到下一个站点，
剩余的gas加上当前的gas再减去cost，看是否大于0，若大于0，则继续前进。当到达某一站点时，若这个值小于0了，
则说明从起点到这个点中间的任何一个点都不能作为起点，则把起点设为下一个点，继续遍历。当遍历完整个环时，当前保存的起点即为所求。
'''


class Solution:
    def canCompleteCircuit(self, gas, cost):
        # 走完整个环的前提是gas的总量要大于cost的总量，这样才会有起点的存在
        if sum(gas) < sum(cost):
            return -1
        # 先假设0为起点
        start = sums = 0
        for i in range(len(gas)):
            sums += gas[i] - cost[i]
            # 如果一个点的sum为负，则将起点设为它的下一个，sum归0
            if sums < 0:
                start, sums = i + 1, 0
        return start


if __name__ == '__main__':
    # a = [1, 2]   # 输出1
    # b = [2, 1]

    a = [1, 2, 3, 4, 5, 6]
    b = [2, 1, 4, 6, 3, 5]

    # a = [5]   # 输出0
    # b = [4]

    so = Solution()
    print(so.canCompleteCircuit(a, b))
