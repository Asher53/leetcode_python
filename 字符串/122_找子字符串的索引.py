'''
implement-strstr
'''
'''
Implement strStr().
Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
'''


# class Solution:
#     def strStr(self, haystack, needle):
#         return haystack.find(needle)

# 或者暴力法
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    so = Solution()
    a, b = 'abced', 'ce'
    print(so.strStr(a, b))
