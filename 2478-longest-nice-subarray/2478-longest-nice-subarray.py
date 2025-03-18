class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        left = 0
        cur = 0

        for right in range(len(nums)):
            while cur&nums[right]:
                cur ^= nums[left]
                left += 1
            ans = max(right-left+1,ans)
            cur |= nums[right]

        return ans