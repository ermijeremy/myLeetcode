# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = []
        
        def recu(root, level):
            if not root:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            recu(root.left, level + 1)
            recu(root.right, level + 1)
        
        recu(root, 0)
        res = Counter(ans[-1])

        ans = None

        def recur(root):
            if not root:
                return
            temp = []
            def bfs(root):
                nonlocal ans,res
                if not root:
                    return
                temp.append(root.val)
                bfs(root.left)
                bfs(root.right)
                if len(res-Counter(temp))==0:
                    ans = root
            bfs(root)
            recur(root.left)
            recur(root.right)
        recur(root)

        return ans