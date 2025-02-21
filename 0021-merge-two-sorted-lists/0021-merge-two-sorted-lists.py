# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1, list2)
        if (not list1) and (not list2):
            return None
        elif (not list1) and list2:
            return list2
        elif (not list2) and list1:
            return list1

        ans = []
        cur = list1
        while cur:
            ans.append(cur.val)
            cur = cur.next
        cur = list2
        while cur:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()

        new = ListNode(ans[0])
        cur = new

        for i in range(1,len(ans)):
            cur.next = ListNode(ans[i])
            cur = cur.next

        return new

