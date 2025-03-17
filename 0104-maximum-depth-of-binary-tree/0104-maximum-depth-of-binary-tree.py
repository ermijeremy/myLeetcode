# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def recur(root,ans):
            if root:
                ans = 1 + max(recur(root.right,ans),recur(root.left,ans))
            return ans
        return recur(root,ans)
