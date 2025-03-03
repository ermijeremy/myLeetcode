class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        maxx = 0
        j = n-1
        while j>1:
            i = j-2
            if nums[i]+nums[i+1] > nums[j]:
                return nums[i]+nums[i+1]+nums[j]
            j -= 1
        return 0
