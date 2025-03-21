# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = defaultdict(int)

        id = 0
        def recur(root):
            nonlocal id
            id += 1
            if not root:
                return
            ans = root.val
            temp = 0
            count = 0
            def bfs(root):
                nonlocal ans,res,temp,count,id
                if not root:
                    return
                count += 1
                temp += root.val
                bfs(root.left)
                bfs(root.right)
                res[(ans,id)] = temp//count
            bfs(root)
            recur(root.left)
            recur(root.right)
        recur(root)
        final = 0

        for i,j in res.items():
            a,b = i
            if a==j:
                final += 1
        return final