# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(root, subroot):
            if not root and not subroot: return True
            if not root or not subroot or root.val != subroot.val: return False
            return isSame(root.left, subroot.left) and isSame(root.right, subroot.right)

        if not subRoot: return True
        if not root: return False
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)