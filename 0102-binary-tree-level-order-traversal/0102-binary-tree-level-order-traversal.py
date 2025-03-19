# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def recur(root, level):
            if not root:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            recur(root.left, level + 1)
            recur(root.right, level + 1)
        
        recur(root, 0)
        return ans