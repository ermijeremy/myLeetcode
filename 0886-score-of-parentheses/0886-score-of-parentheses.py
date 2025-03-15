class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        count ,pre = 0, ''

        for i in s:
            if i==")":
                stack.pop()
                count -= 1
                if pre=='(':
                    ans += 2**count
            else:
                stack.append(i)
                count += 1
            pre = i
        return ans