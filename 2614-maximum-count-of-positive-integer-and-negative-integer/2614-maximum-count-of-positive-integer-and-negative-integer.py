class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a = bisect.bisect_left(nums,0)
        b = bisect.bisect_right(nums,0)
        return max(a,len(nums)-b)
