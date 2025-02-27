class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_sum = [0]*(len(nums)+1)
        odd_sum = [0]*(len(nums)+1)

        for i, val in enumerate(nums):
            if i%2:
                odd_sum[i+1] = odd_sum[i]+val
                even_sum[i+1] = even_sum[i]   
            else:
                even_sum[i+1] = even_sum[i]+val
                odd_sum[i+1] = odd_sum[i]
                
        ans = 0  
        for i in range(1,len(nums)+1):
            odd_sum1 = odd_sum[i-1]
            even_sum1 = even_sum[i-1]

            odd_sum2 = even_sum[-1] - even_sum[i]
            even_sum2 = odd_sum[-1] - odd_sum[i]

            if odd_sum2 + odd_sum1 == even_sum2 + even_sum1:
                ans += 1

        return ans