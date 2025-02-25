class Node:
    def __init__(self,key=0,val=0):
        self.key,self.val = key,val
        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.right = self.left = Node()
        self.left.next, self.right.prev = self.right,self.left
        self.cach = {}

    def delete(self,node):
        temp,temp1 = node.next,node.prev
        temp.prev,temp1.next = temp1,temp


    def insert(self,node):
        cur,prev = self.right,self.right.prev
        cur.prev = node
        node.prev = prev
        prev.next = node
        node.next = cur


    def get(self, key: int) -> int:
        if key not in self.cach:
            return -1

        self.delete(self.cach[key])
        self.insert(self.cach[key])
        return self.cach[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cach:
            self.delete(self.cach[key])
            del self.cach[key]
        self.cach[key] = Node(key,value)
        self.insert(self.cach[key])
        
        if len(self.cach) > self.cap:
            least = self.left.next
            self.delete(least)
            del self.cach[least.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)