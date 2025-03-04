class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        di = Counter(s)
        ans = "1"*(di['1']-1)+"0"*(di['0'])+"1"
        return ans
