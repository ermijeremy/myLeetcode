class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right  # left ---------------------- right
        self.right.prev = self.left  #  0  ------------------------  0

    def get(self, index: int) -> int:
        dummy = self.left.next
        while dummy and index > 0:
            dummy = dummy.next
            index -= 1
        if index == 0 and dummy and dummy != self.right:
            return dummy.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_val,cur,prev = Node(val),self.left.next,self.left
        prev.next = new_val
        cur.prev = new_val
        new_val.next = cur
        new_val.prev = prev

    def addAtTail(self, val: int) -> None:
        new_val,cur,prev = Node(val),self.right,self.right.prev
        prev.next = new_val
        cur.prev = new_val
        new_val.next = cur
        new_val.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = self.left.next
        while dummy and index > 0:
            dummy = dummy.next
            index -= 1
        if index == 0 and dummy:
            new_val,cur,prev = Node(val),dummy,dummy.prev
            prev.next = new_val
            cur.prev = new_val
            new_val.next = cur
            new_val.prev = prev
        

    def deleteAtIndex(self, index: int) -> None:
        dummy = self.left.next
        while dummy and index > 0 :
            dummy = dummy.next
            index -= 1
        if   dummy and index == 0 and dummy != self.right:
            cur,prev = dummy.next,dummy.prev
            prev.next = cur
            cur.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)