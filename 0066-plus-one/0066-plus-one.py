class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(map(str,digits))
        a = int(a)+1
        a = str(a)
        return list(map(int,a))