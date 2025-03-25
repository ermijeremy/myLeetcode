class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(n):
            count = 0
            for i in piles:
                if i <= n:
                    count += 1
                    continue
                count += math.ceil(i/n)
            return count<=h

        l, r, ans = 1, max(piles), 0

        while l<=r:
            mid = (l+r)//2

            if valid(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans