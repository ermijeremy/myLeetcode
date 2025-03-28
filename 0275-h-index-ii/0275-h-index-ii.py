class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort()
        def valid(n):
            a = bisect_left(c,n)
            return n<=(len(c)-a)
        
        l, r = 0, c[-1]+1

        while l <= r:
            mid = (l+r)//2

            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans