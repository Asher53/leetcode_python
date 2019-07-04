'''
linked-list-cycle-ii
'''
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Follow up:
Can you solve it without using extra space?
'''

'''
1）同linked-list-cycle-i一题，使用快慢指针方法，判定是否存在环，并记录两指针相遇位置(Z)；
2）将两指针分别放在链表头(X)和相遇位置(Z)，并改为相同速度推进，则两指在环开针始位置相遇(Y)。

证明如下：
如下图所示，X,Y,Z分别为链表起始位置，环开始位置和两指针相遇位置，则根据快指针速度为慢指针速度的两倍，可以得出：
2*(a + b) = a + b + n * (b + c)；即
a=(n - 1) * b + n * c = (n - 1)(b + c) +c;
注意到b+c恰好为环的长度，故可以推出，如将此时两指针分别放在起始位置和相遇位置，并以相同速度前进，当一个指针走完距离a时，
另一个指针恰好走出 绕环n-1圈加上c的距离。故两指针会在环开始位置相遇。
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
                slow = pHead
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return False


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2
    so = Solution()
    print(so.EntryNodeOfLoop(node1).val)
    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    #
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # so = Solution()
    # print(so.EntryNodeOfLoop(node1))
