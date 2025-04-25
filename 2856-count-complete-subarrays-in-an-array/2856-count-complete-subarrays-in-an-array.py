class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        ans1 = 0
        left = 0
        window = defaultdict(int)
        n = len(nums)

        # getting the number of substrings which have at most k distnict elements

        for right in range(n):
            window[nums[right]] += 1
            
            while len(window) > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

            ans1 += right - left + 1

        ans2 = 0
        left1 = 0
        window1 = defaultdict(int)
        n1 = len(nums)

        # getting the number of substrings which have at most k-1 distinct elements

        for right1 in range(n1):
            window1[nums[right1]] += 1
            
            while len(window1) > k-1:
                window1[nums[left1]] -= 1
                if window1[nums[left1]] == 0:
                    del window1[nums[left1]]
                left1 += 1

            ans2 += right1 - left1 + 1

        return ans1 - ans2  # at most k distinct elements - at most k-1 ditnict elements == exactly k elements 