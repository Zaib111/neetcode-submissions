# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        self.heights = {None: 0}

        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.heights[root] = 1 + max(left, right)
            return self.heights[root]
        
        dfs(root)
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node and abs(self.heights[node.left] - self.heights[node.right]) > 1:
                return False
            if node:
                stack.append(node.left)
                stack.append(node.right)
        return True