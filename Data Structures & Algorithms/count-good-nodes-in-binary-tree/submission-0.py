# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max_so_far):
            if root: 
                good = 1 if root.val >= max_so_far else 0
                max_so_far = max(max_so_far, root.val)
                return good + helper(root.left, max_so_far) + helper(root.right, max_so_far)
            
            return 0
        return helper(root, float("-inf"))