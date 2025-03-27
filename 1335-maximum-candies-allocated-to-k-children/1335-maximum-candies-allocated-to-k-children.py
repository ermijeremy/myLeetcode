class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid(n):
            count = 0
            for i in candies:
                count += i//n
            return count>=k

        ans = 0
        l, r = 1, max(candies)
        while l<=r:
            mid = (l+r)//2

            if valid(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return ans