# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def recur(root):
            if not root:
                return
            temp = []
            def bfs(root):
                nonlocal ans
                if not root:
                    return
                temp.append(root.val)
                bfs(root.left)
                bfs(root.right)
                if (p.val in temp) and (q.val in temp):
                    ans = root
            bfs(root)
            recur(root.left)
            recur(root.right)
        recur(root)

        return ans

            