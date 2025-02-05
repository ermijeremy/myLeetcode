class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ans = set()
        di = Counter(s)
        for i in di.values():
            ans.add(i)
        return len(ans)==1