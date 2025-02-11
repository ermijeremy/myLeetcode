class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        left, right = 0, len(piles)-1
        res = 0
        while left < right-1:
            res += piles[right-1]
            left+=1
            right-=2
        return res