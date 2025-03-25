class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:

        def valid(n):
            cur,s = n,1
            for i in w:
                if cur-i<0:
                    cur = n
                    s += 1
                cur -= i
            return s<=days

        ans = 0
        l,r=max(w),sum(w)
        while l<=r:
            mid = (l+r)//2
            if not valid(mid):
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans

