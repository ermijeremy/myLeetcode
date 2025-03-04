class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans = []

        while n:
            i = 1
            while (3**i)<=n:
                i += 1
            ans.append(i-1)
            n -= (3**(i-1))
            
        return len(ans) == len(set(ans))