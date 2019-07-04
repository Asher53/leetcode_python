'''
remove-duplicates-from-sorted-list
'''
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given1->1->2, return1->2.
Given1->1->2->3->3, return1->2->3.
'''

'''
节点去重
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next  # todo 去掉节点
            else:
                p = p.next
        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    so = Solution()
    res = so.deleteDuplicates(node1)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
