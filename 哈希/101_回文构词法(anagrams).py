'''
Anagrams
'''

'''
Given an array of strings, return all groups of strings that are anagrams.
Note: All inputs will be in lower-case.
'''

'''
首先简单介绍一下Anagram（回文构词法）。Anagrams是指由颠倒字母顺序组成的单词，比如“dormitory”颠倒字母顺序会变成“dirty room”，
“tea”会变成“eat”。回文构词法有一个特点：单词里的字母的种类和数目没有改变，只是改变了字母的排列顺序。
For example:
Input:　　["tea","and","ate","eat","den"]
Output:   ["tea","ate","eat"]
'''

'''
解题思路：anagram的意思是：abc，bac，acb就是anagram。即同一段字符串的字母的不同排序。
将这些都找出来。这里使用了哈希表，即Python中的dict。针对前面的例子来讲，映射为{abc：abc，bac，acb}。
'''


# class Solution:
#     def anagrams(self, strs):
#         dictionary = {}
#         for word in strs:
#             sortedword = ''.join(sorted(word))
#             print(sortedword)
#             # print(sortedword)  # 每次为排序后的字符串
#             dictionary[sortedword] = [word] if sortedword not in dictionary else dictionary[sortedword] + [word]
#             # print(dictionary)
#         res = []
#         print(dictionary)
#         # 遍历字典
#         for item in dictionary:
#             if len(dictionary[item]) >= 2:
#                 res += dictionary[item]
#         return res

class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        print(dict)
        result = []
        for item in dict:
            result.append(dict[item])
        return result


if __name__ == '__main__':
    # s = ['tea', 'and', 'ate', 'eat', 'den', 'adn']
    s = ["tea", "and", "ate", "eat", "den"]
    so = Solution()
    print(so.groupAnagrams(s))
