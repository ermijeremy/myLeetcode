class Solution:
    def romanToInt(self, s: str) -> int:
        value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s = list(s)
        result = value[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if value[s[i]]<value[s[i+1]]:
                result -= value[s[i]]
            else:
                result += value[s[i]]
        return result
        
