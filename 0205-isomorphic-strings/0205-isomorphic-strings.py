class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = i
            if t[i] not in dic2:
                dic2[t[i]] = i
            if dic1[s[i]] != dic2[t[i]]:
                return False
        return True

