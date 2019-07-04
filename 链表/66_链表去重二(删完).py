'''
remove-duplicates-from-sorted-list-ii
'''
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
For example,
Given1->2->3->3->4->4->5, return1->2->5.
Given1->1->1->2->3, return2->3.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        tmp = dummy.next
        while p.next:
            # 相等的话一直移动到相等的最后一个
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            # 如果tmp没有发生移动，说明没有重复的
            if tmp == p.next:
                p = p.next
                tmp = p.next
            # 否则断开它们
            else:
                p.next = tmp.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    so = Solution()
    res = so.deleteDuplicates(node1)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
