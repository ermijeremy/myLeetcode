class Solution:
    def firstUniqChar(self, s: str) -> int:
        di = Counter(s)
        element = 0
        for i in di:
            if di[i]==1:
                return s.index(i)
        return -1