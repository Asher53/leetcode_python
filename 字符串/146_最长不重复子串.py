'''
longest-substring-without-repeating-characters
'''
'''
Given a string, find the length of the longest substring without repeating characters. For example,
the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
'''

'''
题目是要求出最长的不重复子字符串的长度。比如字符串abcabcbb，得到的最长无重复子字符串就是abc，
bca或者cab，那么它最长的不重复长度就是3.
'''

'''
使用一个哈希表，记录字符的索引。例如对于字符串'zzwxyabcabcbb'，当检测到第二个'a'时，由于之前已经有一个'a'了，
所以应该从第一个a的下一个字符重新开始测算长度，但是要把第一个a之前的字符在哈希表中对应的值清掉，如果不清掉的话，
就会误以为还存在重复的。比如检测到第二个'z'时，如果第一个'z'对应的哈希值还在，那就出错了，所以要把第一个'a'之前的字符的哈希值都重置才行。
'''

'''
ord()函数是chr()或unichr()的配对函数，以字符作为参数，返回ASCII数值，或者Unicode数值。
>>>ord('a')
97
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        maxlen = 0
        dic = {}
        n = len(s)
        # {'a': -1, 'b': -1, 'c': -1}
        for i in range(n):
            dic[s[i]] = -1

        for i in range(n):
            if dic[s[i]] != -1:
                # 把第一个之前的都重置
                while start <= dic[s[i]]:
                    # print(start)
                    dic[s[start]] = -1
                    # print(dic)
                    start += 1
            if i - start + 1 > maxlen:
                maxlen = i - start + 1
            dic[s[i]] = i
            # print(dic)
        return maxlen


if __name__ == '__main__':
    so = Solution()
    numbers = 'abcabcbb'
    print(so.lengthOfLongestSubstring(numbers))
