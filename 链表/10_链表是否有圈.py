'''
linked-list-cycle
'''
'''
Given a linked list, determine if it has a cycle in it.
Follow up:
Can you solve it without using extra space?
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        slow = fast = pHead
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node2
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
    print(so.EntryNodeOfLoop(node1))

