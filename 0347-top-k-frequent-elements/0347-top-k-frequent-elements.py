class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = Counter(nums)
        di = sorted(di.items(),key=lambda x: x[1],reverse = True)
        return [di[i][0] for i in range(k)]