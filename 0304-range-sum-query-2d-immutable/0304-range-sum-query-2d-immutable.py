class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        temp = [0]*len(self.matrix[0])

        self.matrix = [temp] + self.matrix
        for i in range(len(self.matrix)):
            self.matrix[i] = [0] + self.matrix[i]
        row = len(self.matrix)
        col = len(self.matrix[0])

        for r in range(1,row):
            for c in range(1,col):
                self.matrix[r][c] = self.matrix[r][c] + self.matrix[r-1][c] + self.matrix[r][c-1] - self.matrix[r-1][c-1]
        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ro, co = row2 + 1, col2 + 1

        return (self.matrix[row2+1][col2+1] + self.matrix[row1][col1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1])

        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)