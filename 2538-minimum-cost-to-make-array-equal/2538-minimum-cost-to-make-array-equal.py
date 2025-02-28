class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        paired = zip(nums,cost)
        paired = list(map(list,sorted(paired,key = lambda x:x[0])))
        cost1 = copy.deepcopy(paired)

        for i in range(1,len(cost)):
            paired[i][1] += paired[i-1][1]

        ans = res = 0
        if paired[-1][1] % 2 == 0:
            target = (paired[-1][1]//2)
        else:
            target = math.ceil(paired[-1][1]/2)

        i = 0
        while paired[i][1] < target:
            i += 1

        ans = paired[i][0]
        for i in range(len(nums)):
            res += abs(paired[i][0]-ans)*cost1[i][1]

        return res