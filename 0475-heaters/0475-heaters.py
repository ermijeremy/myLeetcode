class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def valid(n):
            cover = []
            j = 0
            for i in heaters:
                cover.append([i-n,i+n])
            cover.sort()
            if houses[-1] > cover[-1][1]:
                return False
            for i in range(len(houses)):
                if cover[j][0] > houses[i]:
                    return False
                while j<=len(cover) and houses[i] > cover[j][1]:
                    j += 1
                if j < len(cover) and cover[j][0] > houses[i]:
                    return False
            return True
        # print(valid(5))

        l, r = 0, int(1e9)

        ans = 0
        while l <= r:
            mid = (l+r)//2

            if valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans