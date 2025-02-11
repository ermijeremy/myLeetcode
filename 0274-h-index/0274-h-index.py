class Solution:
    def hIndex(self, citations: List[int]) -> int:
        a = sorted(citations)
        b = [-1]*(max(a)+1)
        l = len(a)
        for i in range(len(a)):
            if not a[i] in a[:i]:
                b[a[i]] = l
            l-=1
        maxx = 0
        for i in range(len(b)):
            if b[i] >= i:
                maxx = max(maxx,i)
            if b[i]<=i:
                maxx = max(maxx,b[i])
        return maxx