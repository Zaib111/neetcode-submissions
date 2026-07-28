class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        edgeMap = {i: [] for i in range(n)}
        for v1, v2 in edges:
            edgeMap[v1].append(v2)
            edgeMap[v2].append(v1)
        
        visit = set()
        def dfs(cur, prev):
            if cur in visit:
                return False
            visit.add(cur)
            for nei in edgeMap[cur]:
                if nei != prev and not dfs(nei, cur): return False
            return True
        
        return dfs(0, -1) and n == len(visit)