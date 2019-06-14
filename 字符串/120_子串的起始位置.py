'''
substring-with-concatenation-of-all-words
'''
'''
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of 
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
For example, given:
S:"barfoothefoobarman"
L:["foo", "bar"]
You should return the indices:[0,9].
(order does not matter).
'''

'''
输入一个字符串s和一连串的长度相同的字符串数组words，找出仅由所有的words组成的s的子字符串起始位置。
'''

'''
这个题目看着很复杂，其实不难，可以用滑动窗口的方法解决，先把 words中的所有单词进行放到一个字典中，然后扫描字符串s，
一个窗口一个窗口的统计分析，把符合的小窗口的起始位置保存结果变量里，即可。
'''


class Solution:
    def findSubstring(self, s, words):
        if not words:
            return []
        wordsDict = {}  # {'foo': 1, 'bar': 1}
        for word in words:  # 统计每个单词出现的个数
            wordsDict[word] = wordsDict.get(word, 0) + 1

        n, m, k = len(s), len(words[0]), len(words)  # n, m, k 分别表示，字符串的长度，单词的长度，单词的个数
        # print(n, m, k)
        res = []

        for i in range(n - m * k + 1):  # 选择一个区间或者窗口 11
            j = 0
            cur_dict = {}

            while j < k:
                word = s[i + m * j:i + m * j + m]  # 区间内选择一个单词
                print(word)

                if word not in wordsDict:  # 出现不存在的单词，直接结束本此区间
                    break

                cur_dict[word] = cur_dict.get(word, 0) + 1

                if cur_dict[word] > wordsDict[word]:  # 某个单词大于所需，则直接结束本此区间
                    break
                j += 1  # 单词数加一

            if j == k:
                res.append(i)  # 记录起始位置

        return res


if __name__ == '__main__':
    solu = Solution()
    s, words = 'barfoothefoobarman', ['foo', 'bar']
    print(solu.findSubstring(s, words))
