class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di = Counter(nums)
        for i in di.values():
            if i>1:
                return True
        return  False