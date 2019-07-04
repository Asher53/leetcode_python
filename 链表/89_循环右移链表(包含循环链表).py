'''
rotate-list
'''

'''
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given1->2->3->4->5->NULL and k =2,
return4->5->1->2->3->NULL.
'''

'''
解题思路：循环右移一条链表，比如k=2，（1，2，3，4，5）循环右移两位变为（4，5，1，2，3）。
由于k值有可能比链表长度大很多，所以先要用一个count变量求出链表的长度。而k%count就是循环右移的步数。
不需反转，只要找准位置
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not k:
            return head
        if not head:
            return head

        p = dummy = ListNode(0)
        dummy.next = head

        count = 0
        # 统计链表长度
        # 此时p是最后一个数5，p.next指向null
        while p.next:
            p = p.next
            count += 1
        # 步数
        step = count - (k % count)

        # todo 实际上变成了一个循环链表
        #  p.next指向第一个数,这样p就是0,1,2,3,4,5,1,2,3,4,5
        p.next = dummy.next

        # 此时p是最后一个未翻转的数3
        for i in range(step):
            p = p.next

        # todo 将其下一个数4，放到head节点,此时head是4,5,1,2,3,4,5,1,2,3,4,5
        head = p.next
        # print(head.next.next.val)
        p.next = None  # 断链
        return head


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
    res = so.rotateRight(node1, 2)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
