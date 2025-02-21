# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        ans = []
        dummy = head
        while dummy:
            ans.append(dummy.val)
            dummy = dummy.next
        temp = list(reversed(ans))

        return ans == temp