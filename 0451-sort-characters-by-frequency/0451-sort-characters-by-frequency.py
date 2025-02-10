class Solution:
    def frequencySort(self, s: str) -> str:
        sc = Counter(s)
        sc = sorted(sc.items(), key = lambda x:x[1], reverse = True)
        ans = []
        for i,j in sc:
            for k in range(j):
                ans.append(i)
        return ''.join(ans)