# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 题意：大的数字如253，用一位位的数字存储表示，逆序就是从个位开始的 253-->[3,5,2]
from typing import Optional


class ListNode:
    '''
    单链表每个数据元素占用若干存储单元的组合称为一个「链节点」，
    还要存放一个指出这个数据元素在逻辑关系上的直接后继元素所在链节点的地址，该地址被称为「后继指针 next」
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 根据 data 初始化一个新链表
def create(data):
    head = ListNode(0)
    cur = head
    for i in range(len(data)):
        node = ListNode(data[i])
        cur.next = node
        cur = cur.next
    head = head.next
    return head


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化链表
        head = tree = ListNode()

        val = tmp = 0
        # 当三者有一个不为空时继续循环
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next

            tmp = val // 10
            val = val % 10

            # 实现链表的连接
            tree.next = ListNode(val)
            tree = tree.next

        return head.next  # 因为头节点是初始化的，为0，所以返回的链表应该是头结点的下一个


solve = Solution()
a = create([2, 3, 4])
b = create([1, 2])
print(solve.addTwoNumbers(a, b).val)


class Solution:
    def addtwolistnode(self, l1:Optional[ListNode], l2:Optional[ListNode]):
        # 头结点，初始化链表
        head = tree = ListNode()  # 其实就是定义一个单链表，然后后面的链表都接在后面
        val = tem = 0   # val存储每一位相加后的值，tem存储进位那些
        while tem or l1 or l2:
            val = tem
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            tem = val // 10
            val = val % 10
            tree.next = ListNode(val)
            tree = tree.next
        return head.next
