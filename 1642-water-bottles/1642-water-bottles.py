class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result,full = numBottles,6
        while full > 0:
            full = numBottles//numExchange
            empity = numBottles%numExchange
            numBottles = full + empity
            result += full
        return result
        
        