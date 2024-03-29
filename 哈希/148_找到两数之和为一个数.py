'''
two-sum
'''

'''
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
用hash(存储元素及对应位置)，一定会找到配对的这一个
'''


class Solution:
    def twoSum(self, num, target):
        dic = dict()
        for i in range(len(num)):
            x = num[i]
            if target - x in dic:
                return dic[target - x] + 1, i + 1
            dic[x] = i  # 存储位置
            # print(dic)


if __name__ == '__main__':
    so = Solution()
    numbers = [2, 11, 7, 15]
    target = 9
    print(so.twoSum(numbers, target))
