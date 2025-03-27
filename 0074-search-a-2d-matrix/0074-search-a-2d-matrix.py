class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 0, 0
        check = set()

        for i in range(row):
            start, end  = matrix[i][0], matrix[i][col-1]

            if start <= target and target <= end:
                l, r = start, end
                check = set(matrix[i])
                break
        else:
            return False

        while l <= r:
            mid = (l+r)//2

            if mid > target:
                r = mid - 1
            elif mid < target:
                l = mid + 1
            else:
                if mid in check:
                    return True
                return False
        return False
        