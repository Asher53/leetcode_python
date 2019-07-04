'''
copy-list-with-random-pointer
'''
'''
A linked list is given such that each node contains an additional random pointer which could point to any node
in the list or null. Return a deep copy of the list.
'''

'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
'''

'''
算法包含下面三个步骤(题)：
1. 复制每一个节点，将新节点插入原节点之后
2.  设置random指针, tmp.next.random = tmp.random.next
3. 分开链表(新旧指针指向该指向的位置)
'''


class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, head):
        if not head:
            return
        # 在原链表的每个节点后都插入一个新节点，新节点的内容和前面的节点一样
        # tmp用来移动
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.val)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next  # 每次跳两格

        # 遍历新链表，为其中的新增节点设置random指针
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        # 分成新旧两个链表，先移动pold，再根据pold设置pnew
        pold = head
        pnew = newhead = head.next  # 暂存pnew
        while pnew.next:
            pold.next = pold.next.next  # 断链
            pold = pold.next  # 移位
            pnew.next = pold.next  # 加入
            pnew = pnew.next  # 移位
        return newhead


if __name__ == '__main__':
    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = node3
    node4.random = node2

    so = Solution()
    print(so.Clone(node1).random.val)
    print(so.Clone(node1).next.next.next.random.val)
