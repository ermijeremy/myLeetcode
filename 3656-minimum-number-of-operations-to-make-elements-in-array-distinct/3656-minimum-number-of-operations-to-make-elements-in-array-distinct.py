class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        di = Counter(nums)
        count, i = -1,0

        while i<len(nums):
            if di[nums[i]]>1:
                di[nums[i]]-= 1
                count = i
            i += 1
        return math.ceil((count+1)/3)
        

