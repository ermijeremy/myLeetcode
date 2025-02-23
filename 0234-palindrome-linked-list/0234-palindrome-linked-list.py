# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        prev = slow.next = None
        first = head

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        while prev:
            if first.val != prev.val:
                return False
            first = first.next
            prev = prev.next
        return True