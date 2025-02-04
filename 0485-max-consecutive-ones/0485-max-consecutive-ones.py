class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = (''.join([str(i) for i in nums])).split('0')
        return len(max(nums))