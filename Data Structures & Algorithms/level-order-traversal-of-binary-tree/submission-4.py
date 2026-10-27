# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            cur = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    cur.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if cur: res.append(cur)

        return res
