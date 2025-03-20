class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        di = Counter(nums)
        while i < len(nums):
            cur = nums[i]
            if di[nums[i]]>=2:
                i += 2
                while i<len(nums) and nums[i]==cur:
                    nums.pop(i)
            else:
                i += 1
        return len(nums)