class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start):
            if len(path)==len(nums):
                if len(path)==len(set(path)):
                    ans.append(path.copy())
                return

            for candidate in nums:
                path.append(candidate)
                backtrack(candidate)
                path.pop()
        backtrack(0)
        return ans

