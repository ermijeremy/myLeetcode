class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0

        i = 0
        while i < len(s):
            co = -2
            flag = True
            while co != 0:
                if flag:
                    co = 0
                    flag = False
                if s[i] == "R":
                    co += 1
                else:
                    co -= 1
                i += 1
            ans += 1

        return ans