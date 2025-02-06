class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        di = Counter(nums)
        for i,j in di.items():
            if j>1:
                ans.append(i)
        return ans