class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        self.t = []
        self.check = False

        def backtrack(idx,num,l,ta):
            if self.t and str(num[l-1]) in str(self.t[-1]) and sum(self.t)==ta:
                self.check = True
            if sum(self.t)>ta:
                return

            for i in range(idx,l):
                if self.check:
                    return
                self.t.append(int(num[idx:i+1]))
                backtrack(i+1,num,l,ta)
                self.t.pop()
        # # backtrack(0,'1296',4,37)
        for i in range(1,n+1):
            cur = str(i*i)
            backtrack(0,cur,len(cur),i)
            if self.check:
                self.check = False
                print(i)
                ans += i*i
        return ans
