'''
reverse-nodes-in-k-group
'''

'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

'''
恰好可以利用栈来完成这段分组反转的操作
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        previous = dummy = ListNode(0)
        node = dummy.next = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
            if len(stack) == k:
                while len(stack):
                    pop_node = stack.pop()
                    previous.next = pop_node
                    previous = previous.next

        # 只需等于stack[0]，因为stack[0]包含了后面的信息
        # 一定要把最后置为None
        previous.next = stack[0] if len(stack) else None
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    # node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6

    so = Solution()
    res = so.reverseKGroup(node1, 3)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
