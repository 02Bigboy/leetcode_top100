# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 
class Solution:
    '''
    思路：就是先找中间节点，然后将两边分别排序，排好了之后调用合并有序链表
    '''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #分
        #首先找到中间节点
        mid = self.middleNode(head)

        #注意上面寻找中间节点的函数中已经把中间节点和前面的节点解开了
        left = self.sortList(head)
        right = self.sortList(mid)

        #合并有序链表
        return self.merge(left, right)

    #这是第876题
    def middleNode(self, head: ListNode) -> ListNode:
        #使用快慢指针
        if not head or not head.next:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        #在这里把前半部分链表和后半部分链表断开
        pre.next = None
        return slow
        
    #合并两个有序链表，这是剑指Offer25题
    def merge(self, l1, l2):
        #递归法
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2



class Solution:
    '''
    思路：就是先找中间节点，然后将两边分别排序，排好了之后调用合并有序链表
    '''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findmid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)
    def findmid(self, head):
        # 通过快慢指针，找中点：
        slow = head
        fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None   # 断开链表
        return slow
    def merge(self, m1, m2):
        if not m1:
            return m2
        if not m1:
            return m1
        if m1.val <= m2.val:
            m1.next = self.merge(m1.next, m2)
            return m1
        else:
            m2.next = self.merge(m2.next, m1)
            return m2