class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if (not list1) and (not list2):
            return None
        elif (not list1) and list2:
            return list2
        elif (not list2) and list1:
            return list1

        prev = ListNode(-999)
        prev.next = list2
        cur1 = list1

        while cur1:
            temp = cur1
            temp1 = cur1.next
            cur = prev
            while cur and cur1.val > cur.val:
                pre = cur
                cur = cur.next
            pre.next = temp
            temp.next = cur
            cur1 = temp1

        return prev.next