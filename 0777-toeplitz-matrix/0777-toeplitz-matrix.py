class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ans = set()
        for k in range(len(matrix)):
            for j in range(len(matrix[0])):
                i,row = j,k
                while i<len(matrix[0]) and row<len(matrix):
                    ans.add(matrix[row][i])
                    i+=1
                    row+=1
                if len(ans)!=1:
                    return False
                ans = set()
        return True