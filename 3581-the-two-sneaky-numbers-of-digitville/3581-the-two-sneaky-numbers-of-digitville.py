class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        di = Counter(nums)
        ans = []
        print(di)
        for i in di:
            if di[i]>1:
                ans.append(i)
        return ans