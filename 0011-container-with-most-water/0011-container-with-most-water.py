class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = []
        i = 0
        j = len(height)-1
        while i < j:
            if height[i] < height[j]:
                ans.append(height[i]*(j-i))
                i+=1
            else:
                ans.append(height[j]*(j-i))
                j-=1
        return max(ans)