class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        count = 0
        i = 0
        while res < coins and i < len(costs):
            res += costs[i]
            if res <= coins:
                count+=1
            i+=1
        return count