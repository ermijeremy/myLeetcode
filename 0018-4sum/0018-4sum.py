class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum_recursion(nums, 0, 4, target)

    def k_sum_recursion(self, nums, index, k, target):
            if k == 2:
                return self.two_sum(nums, index, len(nums) - 1, target)

            result = []
            for i in range(index, len(nums) - k + 1):
                for subset in self.k_sum_recursion(nums, i + 1, k - 1, target - nums[i]):
                    if [nums[i]] + subset not in result:
                        result.append([nums[i]] + subset)
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
            return result

    def two_sum(self,nums, left, right, target):
            result = []
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    if [nums[left], nums[right]] not in result:
                        result.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return result