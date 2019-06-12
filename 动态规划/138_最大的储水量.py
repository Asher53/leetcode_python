'''
container-with-most-water
'''
'''
Given n non-negative integers a1 , a2 , ..., an , where each represents a point at coordinate (i, ai ).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai ) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.
'''

'''
给出一个n长度的非0数组，a1,a2,……,an，ai代表在坐标i上的高度为ai。以以ai，aj为高，i到j为底，可以构造出一个容器。
那么求出这些容器中可以装的水的最大容积（容器不能倾斜）。例如数组[2,1]，一共可以构造1个容器，
这个容器的四个端点坐标是（0，0），（0，2），（1，1），（1，1），那么他可以装的最大的水容积是（1-0）*1 = 1.
'''

'''
我们认真研究一下寻找过程，我们从第一个高度为起始容器壁，那么我们直接以最后一个高度为终止壁，如果a1 <= an，
那么以a1为起始的容器最大是a1 * （n - 1），以a1为容器壁的最大容器计算出来的。那么以a1为壁的所有情况不需要再考虑，
接着考虑a2的；同理，如果a1 > an,an不再考虑，考虑an-1，这有点类似"夹逼定理"。比较ai和aj（i<j）如果ai <= aj，
i++；否者j ++直到i == j。这个算法的时间复杂度是（O（n））。
'''

class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [2, 1]
    print(s.maxArea(nums))
