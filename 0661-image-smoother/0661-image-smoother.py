class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans = copy.deepcopy(img)
        for r in range(len(img)):
            for c in range(len(img[0])):
                res = 0
                count = 0
                if r < len(img)-1 and c < len(img[0])-1:
                    res += img[r+1][c+1]
                    count += 1
                if r > 0 and c > 0:
                    res += img[r-1][c-1]
                    count += 1
                if r < len(img)-1 and c > 0:
                    res += img[r+1][c-1]
                    count += 1
                if r > 0 and c < len(img[0])-1:
                    res += img[r-1][c+1]
                    count += 1
                if r > 0:
                    res += img[r-1][c]
                    count += 1
                if c < len(img[0])-1:
                    res += img[r][c+1]
                    count += 1
                if c > 0:
                    res += img[r][c-1]
                    count += 1
                if r < len(img)-1:
                    res += img[r+1][c]
                    count += 1
                print((res+img[r][c]),count+1)
                ans[r][c] = (res+img[r][c])//(count+1)
        return ans            