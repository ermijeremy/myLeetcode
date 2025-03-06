class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        n = len(t)-1
        ans = []

        for i in range(n,-1,-1):
            while stack and t[i] >= stack[-1][0]:
                stack.pop()
            stack.append([t[i],i])
            if len(stack)>=2:
                ans.append(stack[-2][1]-stack[-1][1])
            else:
                ans.append(0)

        return list(reversed(ans))