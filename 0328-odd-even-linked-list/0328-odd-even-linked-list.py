# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd,even = ListNode(),ListNode()
        od,eve = odd,even

        i = 0

        while head:
            if (i+1)%2==1:
                od.next = head
                od = od.next
            else:
                eve.next = head
                eve = eve.next
            i+=1
            head = head.next

        od.next = even.next
        eve.next = None

        return odd.next


        