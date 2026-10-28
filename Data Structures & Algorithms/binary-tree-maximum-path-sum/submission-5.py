# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(cur):
            if not cur: return 0
            left_max = max(0, dfs(cur.left))
            right_max = max(0, dfs(cur.right))
            temp_sum = cur.val + max(left_max, right_max)
            self.res = max(cur.val + left_max + right_max, self.res)
            return temp_sum
        dfs(root)
        return self.res