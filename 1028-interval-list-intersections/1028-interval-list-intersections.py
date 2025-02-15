class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        ans = []

        if len(first) > len(second):
            for i in range(len(first)):
                f_min = first[i][0]
                f_max = first[i][1]
                for j in range(len(second)):
                    s_min = second[j][0]
                    s_max = second[j][1]
                    if f_max < s_min or s_max < f_min:
                        continue
                    a = max(f_min,s_min)
                    b = min(f_max,s_max)
                    ans.append([a,b])
        else:
            for i in range(len(second)):
                s_min = second[i][0]
                s_max = second[i][1]
                for j in range(len(first)):
                    f_min = first[j][0]
                    f_max = first[j][1]
                    if f_max < s_min or s_max < f_min:
                        continue
                    a = max(s_min,f_min)
                    b = min(s_max,f_max)
                    ans.append([a,b])

        return ans