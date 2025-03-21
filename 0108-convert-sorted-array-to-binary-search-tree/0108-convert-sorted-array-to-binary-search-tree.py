# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[len(nums)//2])
        small = nums[:len(nums)//2]
        bigger = nums[len(nums)//2+1:]
        
        def recur(root,small,bigger):
            if not root:
                return
            mid = len(small)//2
            mid1 = len(bigger)//2
            if len(small)==1:
                mid = 0
            if mid >= len(small):
                mid -= 1
            if len(bigger)==1:
                mid1 = 0
            if mid1 >= len(bigger):
                mid1 -= 1
            if mid < len(small) and mid >= 0:
                root.left = TreeNode(small[mid])
                small.pop(mid)
            if mid1 < len(bigger) and mid1 >= 0:
                root.right = TreeNode(bigger[mid1])
                bigger.pop(mid1)
            
            recur(root.left,small[:mid],small[mid:])
            recur(root.right,bigger[:mid1],bigger[mid1:])
        recur(root,small,bigger)
        return root