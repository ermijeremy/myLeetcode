class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        di = Counter(candies)

        def binary(arr, target, di):
            ans, left, right = 0, 0, max(arr)
            while left <= right:
                mid = (left + right + 1)// 2
                have = 0
                for i,j in di.items():
                    have += (i//mid)*(j)
                if have >= target:
                    ans = max(mid,ans)
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        return binary(candies,k,di)