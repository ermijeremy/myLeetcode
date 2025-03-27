class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        check = set(p)
        p.sort()

        def valid(n):
            count, i = 1, 0
            while i < len(p):
                temp = p[i]+n
                if temp in check:
                    count += 1
                    i = bisect_left(p,temp)
                else:
                    if temp > p[-1]:
                        return count >= m
                    a = bisect_left(p,temp)
                    count += 1
                    i = a
            return count >= m

        l, r = 1, p[-1]-1

        while l <= r:
            mid = (l+r)//2
            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
        