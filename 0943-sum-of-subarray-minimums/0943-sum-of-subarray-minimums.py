class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stackF, stackR = [], []
        ans = []
        ans1 = []

        # forward
        for i in arr:
            count = 1
            while stackF and stackF[-1][0]>i:
                count += stackF[-1][1]
                stackF.pop()
            stackF.append([i,count])
            ans.append(count)
       
        # backward
        for i in arr[::-1]:
            count = 1
            while stackR and stackR[-1][0]>=i:
                count += stackR[-1][1]
                stackR.pop()
            stackR.append([i,count])
            ans1.append(count)
        
        final = 0

        for i in range(len(arr)):
            final += ans[i]*ans1[len(arr)-i-1]*arr[i]
        
        return final%(10**9 + 7)