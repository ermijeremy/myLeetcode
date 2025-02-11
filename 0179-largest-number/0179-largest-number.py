class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums)==0:
            return "0"
        x = list(map(str,nums))
        return ''.join(list(reversed(sorted(x,key = lambda x: x*100))))
