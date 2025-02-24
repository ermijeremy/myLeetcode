class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        if not head or not fast or not fast.next:
            return
        
        slow = head

        while fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next