class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        querie = [0]*(len(s)+1)

        for i,j,k in shifts:
            if k == 0:
                querie[i] -= 1
                querie[j+1] += 1
            else:
                querie[i] += 1
                querie[j+1] -= 1

        for i in range(1,len(querie)):
            querie[i] += querie[i-1]

        for i in range(len(s)):
            index = (ord(s[i]) - ord('a') + querie[i]) % 26
            s[i] = chr(index + ord('a'))


        return ''.join(s)