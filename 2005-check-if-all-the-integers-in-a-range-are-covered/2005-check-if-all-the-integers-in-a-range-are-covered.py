class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        alls = set()
        for i in ranges:
            alls |= set(range(i[0],i[1]+1))
        for i in range(left,right+1):
            if not i in alls:
                return False
        return True