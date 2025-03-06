class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:      
        di = {}
        stack = []
        n = len(nums2)-1
        ans = []
        for i in range(n,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
                di[nums2[i]] = -1
            if stack:
                di[nums2[i]] = stack[-1]
            else:
                di[nums2[i]] = -1
            stack.append(nums2[i])

        for i in nums1:
            ans.append(di[i])
        return ans
