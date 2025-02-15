class Solution:
    def punishmentNumber(self, n: int) -> int:
        li = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        i = 0
        ans = 0

        while i < len(li) and li[i] <= n:
            ans += li[i]**2
            i += 1
        
        return ans