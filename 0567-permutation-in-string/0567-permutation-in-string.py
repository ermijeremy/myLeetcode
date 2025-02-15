class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        Window = Counter()
        s1_counter = Counter(s1)
        left = 0

        for right in range(len(s2)):
            Window[s2[right]] += 1

            while sum(Window.values()) > len(s1):
                Window[s2[left]] -= 1
                if Window[s2[left]] == 0:
                    del Window[s2[left]]
                left += 1

            if len(Window)==len(s1_counter) and len(s1_counter - Window)==0 :
                return True

        return False
