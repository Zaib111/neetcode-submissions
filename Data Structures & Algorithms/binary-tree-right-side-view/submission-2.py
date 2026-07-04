# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, q = [], collections.deque([root])
        while q:
            rightmost = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightmost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightmost: res.append(rightmost)
        return res