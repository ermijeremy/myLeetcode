class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        di = Counter(nums)
        di = sorted(di.items(),key = lambda x:x[1])
        ta, t = di[-1]
        count, n = 0, len(nums)
        for i in range(n):
            if nums[i]==ta:
                count += 1
            if count*2 > i+1 and (t-count)*2 > n-(i+1):
                return i
        return -1