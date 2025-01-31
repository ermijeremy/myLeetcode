class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        string = ''.join(map(str,nums))
        for i in string:
            result.append(int(i))
        return result