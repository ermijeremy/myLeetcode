class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        di = Counter(nums)
        res = 0
        for i in di.values():
            res += i//2
        return [res,len(nums)-(2*res)]