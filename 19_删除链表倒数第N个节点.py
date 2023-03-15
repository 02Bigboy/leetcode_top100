# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 这是链表的问题，先不做
        if not head or  n <1:
            return None
        fast = head
        slow = head
        for _  in range(n): # 先让快指针走n步
            if not fast:
                return None
            fast = fast.next
        if not fast: #当要删除的节点比链表还长的时候
            return head.next
        while  fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next #将要删除的节点的前一个节点的指针指向要删除的元素的下一个元素
        return head
    
class Solve:
    '''
    思路：定义两个指针，一个快指针，一个慢指针
    快指针先走n步，然后快慢指针再同步走，快指针走到头后，慢指针还有n步可以走
    即找到了倒数第n个节点
    '''
    def removeN(head, n):
        slow = fast = head
        if not head or n < 0:
            return None
        for _ in range(n):
            if not fast:
                return None
            fast = fast.next
        if not fast:  # n等于链表长度
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head