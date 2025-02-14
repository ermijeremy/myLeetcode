class Solution:
    def minWindow(self, s: str, t: str) -> str:
        di = Counter(t)

        min_len = float('inf')
        window = Counter()
        left = 0
        l = 0


        for right in range(len(s)):
            window[s[right]] += 1
            
            while len(di - window) == 0 :
                
                if right - left + 1 < min_len:
                    l = left
                    min_len  = right - left + 1

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        if min_len == float('inf'):
            return ""
        return s[l:l+int(min_len)]