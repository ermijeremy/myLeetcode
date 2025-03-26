class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def valid(n):
            ans = 0
            for i in ranks:
                ans += int(math.sqrt(n/i))
            return ans >= cars

        l, r = 1, min(ranks)*(cars**2)

        while l<=r:
            mid = (l+r)//2

            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
