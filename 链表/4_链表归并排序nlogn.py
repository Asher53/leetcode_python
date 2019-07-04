'''
sort-list
'''
'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序
一共有logn层，故复杂度是 O(nlogn)
因为题目要求复杂度为O(nlogn),故可以考虑归并排序的思想。
归并排序的一般步骤为：
1）将待排序数组（链表）取中点并一分为二；
2）递归地对左半部分进行归并排序；
3）递归地对右半部分进行归并排序；
4）将两个半部分进行合并（merge）,得到结果。

所以对应此题目，可以划分为三个小问题：
1）找到链表中点
2）写出merge函数，即如何合并链表。
3）写出mergesort函数，实现上述步骤。
测试用例:
{2,1} 对应输出应该为: {1,2}
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, left, right):
        p = Point = ListNode(0)
        while left and right:
            if left.val <= right.val:
                Point.next = left
                left = left.next
                Point = Point.next  # 不要忘了移动Point
            else:
                Point.next = right
                right = right.next
                Point = Point.next
        Point.next = left or right
        return p.next

    def MergeSort(self, head):
        # 注意终止条件
        if not head or not head.next:
            return head

        # 找到中点
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None  # todo 必须断开链表
        print(left.val, right.val)

        # 分到底层再排序
        left = self.MergeSort(left)
        right = self.MergeSort(right)
        return self.Merge(left, right)


if __name__ == '__main__':
    node1 = ListNode(6)
    node2 = ListNode(4)
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
    res = so.MergeSort(node1)
    l = []
    while res:
        l.append(res.val)
        res = res.next
    print(l)
