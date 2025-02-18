class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        s = [1]
        for i in range(len(nums)-1):
            p.append(p[-1]*nums[i])
        for i in nums[len(nums)-1:0:-1]:
            s.append(s[-1]*i)
        s = list(reversed(s))
        ans = [x[0]*x[1] for x in zip(p,s)]
        
        return ans