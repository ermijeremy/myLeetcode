class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:        
        if not head or not head.next:
            return head
        # to target
        prev = ListNode(float("-inf"))
        prev.next = head
        temp = prev
        target = target1 = None

        while temp:
            if  temp.next and temp.val < x and temp.next.val >= x:
                target = temp
                target1 = temp.next
                break
            temp = temp.next

        if target and target1:
            curr = target1
            while curr:
                while curr.next and curr.next.val < x:
                    temp = curr.next
                    target.next = temp
                    curr.next = temp.next
                    temp.next = target1
                    target = temp
                curr = curr.next
        else:
            return head

        return prev.next