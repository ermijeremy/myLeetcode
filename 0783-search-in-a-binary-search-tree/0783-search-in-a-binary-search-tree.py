# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None
        def recur(root):
            nonlocal ans
            if root:
                if root.val>val:
                    recur(root.left)
                elif root.val<val:
                    recur(root.right)
                else:
                    ans = root
            return ans
        return recur(root)