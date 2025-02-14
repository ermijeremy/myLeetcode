class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        window = Counter()
        left = 0
        temp = Counter(p)

        for right in range(len(s)):
            window[s[right]] += 1

            while len(temp - window) == 0:
                if len(temp - window) == 0 and sum(window.values())==sum(temp.values()):
                    ans.append(right - len(p) + 1)
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
                
        return ans