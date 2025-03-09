class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        minn = nums[0]
        for i in nums:
            while stack and i > stack[-1][0]:
                stack.pop()

            if stack and stack[-1][0] > i and stack[-1][1] < i:
                    return True

            stack.append([i,minn])
            minn = min(i,minn)
        
        

        return False