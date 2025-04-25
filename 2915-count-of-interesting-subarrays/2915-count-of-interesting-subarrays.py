class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%modulo == k:
                nums[i] = 1
            else:
                nums[i] = 0

        count = 0
        prefix_sum = 0
        mod_counts = defaultdict(int)
        mod_counts[0] = 1

        for num in nums:
            prefix_sum += num
            current_mod = prefix_sum % modulo
            target_mod = (current_mod - k) % modulo
            count += mod_counts[target_mod]
            mod_counts[current_mod] += 1
        
        return count