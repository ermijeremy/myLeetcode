class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect_left(nums,target)
        b = bisect_right(nums,target)
        if a==b:
            return [-1,-1]
        return [a,b-1]