class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        close = float('inf')
        ans = 0

        for i in range(n):
            left,right = i+1, n-1
            while left < right:
                temp = nums[left] + nums[right] + nums[i]
                if temp == target:
                    return temp
                elif temp > target:
                    right -= 1
                else:
                    left += 1
                
                if abs(temp-target) <= close:
                    close = abs(temp-target)
                    ans = temp
  
        return ans