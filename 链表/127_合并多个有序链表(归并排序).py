'''
merge-k-sorted-lists
'''

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

'''
将k个已排好序的链表合并为一个非下降排序的链表。
'''

'''
参考归并排序的思路，对k个链表进行分组，最后两两归并，最终合成一个链表
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
下面这一段太垃圾，可以用合并两个有序链表
不对，合并两个可以那样，但这里要求的是k个
其实原理上就是两两合并
'''


class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if not n:
            return None
        if n == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[:n // 2])
        l2 = self.mergeKLists(lists[n // 2:])
        return self.Merge(l1, l2)

    def Merge(self, pHead1, pHead2):
        dummy = head = ListNode(0)  # 初始化res和head,两个指针，head用来移动，res始终指向头部,返回可以返回其的next

        while pHead1 and pHead2:  # 两个链表均有值时

            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
            else:
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
    node6 = ListNode(7)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(5)
    node8 = ListNode(6)
    node9 = ListNode(10)
    node7.next = node8
    node8.next = node9

    a = [node1, node7, node4]

    so = Solution()
    res = so.mergeKLists(a)
    l = list()
    while res:
        l.append(res.val)
        res = res.next
    print(l)
