class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        maxpair = []
        minpair = []

        for i in range(len(w)-1):
            maxpair.append(w[i]+w[i+1])
        n = len(w)
        maxpair.sort()
        ans = 0
        print(maxpair)
        for i in range(k - 1):
            ans += maxpair[n - 2 - i] - maxpair[i]
        return ans