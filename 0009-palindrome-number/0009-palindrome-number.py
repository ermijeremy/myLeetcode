class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        temp = x
        if x <0:
            return False
        while x>0:
            remainder = x%10
            result = (result*10)+remainder
            x = x//10
        return temp==result
