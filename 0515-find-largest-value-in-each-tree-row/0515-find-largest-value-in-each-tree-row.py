# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans =  []
        temp = []
        def bfs(root,level):
            if not root:
                return
            if len(temp)==level:
                temp.append([])
            temp[level].append(root.val)
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)

        for i in temp:
            ans.append(max(i))
        return ans