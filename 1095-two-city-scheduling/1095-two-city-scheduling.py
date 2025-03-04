class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(costs,key = lambda x:x[1]-x[0])
        ans = 0
        for i in range(len(a)):
            if i < len(costs)//2:
                ans += a[i][1]
            else:
                ans += a[i][0]
        
        return ans