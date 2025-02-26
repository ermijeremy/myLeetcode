class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        local_max = global_max = nums[0]
        local_min = global_min = nums[0]

        for i in range(1,len(nums)):
            local_max = max(nums[i], nums[i]+local_max)
            global_max = max( local_max, global_max)
            local_min = min(nums[i], nums[i]+local_min)
            global_min = min(local_min, global_min)

        return max(global_max, abs(global_min))