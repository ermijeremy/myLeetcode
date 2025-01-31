class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            temp = s[0]
            s = s[1::]
            s += temp
            if s == goal:
                return True
        return False