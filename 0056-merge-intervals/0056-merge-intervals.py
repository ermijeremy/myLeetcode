class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        j = 0
        for i in range(1,len(intervals)):
            begin, end = ans[j][0],ans[j][1]#intervals[i-1][0], intervals[i-1][1]
            cbegin, cend = intervals[i][0], intervals[i][1]
            if end >= cbegin:
                if end >= cend:
                    ans[j][1] = end
                else:
                    ans[j][1] = cend
            else:
                ans.append(intervals[i])
                j += 1

        print(intervals)
        return ans