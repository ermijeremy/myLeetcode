class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = ""
        s = list(s)
        for i in t:
            for j in range(len(s)):
                if i == s[j]:
                    s[j]=0
                    break
            else:
                r+=i
                continue
        return r