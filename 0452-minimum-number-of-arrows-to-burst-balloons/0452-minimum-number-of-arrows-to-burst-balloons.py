class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        res = [points[0]]

        i,j = 1,0
        while i < len(points):
            cs,ce = points[i][0],points[i][1]
            ns,ne = res[j][0],res[j][1]
            if cs <= ne:
                res[-1] = [cs,ne]
            else:
                res.append(points[i])
                j += 1
            i += 1
        return len(res)
            

