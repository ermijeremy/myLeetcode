# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        res = []
        def recur(root):
            nonlocal ans, res
            if root:
                res.append(root.val)
                recur(root.left)
                recur(root.right)
                if (not root.left) and (not root.right):
                    ans.append(res)
                    res = res[:-1]
                else:
                    res = res[:-1]
        recur(root)

        final = 0
        for i in ans:
            j = ''.join(map(str,i))
            final += int(j)

        return final