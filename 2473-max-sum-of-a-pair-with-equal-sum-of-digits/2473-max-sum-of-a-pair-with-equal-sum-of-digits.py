class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        def digsum(num):
            res = 0
            while num > 0:
                res += num % 10 
                num = num // 10 
            return res

        temp = {}
        res = 0
        for i in range(len(nums)):
            a = digsum(nums[i])
            if temp.get(a,0):
                temp[a].append(nums[i])
            else:
                temp[a] = [nums[i]]
        
        for i in temp.values():
            i.sort()
            if len(i)>1:
                tem = i[len(i)-1]+i[len(i)-2]
                res = max(tem,res)

        if res > 0:
            return res
        else:
            return -1