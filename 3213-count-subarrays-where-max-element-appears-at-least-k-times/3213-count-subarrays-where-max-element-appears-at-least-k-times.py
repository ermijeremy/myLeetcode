class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxno = max(nums)
        ind = []
        ans = 0
        window = defaultdict(list)
        left = 0

        for right in range(len(nums)):
            if nums[right]==maxno:
                if window[maxno]:
                    window[maxno][0] += 1
                    window[maxno][1] = min(window[maxno][1],right)
                else:
                    window[maxno].append(1)
                    window[maxno].append(right)
                    
            else:
                if window[nums[right]]:
                    window[nums[right]][0] += 1
                else:
                    window[nums[right]].append(1)

            while window[maxno] and window[maxno][0]>=k:
                ans += (len(nums)-right)
                window[nums[left]][0] -= 1
                left += 1
            
        return ans