# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(cur):
            if not cur: return 0
            leftHeight, rightHeight = dfs(cur.left), dfs(cur.right)
            if abs(leftHeight - rightHeight) > 1: self.balanced = False
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return self.balanced