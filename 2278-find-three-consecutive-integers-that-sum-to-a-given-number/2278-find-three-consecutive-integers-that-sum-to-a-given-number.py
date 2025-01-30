class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num%3!=0:
            return ans
        first = (num//3)-1
        ans.append(first)
        ans.append(first+1)
        ans.append(first+2)
        return ans