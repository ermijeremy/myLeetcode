class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = 0
        pree = 0

        for i in range(len(meetings)):
            curs = meetings[i][0]
            if curs-pree>1:
                ans += curs-pree-1
            pree = max(pree,meetings[i][1])
        ans += days-pree
        return ans