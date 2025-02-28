class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s = sorted(s,key = lambda x:x[-1])
        ans = ""
        for i in s:
            ans += i.replace(i[-1]," ")
        return ans.rstrip()