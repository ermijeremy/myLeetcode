class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            ans.append(tot)
        return ans