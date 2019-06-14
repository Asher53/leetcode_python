'''
length-of-last-word
'''
'''
Given a string s consists of upper/lower-case alphabets and empty space characters' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
For example,
Given s ="Hello World",
return5.
'''


class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split()) - 1]) if s.split() != [] else 0


if __name__ == '__main__':
    so = Solution()
    s = "Hello World"
    print(so.lengthOfLastWord(s))
