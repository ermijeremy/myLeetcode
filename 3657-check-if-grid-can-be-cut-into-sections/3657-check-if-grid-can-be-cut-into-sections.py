class Solution:
    def checkValidCuts(self, n: int, r: list[list[int]]) -> bool:
        r.sort(key=lambda x:x[1])
        count = 0
        pree = -1
        for i in range(len(r)):
            curs = r[i][1]
            if curs>=pree:
                count += 1
            pree = max(pree,r[i][3])
        r.sort(key = lambda x:x[0])
        count1 = 0
        pree = -1
        for i in range(len(r)):
            curs = r[i][0]
            if curs>=pree:
                count1 += 1
            pree = max(pree,r[i][2])
        return count>=3 or count1>=3