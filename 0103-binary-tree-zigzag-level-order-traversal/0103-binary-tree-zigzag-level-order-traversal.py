# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def recur(root,turn,level):
            if not root:
                return
            if turn==1:
                if level == len(ans):
                    ans.append(deque([]))
                ans[level].append(root.val)
                recur(root.left,2, level + 1)
                recur(root.right,2, level + 1)
            else:
                if level == len(ans):
                    ans.append(deque([]))
                ans[level].appendleft(root.val)
                recur(root.left,1, level + 1)
                recur(root.right,1, level + 1)
        recur(root,1,0)
        ans = list(map(list,ans))
        return ans