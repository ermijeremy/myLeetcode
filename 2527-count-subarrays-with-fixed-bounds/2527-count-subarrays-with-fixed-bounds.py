class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        b = minn = maxx = -1
        ans = 0

        for i in range(len(nums)):
            if nums[i]<minK or nums[i]>maxK:
                b = i
            if nums[i]==minK:
                minn = i
            if nums[i]==maxK:
                maxx = i
            ans += max(0,min(maxx,minn)-b)
        return ans