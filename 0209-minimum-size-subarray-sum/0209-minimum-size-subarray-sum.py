class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        nums = [0] + nums
        ans = float('inf')
        window = 0
        left = 0

        for right in range(len(nums)):
            window = nums[right]
            while window-nums[left] >= target:
                left += 1
                ans = min(ans,(right - left + 1))

        if ans == float('inf'):
            return 0
        return ans