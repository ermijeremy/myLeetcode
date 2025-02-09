class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        # initializilng the 4 boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # first go right
            for i in range(left, right):
                ans.append(matrix[left][i])
            top += 1
            #  then go down
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            right -= 1
            
            # break to not to go to left after the matrix is finished
            if left == right or top == bottom:
                break

            # then go left
            for i in range(right-1,left-1,-1):
                ans.append(matrix[bottom-1][i])
            bottom -= 1
            # then go up
            for i in range(bottom-1,top-1,-1):
                ans.append(matrix[i][left])
            
            left += 1

        return ans