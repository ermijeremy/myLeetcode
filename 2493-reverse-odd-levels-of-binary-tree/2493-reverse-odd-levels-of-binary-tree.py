# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans =  []
        temp = []
        def bfs(root,level):
            if not root:
                return
            if len(temp)==level:
                temp.append([])
                ans.append([])
            if level%2:
                temp[level].append(root)
                ans[level].append(root.val)
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)
        for i in range(len(ans)):
            ans[i] = list(reversed(ans[i]))
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                temp[i][j].val = ans[i][j]
        return root