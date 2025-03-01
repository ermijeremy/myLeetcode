class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set(i for i in range(1,n+1))
        b = set(nums)
        return(list(a-b))