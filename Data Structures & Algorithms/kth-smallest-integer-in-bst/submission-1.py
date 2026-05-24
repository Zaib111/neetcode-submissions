# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

        # def inOrderTraversal(root):
        #     if not root:
        #         return []
        #     else:
        #         return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
        # res = inOrderTraversal(root)
        # return res[k - 1]