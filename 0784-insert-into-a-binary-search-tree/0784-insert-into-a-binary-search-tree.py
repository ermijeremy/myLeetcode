# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        val = TreeNode(val)
        ans = []
        def recur(root):
            if root:
                if root.val>val.val:
                    recur(root.left)
                elif root.val<val.val:
                    recur(root.right)
                ans.append(root)
        recur(root)
        if ans:
            ans = ans[0]
            if ans.val>val.val:
                ans.left = val
            else:
                ans.right = val
            return root
        else:
            return val