class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        window = defaultdict(int)
        left = 0
        maxx = 0

        for right in range(len(s)):
            window[s[right]] += 1

            maxx = max(maxx, window[s[right]])

            while (right - left + 1) - maxx > k:

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans
