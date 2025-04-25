class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        persons = [0]*(n+1)
        di = dict(trust)
        persons[0] = -1

        for i in trust:
            persons[i[1]] += 1
        
        if (n-1) not in persons:
            return -1
        
        ind = persons.index(n-1)

        if di.get(ind,0):
            return -1
        return ind