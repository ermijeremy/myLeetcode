class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        di = Counter(nums)
        for i,j in di.items():
            if j%2:
                return False
        return True