class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        ans = 0
        while l<=r:
            mid = (l+r)//2

            if mid*mid<x:
                ans = mid
                l = mid + 1
            elif mid*mid>x:
                r = mid-1
            else:
                return mid
        else:
            return ans