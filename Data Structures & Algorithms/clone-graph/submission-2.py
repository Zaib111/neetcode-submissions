"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        old_to_new = {node: Node(node.val, [])}

        def dfs(node):
            if node not in old_to_new:
                old_to_new[node] = Node(node.val, [])
            clone = old_to_new[node]
            for neighbor in node.neighbors:
                if neighbor not in old_to_new:
                    dfs(neighbor)
                clone.neighbors.append(old_to_new[neighbor])
        dfs(node)
        return old_to_new[node]