class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        di = Counter(nums)
        for i in di.values():
            if i>1:
                res += (i*(i-1))//2
        return res
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             res+=1
        # return res