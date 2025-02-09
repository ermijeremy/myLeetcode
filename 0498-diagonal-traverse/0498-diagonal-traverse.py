class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        # initialize 4 pointers
        row = len(mat)
        col = len(mat[0])

        up = True
        r = c = 0
        while len(ans) < row*col:
            if up:
                while r >= 0 and c < col:
                    ans.append(mat[r][c])
                    r -= 1
                    c += 1
                if c == col:
                    r += 2
                    c -= 1
                else:
                    r += 1
                up = False
            else:
                while r < row and c >= 0:
                    ans.append(mat[r][c])
                    r += 1
                    c -= 1
                if r == row:
                    c += 2
                    r -= 1
                else:
                    c += 1
                up = True

        return ans