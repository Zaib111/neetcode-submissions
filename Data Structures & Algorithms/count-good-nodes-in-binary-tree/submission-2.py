# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(cur, max_val):
            if not cur: return
            if cur.val >= max_val:
                self.good += 1
                max_val = cur.val
            dfs(cur.left, max_val)
            dfs(cur.right, max_val)
        
        dfs(root, float("-inf"))
        return self.good