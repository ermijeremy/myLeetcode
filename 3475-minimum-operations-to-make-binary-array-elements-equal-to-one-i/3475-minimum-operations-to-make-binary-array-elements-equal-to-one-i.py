class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = i = 0
        while i<len(nums)-2:
            if nums[i]==1:
                i += 1
                continue
            else:
                for j in range(i,i+3):
                    nums[j] ^= 1
                ans += 1
            i += 1
        if len(set(nums))==1:
            return ans
        else:
            return -1