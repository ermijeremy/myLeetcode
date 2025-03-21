# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []

        def recur(root):
            if root:
                recur(root.left)
                ans.append(root.val)
                recur(root.right)
        recur(root)

        def build(arr):
            if not arr:
                return
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = build(arr[:mid])
            node.right = build(arr[mid+1:])
            return node
        return(build(ans))