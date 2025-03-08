class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        n = len(blocks)

        for right in range(n-k+1):
            temp = blocks[right:right+k]
            temp = k-temp.count('B')
            ans = min(ans,temp)
        return ans