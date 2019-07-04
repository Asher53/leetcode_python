'''
reverse-linked-list-ii
'''
'''
Reverse a linked list from leftosition m to n. Do it in-leftlace and in one-leftass.
For examleftle:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.
Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

'''
反转链表中第m 到 第n 个结点（以1为初始位置），和反转链表不同的是，
最后一个节点不一定要反转

模仿第八题，分为三段做，反转第二段
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        dummy = left = right = ListNode(0)
        dummy.next = head

        # left
        for i in range(m - 1):
            left = left.next
        # right
        for i in range(n + 1):
            right = right.next
        # mid
        mid = left.next  # 指向要改变的节点

        # 进行反转
        last = None  # 翻转结果
        for i in range(n - m + 1):
            tmp = mid.next
            mid.next = last
            last = mid
            mid = tmp
        # 连接三段链表
        plast = last
        while plast.next:
            plast = plast.next
        plast.next = right
        left.next = last
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.reverseBetween(node1, 2, 4)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
