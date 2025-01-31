class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        converts = []
        result = 0

        for i in range(len(s)):
            if s[i] in letters:
                ind = letters.index(s[i])
                ind += 1
                while ind > 0:
                    converts.append((ind)%10)
                    ind = ind//10
        temp = sum(converts)
        print(temp)
        if k==1:
            return temp

        for i in range(k-1):
            result = 0
            while temp>0:
                result += temp%10
                temp = temp//10
            temp = result
        return result