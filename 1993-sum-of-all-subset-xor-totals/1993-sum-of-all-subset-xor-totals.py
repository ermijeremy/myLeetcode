class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        for i in range(1,len(nums)+1):
            ans.extend(list(map(list,itertools.combinations(nums,i))))
        res = 0

        for i in ans:
            temp = 0
            for j in i:
                temp^=j
            res += temp
        return res