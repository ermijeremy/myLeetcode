class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        a = []
        b = ""
        maxx = 0
        for i in s:
            maxx = max(maxx,len(i))
        for i in range(maxx):
            for j in range(len(s)):
                try:
                    b+=(s[j][i])
                    if len(b)==len(s):
                        a.append(b)
                        b = ""
                except:
                    b+=" "
                    if len(b)==len(s):
                        b = b.rstrip(" ")
                        a.append(b)
                        b = ""
        return a