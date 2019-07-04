'''
reorder-list
'''
'''
Given a singly linked list L: L 0→L 1→…→L n-1→L n,
reorder it to: L 0→L n →L 1→L n-1→L 2→L n-2→…

You must do this in-place without altering the nodes' values.
不能定义新节点, 所以不能定义dummy
For example,
Given{1,2,3,4}, reorder it to{1,4,2,3}.
'''
'''
相当于三个题:
1 快慢指针找到中点
2 反转链表 right
3 合并链表
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        # 第一步: 快慢指针找到中点
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None

        # 第二步: 反转right链表 todo 可单独作为一道题
        last = None  # 翻转结果
        while right:  # 拿出当前结点，加到last的前面，再改变last
            temp = right.next
            right.next = last
            last = right
            right = temp

        # 第三步：合并
        p1 = left  # [1,2,3]
        p2 = last  # [5,4]

        p = dummy = ListNode(0)
        while p1 and p2:
            p.next = p1
            p1 = p1.next
            p = p.next
            p.next = p2
            p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    so = Solution()
    res = so.reorderList(node1)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
