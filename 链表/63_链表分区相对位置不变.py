'''
partition-list
'''
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal 
to x. You should preserve the original relative order of the nodes in each of the two partitions.
For example,
Given1->4->3->2->5->2and x = 3,
return1->2->2->4->3->5.
'''

'''
比较无脑
创建两个头结点head1和head2，
head1这条链表是小于x值的节点的链表，head2链表是大于 等于 x值的节点的链表，然后将head2链表链接到head链表的尾部即可。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
只要管小于的数，后面的相对位置才能不变
'''


class Solution:
    def partition(self, head, x):
        phead1 = head1 = ListNode(0)
        phead2 = head2 = ListNode(0)
        tmp = head
        while tmp:
            if tmp.val < x:
                phead1.next = tmp
                tmp = tmp.next
                phead1 = phead1.next
                phead1.next = None  # 注意设为None
            else:
                phead2.next = tmp
                tmp = tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.partition(node1, 3)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
