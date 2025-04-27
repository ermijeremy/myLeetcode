class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)-2):
            first,mid,last = nums[i],nums[i+1],nums[i+2]

            if (first+last)*2==mid:
                ans += 1
        return ans