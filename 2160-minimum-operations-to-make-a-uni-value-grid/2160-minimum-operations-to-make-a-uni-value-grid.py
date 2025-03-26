class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        li = []

        for i in grid:
            li.extend(i)
        li.sort()
        mid = 0
        if len(li)%2:
            mid = len(li)//2
        else:
            mid = len(li)//2-1
        target = li[mid]
        ans = tot = 0
        for i in li:
            tot += abs(i-target)
            if tot%x:
                return -1
            ans += abs(i-target)//x
        return ans