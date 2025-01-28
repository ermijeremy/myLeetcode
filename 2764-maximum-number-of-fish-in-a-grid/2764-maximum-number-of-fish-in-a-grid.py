class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if len(grid)<1:
            return 0
        row_len = len(grid)
        col_len = len(grid[0])
        fish = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c]!=0:
                    fish = max(fish,self.find(r,c,grid))
        return fish
    def find(self,r,c,grid):
        if c<0 or c>=len(grid[0]) or r<0 or r>=len(grid):
            return 0
        if grid[r][c]!=0:
            a = grid[r][c]
            grid[r][c]=0
            return (a+
            (self.find(r+1,c,grid))
            +(self.find(r-1,c,grid))
            +(self.find(r,c+1,grid))
            +(self.find(r,c-1,grid))
            )
        return 0