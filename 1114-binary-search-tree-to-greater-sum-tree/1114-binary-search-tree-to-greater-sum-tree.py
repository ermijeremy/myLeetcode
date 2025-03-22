# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = 0

        def recur(root):
            if not root:
                return
            recur(root.right)
            self.ans += root.val
            root.val = self.ans
            recur(root.left)
        recur(root)
        return root