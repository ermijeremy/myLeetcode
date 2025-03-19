# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        temp = deque()
        temp.append(root)

        while temp:
            l = len(temp)

            temp1 = []

            for i in range(l):
                n = temp.popleft()
                
                if n:
                    temp1.append(n.val)
                    temp.append(n.left)
                    temp.append(n.right)
                
            if temp1:
                ans.append(temp1)
        return ans