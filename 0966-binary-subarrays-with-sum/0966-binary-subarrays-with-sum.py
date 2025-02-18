class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        nums = list(itertools.accumulate(nums))
        di = defaultdict(int)
        di[0] = 1
        ans = 0
        for i in nums:
            ans += di[i - goal]
            di[i] += 1
        
        return ans