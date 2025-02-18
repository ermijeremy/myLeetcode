class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        temp = [0]*(len(nums)+1)
        nums.sort(reverse = True)

        for i in requests:
            temp[i[0]] += 1
            temp[i[1]+1] += -1
        
        for i in range(1,len(temp)):
            temp[i] += temp[i-1]
        temp.sort(reverse = True)
        
        temp1 = zip(nums,temp)
        ans = 0
        for i,j in temp1:
            ans += i*j
        return ans%(10**9+7)
