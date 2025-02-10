class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f = True
        while f:
            f = False
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    f = True
                    nums[i], nums[i+1] = nums[i+1], nums[i]