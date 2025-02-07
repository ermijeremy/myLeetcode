class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        even_sum = (sum([i for i in nums if i%2==0]))
        print(even_sum)

        for i in range(len(queries)):
            old = nums[queries[i][1]]
            nums[queries[i][1]] = queries[i][0] + nums[queries[i][1]]
            new = nums[queries[i][1]]
            if old % 2 == 0 and new % 2 == 0:
                even_sum = (new-old)+even_sum
                res.append(even_sum)
            elif old % 2!= 0 and new % 2 == 0:
                even_sum = even_sum + new
                res.append(even_sum)
            elif old % 2 == 0 and new % 2 != 0:
                even_sum = even_sum - old
                res.append(even_sum)
            else:
                res.append(even_sum)

        return res
