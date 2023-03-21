# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = new = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    new.next = ListNode(list1.val)
                    new = new.next
                    list1 = list1.next
                else:
                    new.next = ListNode(list2.val)
                    new = new.next
                    list2 = list2.next
            elif list1:
                new.next = ListNode(list1.val)
                new = new.next
                list1 = list1.next
            else:
                new.next = ListNode(list2.val)
                new = new.next
                list2 = list2.next
        return head.next