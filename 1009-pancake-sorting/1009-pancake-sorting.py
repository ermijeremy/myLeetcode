class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        mm = sorted(arr, reverse = True)
        n = len(arr)
        t = n
        for i in range(1,n):
            j = i-1
            m = mm[j]
            if m != arr[n-i]:
                k = arr.index(m)
                ans.append(k+1)
                arr[:k+1] = reversed(arr[:k+1])
                ans.append(t)
                arr[:n-i+1] = reversed(arr[:n-i+1])
            t-=1
        return ans