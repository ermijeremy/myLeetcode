class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        di = defaultdict(int)
        ans = []
        n = 1
        flag = True
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                di[grid[r][c]] += 1
                if di[grid[r][c]] == 2 and flag:
                    ans.append(grid[r][c])
                    flag = False
        for i in range(1,(len(grid)**2)+1):
            if di[i] == 0:
                ans.append(i)
                return ans

        

