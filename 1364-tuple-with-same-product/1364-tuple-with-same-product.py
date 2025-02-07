class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        di = {}
        ans = 0
        nums = set(nums)
        for i in nums:
            for j in range(i):
                if j in nums:
                    ans += di.get(i*j,0)*8
                    di[i*j] = di.get(i*j, 0) + 1
        print(di)
        return ans