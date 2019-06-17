'''
max-points-on-a-line
'''
'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''

'''
给定n个2维平面上的点，找到在同一直线上最多的点数。
'''

'''
题目类型：哈希统计
这道题比较容易陷入一种思维定势。也就是，大家中学里都学过A，B，C三点共线的判断方法，即判断AB和BC的斜率相等。那么就每次选出两个点，
然后去遍历其他点，看是否与这两个点共线，最后找出共线最多的点数。这个算法的时间复杂度是O(n^3)。从时间复杂度上来看，应该还有其它更好
的方法。更好的方法也就是，每次只挑出一个点，然后遍历其他点，计算与该点形成的斜率，然后统计到相应的map（字典）中，这样复杂度就降低到
了O(n^2)，因为Python的字典是用Hash表实现，所以理想情况下可以看成插入和查找的时间复杂度为O(1)。
'''
'''
但是需要特别注意两种特殊点：
与当前考察点重合。这类点可以算入到任何其它斜率的直线上。如A点和B点形成30度斜率，C点和A点重合，那么30度斜率直线上至少就有A，B，C三个点。
与当前考察点垂直。因为这种情况斜率无穷大，dx分母为0，不能进行计算斜率的除法操作，因此要单独计数。
'''

'''
[(0,0),(1,1),(1,-1)] 对应输出应该为:2
[(0,0),(0,0)] 对应输出应该为:2
[(0,0),(-1,-1),(2,2)] 对应输出应该为:3
'''


# 公式 k = (y2-y1) / (x2-x1)    (x1!=x2)
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        len_points = len(points)
        if len_points <= 2:
            return len_points
        max_count = 0
        for index1 in range(len_points):
            p1 = points[index1]
            gradients = {}
            infinite_count = 0
            duplicate_count = 0
            for index2 in range(index1, len_points):
                p2 = points[index2]
                # k = (y2-y1) / (x2-x1)    (x1!=x2)
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                # 重合点
                if dx == 0 and dy == 0:
                    duplicate_count += 1
                # todo dx==0,无论是否重合，都算作斜率不存在
                if dx == 0:
                    infinite_count += 1
                else:
                    g = float(dy) / dx  # take care
                    # seem like cannot do gradients[g] += 1 if key: g not exists
                    gradients[g] = gradients.get(g, 0) + 1
            if infinite_count > max_count:
                max_count = infinite_count

            for v in list(gradients.values()):
                v += duplicate_count
                if v > max_count:
                    max_count = v
        return max_count


if __name__ == '__main__':
    a = Point(0, 0)
    b = Point(-1, -1)
    c = Point(3, 5)
    d = Point(3, 6)
    e = Point(3, 7)
    l = [a, b, c, d, e]

    # a = Point(0, 0)
    # b = Point(1, 1)
    # c = Point(1, -1)
    # l = [a, b, c]

    # a = Point(0, 0)
    # b = Point(0, 0)
    # l = [a, b]

    so = Solution()
    print(so.maxPoints(l))
