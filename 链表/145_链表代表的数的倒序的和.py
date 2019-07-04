'''
add-two-numbers
'''
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of
their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        add = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(add[0])
        answer = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer


if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.addTwoNumbers(node1, node4)

    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
