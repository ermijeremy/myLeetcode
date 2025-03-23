class Solution:
    def getRow(self, r: int) -> List[int]:
        if r==0:
            return [1]
        ans = []
        self.r = r

        def recur(arr):
            temp = [1]
            if len(arr)==self.r+1:
                ans.extend(arr.copy())
                return
            l,r = 0,len(arr)-1
            while l<r:
                temp.append(arr[l]+arr[l+1])
                l += 1
            temp.append(1)
            recur(temp)
        recur([1,1])
        return ans