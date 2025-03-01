class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set(i for i in range(1,n+1))
        b = set(nums)
        for i in nums:
            if nums.count(i) == 2:
                return ([i]+list(a-b))