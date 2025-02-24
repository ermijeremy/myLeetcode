# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        left,right = prev,head

        while right:
            if n <= 0:
                left = left.next
            right = right.next
            n -= 1
        print(left.val)
        if left.next:
            temp = left.next.next
            left.next = temp
        else:
            left = None
    
        return prev.next