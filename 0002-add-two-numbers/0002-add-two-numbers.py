# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []

        cur = l1
        while cur:
            first.append(str(cur.val))
            cur = cur.next
        cur = l2
        while cur:
            second.append(str(cur.val))
            cur = cur.next

        temp = int(''.join(reversed(first))) + int(''.join(reversed(second)))
        last = list(map(int,reversed(str(temp))))

        ans = ListNode()
        cur = ans
        for i in last:
            ans.next = ListNode(i)
            ans = ans.next

        return cur.next

        
