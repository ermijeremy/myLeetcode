class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(s.lower().split(" "))
        s3  = []
        for i in s2:
            if i.isalnum():
                s3.append(i)
        return(s3==s3[::-1])