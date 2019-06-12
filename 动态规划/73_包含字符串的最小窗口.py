'''
minimum-window-substring
'''
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S ="ADOBECODEBANC"
T ="ABC"

Minimum window is"BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string"".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

'''
在S中找出包含T的全部字符的最小子串。
'''

'''
这道题的思路是： 
题目提示已经给了很多，hash、双指针、滑动窗口。很明显就是用滑动窗口方法。
（1）采用滑动窗口的方法，可以用hash记录字符串T中的各个字符出现的次数，方便后面计算。
（2）在S串中，从左向右滑动，用(i, j)记录在S串的第一个符合的窗口，并更新记录到(m, n)中。
（3）现在开始，向右滑动窗口，依次扩展（右边界），并判断左边界，是否可以收缩（左边是否可以向右移动）。
（4）在滑动的过程中，当前窗口如果满足条件，要及时更新最小的窗口。
'''


class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        count = Counter(t)  # 统计字符串 t 中字符出现的次数 Counter({'A': 1, 'B': 1, 'C': 1})

        miss = len(t)  # miss 负责记录 当前窗口是否满足条件
        i = m = n = 0
        # enumerate j是下标，v是变量
        for j, v in enumerate(s, 1):  # 向右滑动或扩展   enumerate(s, 1)下标从1开始给
            # 先维护t
            miss -= (count[v] > 0)  # 判断式会转化为(0,1),找到第一个包含T中的字符以后就恒为零
            # print(j, v, miss)
            count[v] -= 1  # 没有出现的字符也会减1,正好可以记录边界情况
            # print(count)
            # 包含了所有t的字符以后，开始收缩
            if not miss:  # 当前窗口满足条件
                # print(count)
                while i < j and count[s[i]] < 0:  # 左边界收缩
                    count[s[i]] += 1
                    i += 1
                if not n or j - i <= n - m:  # 更新新的窗口
                    n, m = j, i
        return s[m:n]


if __name__ == '__main__':
    s = "ADOBECODEBANCO"
    t = "ABC"
    so = Solution()
    print(so.minWindow(s, t))
