class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        tot = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            tot += nums[right]
            l = right-left+1

            while (tot*l)>=k:
                tot -= nums[left]
                left += 1
                l = right-left+1
            
            ans += right - left + 1
        
        return ans