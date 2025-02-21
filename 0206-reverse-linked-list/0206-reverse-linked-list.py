# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=2, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ans = []
        dummy = head
        while dummy:
            ans.append(dummy.val)
            dummy = dummy.next
        new = ListNode(ans[-1])
        dummy = new
        for i in ans[-2::-1]:
            dummy.next = ListNode(i)
            dummy = dummy.next
        print(ans)
        return new       