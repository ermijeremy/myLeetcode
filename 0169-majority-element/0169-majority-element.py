class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = Counter(nums)
        di = sorted(di.items(),key=lambda x:x[1],reverse = True)
        for i in di:
            return i[0]