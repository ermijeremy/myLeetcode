class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        # using this helper function i check if the given middle value can be a possible answer
        # i am gonna check that by counting the numbers of non adjecent houses that have money less than or equal to the given middle value, ( because the given middle value could possibly be the answer if all other non adjecent houses have less than or equal to the middle value)
        def valid(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i]<=cap:
                    i += 2      # increasing the pointer by to inorder to get the next non adjecent house
                    count += 1
                else:
                    i += 1
            return count>=k

        # this solution is a pure binary search but the variant is we are looking for a specific targer, rather we are looking for a range value
        # this range is where we get and minimize our capability

        left, right = min(nums), max(nums)
        ans = 0

        while left <= right:
            mid = (left+right)//2

            if valid(mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans

