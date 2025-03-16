class Solution:
    def rob(self, nums: List[int]) -> int:
        a=b=0
        for i in nums: t=max(i+a,b);a=b;b=t
        return b
