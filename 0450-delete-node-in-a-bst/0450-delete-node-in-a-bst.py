# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root and root.val==key and (not root.left) and (not root.right):
            root = None
            return root
        elif root and root.val==key and root.left and root.right==None:
            return root.left
        elif root and root.val==key and root.right and root.left==None:
            return root.right
        elif root and root.left and root.left.val==key:
            if root.left.right==None:
                root.left = root.left.left
                return root
            elif root.left.left == None:
                root.left = root.left.right
                return root
            elif root.left.left==None and root.left.right==None:
                root.left = None
                return root
        elif root and root.right and root.right.val == key:
            if root.right.right==None:
                root.right = root.right.left
                return root
            elif root.right.left == None:
                root.right = root.right.right
                return root
            elif root.right.right==None and root.right.left==None:
                root.right = None
                return root



        def getleast(root):
            while root:
                if not root.left:
                    return root.val
                root = root.left
        if root:
            if root.val>key:
                root.left = self.deleteNode(root.left,key)
            elif root.val<key:
                root.right = self.deleteNode(root.right,key)
            else:
                root.val = getleast(root.right)
                root.right = self.deleteNode(root.right,root.val)
        return root