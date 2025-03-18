# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:


        def recur(root,minn,maxx):
            if not root:
                return maxx-minn
            minn = min(minn,root.val)
            maxx = max(maxx,root.val)
            x = recur(root.left, minn, maxx)
            y = recur(root.right,minn, maxx)
            return max(x,y)

        return recur(root,float('inf'),float('-inf'))