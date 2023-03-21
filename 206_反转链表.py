class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 思路：翻转链表：将当前节点的 next指针改为指向前一个节点。由于节点没有引用其前一个节点，因此必须事先存储其前一个节点。
        if head is None:
            return head
        prev, curr, nxt = None, head, head.next

        while curr:
            curr.next = prev
            prev = curr  # pre，和cur位置加1
            curr = nxt
            nxt = nxt.next if nxt else None
        
        return prev