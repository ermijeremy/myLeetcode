class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        diF = Counter(first)
        diS = Counter(second)
        diT = Counter(third)

        ans = []
        for i in words:
            temp = Counter(set(i.lower()))
            print(temp)
            if not (temp-diF and temp-diS and temp-diT):
                ans.append(i)
        return ans
            