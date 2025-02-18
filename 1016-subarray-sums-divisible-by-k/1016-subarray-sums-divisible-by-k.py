class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        di = defaultdict(int)
        di[0]  = 1
        count = 0
        
        for i in nums:
            temp = i % k
            count += di[temp]
            di[temp] += 1

        return count