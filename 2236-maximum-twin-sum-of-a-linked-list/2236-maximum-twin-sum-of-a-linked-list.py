class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur1 = prev
        cur2 = head
        ans = float('-inf')
        while cur2 and cur1:
            ans = max((cur1.val+cur2.val), ans)
            cur1 = cur1.next
            cur2 = cur2.next

        return ans        