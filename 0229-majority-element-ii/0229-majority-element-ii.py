class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        di = sorted(Counter(nums).items(),key=lambda x:x[1],reverse = True)
        for i in di:
            if i[1]>len(nums)/3:
                ans.append(i[0])
            else:
                return ans
        return ans