class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        new_ma = []
        res = []
        for i in range(col):
            for j in range(row):
                res.append(matrix[j][i])
            new_ma.append(res)
            res = []
        return new_ma