class Solution:
    def minSteps(self, s: str, t: str) -> int:
        di = Counter(t)
        di1 = Counter(s)
        dif = sum((di1-di).values())
        return(dif)