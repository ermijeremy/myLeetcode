class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            a = target-nums[i]
            if di.get(a,-1)==-1:
                di[nums[i]] = i
            else:
                return [di[a],i]
        return []