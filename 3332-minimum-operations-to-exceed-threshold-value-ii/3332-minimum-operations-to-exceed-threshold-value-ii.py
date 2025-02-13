class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        heapq.heapify(nums)
        m = nums[0]
        while m < k:
            if n < 2:
                return count

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, x*2+y)
            
            count+=1
            m = nums[0]

            

        return count