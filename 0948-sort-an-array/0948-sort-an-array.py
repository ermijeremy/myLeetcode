class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        m = abs(min(nums))
        a = [0]*(max(nums)+1+m)
        b = []
        for i in nums:
            a[i+m] += 1
        for i,j in enumerate(a):
            for k in range(j):
                b.append(i-m)
        return b