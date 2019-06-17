'''
longest-consecutive-sequence
'''

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example,
Given[100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is[1, 2, 3, 4]. Return its length:4.
Your algorithm should run in O(n) complexity.
'''

'''
解题思路：使用一个哈希表，在Python中是字典dict数据类型。dic中的映射关系是{x in num：False}，这个表示num中的x元素没有被访问过，
如果被访问过，则为True。如果x没有被访问过，检查x+1，x+2...，x-1，x-2是否在dict中，如果在dict中，就可以计数。最后可以求得最大长度。
'''


# 散列表 = 哈希表
class Solution:
    def longestConsecutive(self, num):
        longgest = 0
        # todo 最后连续的数的入口为False
        hash_table = {i: False for i in num}  # todo : 优雅的字典初始化
        # print(hash_table)
        for i in hash_table:
            if hash_table[i] == False:
                len_right = 0
                v = i + 1
                while v in hash_table:
                    len_right += 1
                    hash_table[v] = True
                    v += 1
                len_left = 0
                v = i - 1
                while v in hash_table:
                    len_left += 1
                    hash_table[v] = True
                    v -= 1
                longgest = max(len_left + len_right + 1, longgest)
        return longgest


if __name__ == '__main__':
    a = [100, 2, 200, 1, 3, 4, 101]
    so = Solution()
    print(so.longestConsecutive(a))
