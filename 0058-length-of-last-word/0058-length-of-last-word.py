class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in s[::-1]:
            if i.isalnum():
                count += 1
            else:
                if count > 0:
                    return count
        return count