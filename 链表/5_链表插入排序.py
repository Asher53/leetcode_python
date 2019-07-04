'''
insertion-sort-list
'''
'''
Sort a linked list using insertion sort.
'''

'''
dummy是结果指针
p2其实指向的是已排序最大的数
p1为了不改变dummy而设
保证: 
dummy.next = head
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        # dummy是结果，dummy初始化为链表
        dummy = ListNode(0)
        dummy.next = head
        # 位置指针
        p2 = head
        while p2.next:  # 待插入节点是p2.next
            # 只有在值小于左边的邻结点才插入
            if p2.next.val < p2.val:
                p1 = dummy   # 暂存结果的指针
                while p1.next.val <= p2.next.val:  # 前面和后面的比较
                    p1 = p1.next
                t = p2.next  # 也是 p2.next
                p2.next = p2.next.next  # 此步与if语句对应
                t.next = p1.next
                p1.next = t
            else:
                p2 = p2.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(8)
    node2 = ListNode(10)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(7)
    node5 = ListNode(9)
    node6 = ListNode(1)

    node3.next = node4
    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.insertionSortList(node1)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
