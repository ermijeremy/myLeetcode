class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)-extraCandies
        return [True if i>=maxx else False for i in candies]
        