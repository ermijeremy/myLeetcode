# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle and break the list into two parts
        slow, fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse the second list

        cur = second
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # merge the first and the second list

        cur = head
        cur1 = prev
        while cur1:
            temp, temp1 = cur.next, cur1.next
            cur.next = cur1
            cur1.next = temp
            cur = temp
            cur1 = temp1