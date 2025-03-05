class Solution:
    def coloredCells(self, n: int) -> int:
        return (1 if n==1 else ((n-1)*(2*(n-1)+2)+1))