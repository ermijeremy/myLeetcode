class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        k = 4
        while n>1:
            ans += k
            k += 4
            n -= 1
        return ans
