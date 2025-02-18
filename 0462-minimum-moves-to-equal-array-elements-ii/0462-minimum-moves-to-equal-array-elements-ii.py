class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums)-1
        ans = 0
        while i < j:
            ans += abs(nums[i]-nums[j])
            i+=1
            j-=1
        return ans


        # using their median
        # if len(nums)%2==0:
        #     mid = (nums[len(nums)//2]+nums[(len(nums)//2)-1])//2
        # else:
        #     mid = nums[len(nums)//2]
        # for i in nums:
        #     ans += abs(i-mid)
        # return ans