class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            left, right, = i + 1, n-1
            if i > 0 and nums[i]==nums[i-1]:
                continue
                
            temp = nums[i]
            while left < right:
                if nums[left] + nums[right] > -(temp):
                    right -= 1
                elif nums[left] + nums[right] < -(temp):
                    left += 1
                else:
                    ans.append([temp,nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left -1]:  
                        left += 1
        return ans