class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        K = celsius + 273.15
        F = celsius*1.80 + 32.00
        ans.append(K)
        ans.append(F)
        return ans