class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        count = 0

        for i in s[::-1]:
            if i == '0':
                count += 1
            else:
                ans += count

        return ans