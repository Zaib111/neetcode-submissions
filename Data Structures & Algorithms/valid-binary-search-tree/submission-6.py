# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(cur, leftBound, rightBound):
            if not cur: return True
            if leftBound < cur.val < rightBound:
                return dfs(cur.left, leftBound, cur.val) and dfs(cur.right, cur.val, rightBound)
            return False
        return dfs(root, float("-inf"), float("inf"))