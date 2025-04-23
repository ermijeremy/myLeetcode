class Solution:
    def countLargestGroup(self, n: int) -> int:
        di = defaultdict(int)
        for i in range(1,n+1):
            s = 0
            while i:
                s += i%10
                i //= 10
            di[s] += 1

        # Counting the number of largest sized gropus
        di = sorted(di.values(), reverse = True)
        t, i, ans = di[0], 0, 0
        while i<len(di) and di[i]==t:
            ans += 1
            i += 1
            
        return ans