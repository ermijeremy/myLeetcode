class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visit = defaultdict(int)

        def recur(left,right,turn):
            if left > right:
                return 0
            if (left,right,turn) in visit:
                return visit[(left,right,turn)]
            res = 0
            if turn==1:
                print(right)
                res = max((nums[left]+recur(left+1,right,2)),nums[right]+recur(left,right-1,2))
            else:
                res = min(recur(left+1,right,1),recur(left,right-1,1))
            visit[(left,right,turn)] = res
            return res

        return sum(nums)-recur(0,len(nums)-1,1)<=recur(0,len(nums)-1,1)