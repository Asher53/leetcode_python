'''
longest-common-prefix
'''
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:
所有输入只包含小写字母 a-z 。
"""

"""
第一字符串当做基准，用一个指针来表示在此之前的字符是满足题目要求的。
遍历每一个字符串，用指针对应的字符与基准中相应的字符比较.
后面的字符串可能没有第一个字符串长，如果指针超过了最短的字符串也应该终止。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        # 第一字符串当做基准
        for i in range(len(strs[0])):
            # 遍历每一个字符串
            for str in strs:
                # print(str)
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    so = Solution()
    numbers = ["flower", "flow", "flight"]
    # numbers = ["dog", "racecar", "car"]
    print(so.longestCommonPrefix(numbers))
