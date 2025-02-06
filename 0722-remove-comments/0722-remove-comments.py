class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        res = ''
        flag = False
        for i in source:
            tstr = i
            r = 0
            while r<len(i):
                if tstr[r:r+2] == "/*" and not flag:
                    flag = True
                    r+=1
                elif tstr[r:r+2] == "*/" and flag:
                    flag = False
                    r+=1
                elif tstr[r:r+2] == "//" and not flag:
                    break
                elif not flag:
                    res+=tstr[r]
                r+=1
            if not flag and res:
                ans.append(res)
                res = ''
        return ans