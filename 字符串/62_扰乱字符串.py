'''
scramble-string
'''
'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 ="great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node"gr"and swap its two children, it produces a scrambled string"rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that"rgeat"is a scrambled string of"great".

Similarly, if we continue to swap the children of nodes"eat"and"at", it produces a scrambled string"rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that"rgtae"is a scrambled string of"great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''

'''
那打乱这个过程是怎么做的呢，很简单，给你一个字符串，你必须先找一个点把它砍成两半，你可以通过交换这两半的顺序来打乱源字符串的顺序，
那想一下，怎么知道打断的那个点在哪呢？穷举。怎么知道打断之后有没有做交换操作呢？两种情况递归，有一条走的通就可以了。
'''


class Solution(object):
    def isScramble(self, s1, s2):
        # 完全一样
        if s1 == s2:
            return True
        # 不一样
        if sorted(s1) != sorted(s2):
            return False
        '''
        当s1='ab', s2只有'ab'或者'ba'才可以。 
        '''
        length = len(s1)
        for i in range(1, length):
            # ab
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # ba
            if self.isScramble(s1[:i], s2[length - i:]) and self.isScramble(s1[i:], s2[:length - i]):
                # print(s1[:i], s2[length - i:], self.isScramble(s1[i:], s2[:length - i]))
                return True
        return False


if __name__ == '__main__':
    s1 = 'great'
    s2 = 'eatrg'

    # s1 = 'ab'
    # s2 = 'ba'
    so = Solution()
    print(so.isScramble(s1, s2))
