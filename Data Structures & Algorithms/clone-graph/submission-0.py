"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToClone = {}
        def dfs(node):
            if node in nodeToClone:
                return
            nodeToClone[node] = Node(node.val, [])
            for neighbor in node.neighbors:
                dfs(neighbor)
                nodeToClone[node].neighbors.append(nodeToClone[neighbor])

        if not node: return
        dfs(node)
        return nodeToClone[node]