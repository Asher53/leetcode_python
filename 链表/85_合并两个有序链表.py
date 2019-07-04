'''
merge-two-sorted-lists
'''

'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''



'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

'''
思路：
初始化res和head,两个指针，head用来移动，res始终指向head的头部
返回可以返回res的next
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        dummy = head = ListNode(0)  # 初始化res和head,两个指针，head用来移动，res始终指向头部,返回可以返回其的next

        while pHead1 and pHead2:  # 两个链表均有值时

            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next

            elif pHead1.val >= pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next

            head = head.next  # 每次head指针移位

        head.next = pHead1 or pHead2  # todo 如果有值的话

        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(9)
    node1.next = node2
    node2.next = node3



    node4 = ListNode(2)
    node5 = ListNode(3)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.Merge(node1,node4)
    l = list()
    while res:
        l.append(res.val)
        res = res.next
    print(l)