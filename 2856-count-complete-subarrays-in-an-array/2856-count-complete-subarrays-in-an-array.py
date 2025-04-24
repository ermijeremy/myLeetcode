class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique = set(nums)
        n = len(unique)

        window = []
        ans = 0
        left = 0

        for i in range(len(nums)):
            window = set()
            for j in range(i,len(nums)):
                window.add(nums[j])
                if len(window)==n:
                    ans += 1
        
        return ans