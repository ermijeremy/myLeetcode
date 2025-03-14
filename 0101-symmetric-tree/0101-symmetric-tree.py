# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = root.left
        right = root.right
        ans = []
        def recur(left,right):
            if left and right:
                ans.append([left.val,right.val])
                recur(left.left,right.right)
                recur(left.right,right.left)
            else:
                if left:
                    ans.append([left.val,right])
                elif right:
                    ans.append([left,right.val])
                else:
                    ans.append([left,right])
        recur(left,right)
        for i in ans:
            if i[0]!=i[1]:
                return False
        return True