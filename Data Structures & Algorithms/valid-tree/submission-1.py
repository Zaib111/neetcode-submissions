class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1: return False

        edgeMap = {i: [] for i in range(n)}
        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)
        
        cycle, visit = set(), set()
        def dfs(cur, prev):
            if cur in cycle:
                return False
            if cur in visit:
                return True
            cycle.add(cur)
            for neighbor in edgeMap[cur]:
                if neighbor != prev and not dfs(neighbor, cur): return False
            cycle.remove(cur)
            visit.add(cur)
            return True
        
        for i in range(n):
            if not dfs(i, -1): return False
        return True