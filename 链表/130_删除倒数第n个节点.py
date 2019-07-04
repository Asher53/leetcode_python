'''
remove-nth-node-from-end-of-list
'''

'''
Given a linked list, remove the n th node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

'''
技巧题：找倒数节点的方法
'''

'''
这道题的含义是删除链表的倒数第n个节点。
解题思路：加一个头结点dummy，并使用双指针p1和p2。p1先向前移动n个节点，然后p1和p2同时移动，当p1.next==None(走到最后一个时)，
此时p2.next指的就是需要删除的节点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        p1 = p2 = dummy = ListNode(0)
        dummy.next = head
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        print(p2.val)
        p2.next = p2.next.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    so = Solution()
    res = so.removeNthFromEnd(node1, 2)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
