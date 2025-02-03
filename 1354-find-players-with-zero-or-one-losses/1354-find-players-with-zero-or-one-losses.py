from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = []
        loser = []
        w = []
        l = []
        for i in matches:
            winner.append(i[0])
            loser.append(i[1])
        winner = Counter(winner)
        loser = Counter(loser)
        for i in loser:
            if loser[i]==1:
                l.append(i)
        for i in winner:
            if loser.get(i,0)==0:
                w.append(i)
        w = sorted(w)
        l = sorted(l)
        return [w,l]
