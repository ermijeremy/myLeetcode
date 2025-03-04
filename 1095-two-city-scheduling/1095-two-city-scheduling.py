class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = sorted(costs,key = lambda x:x[1]-x[0])
        aa = []
        bb = []
        for i in a:
            if (len(bb)<len(costs)//2):
                bb.append(i[1])
            elif (len(aa)<len(costs)//2):
                aa.append(i[0])
        
        return sum(aa)+sum(bb)