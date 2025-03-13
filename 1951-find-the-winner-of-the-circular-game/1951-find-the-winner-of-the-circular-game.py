class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        li, i = list(range(1,n+1)), 0

        while len(li)>1:
            i = (i+k-1)%n
            li.pop(i)
            n -= 1
        return li[0]