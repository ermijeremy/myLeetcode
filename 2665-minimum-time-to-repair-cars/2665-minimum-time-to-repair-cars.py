class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort(reverse = True)

        ans = float('inf')
        left, right = 1, ranks[-1]*(cars**2)

        while left <= right:
            mid = (left+right)//2
            t = 0
            for i in ranks:
                t += int(math.sqrt(mid/i))
            if t >= cars:
                ans = min(ans,mid)
                right = mid-1
            else:
                left = mid + 1
        return ans