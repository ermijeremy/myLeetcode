class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        
        e_o = defaultdict(int)
        o_z = {0:0,1:0}

        for i in arr:
            if i % 2 == 0:
                e_o[0] += 1
                o_z[0] += e_o[1]
            else:
                e_o[1] += 1
                o_z[1] += (1 + e_o[0])
        ans = sum(o_z.values())

        return ans%(10**9 + 7)