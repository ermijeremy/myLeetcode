class Solution:
    def numRabbits(self, an: List[int]) -> int:
        ans = 0
        di = Counter(an)

        for i,j in di.items():
            if i==0:
                ans += j
            elif j>i:
                ans += (i+1)*math.ceil(j/(i+1))
            else:
                ans += i+1
        return ans

        
