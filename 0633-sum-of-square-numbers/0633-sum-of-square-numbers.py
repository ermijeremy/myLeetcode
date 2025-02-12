class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(sqrt(c))
        while i <= j:
            if i**2 + j**2 > c:
                j-=1
            elif i**2 + j**2 < c:
                i+=1
            else:
                return True
        return False