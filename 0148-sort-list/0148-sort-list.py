# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (not head.next):
            return head
        ans = []
        cur = head

        while cur:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()
        cur = ListNode(ans[0])
        head = cur
        for i in range(1,len(ans)):
            nex = ListNode(ans[i])
            cur.next = nex
            cur = cur.next
        return head