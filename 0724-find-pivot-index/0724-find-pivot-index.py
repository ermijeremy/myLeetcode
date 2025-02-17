class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        print(nums)
        for i in range(len(nums)):
            if i == 0 and nums[-1] - nums[i] ==0:
                return i
            if i == len(nums)-1 and nums[-2]==0:
                return i
            if i > 0 and nums[i-1] == nums[-1] - nums[i]:
                return i
        return -1