class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        res = 0
        adj = {i: [] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(i):
            visit.add(i)
            for j in adj[i]:
                if j not in visit:
                    dfs(j)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res