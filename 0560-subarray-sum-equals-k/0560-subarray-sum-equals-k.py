class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums = list(itertools.accumulate(nums))
        ans = defaultdict(int)
        ans[0] = 1

        count = 0
        for i in nums:
            count += ans.get(i-k,0)
            ans[i] += 1
        print(ans)

        return count