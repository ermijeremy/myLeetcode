class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cop = copy.deepcopy(nums)
        for i in range(len(nums)):
            if i + k <= len(nums)-1:
                nums[i+k] = cop[i]
            else:
                nums[(i+k)%len(nums)] = cop[i]
        print(nums)