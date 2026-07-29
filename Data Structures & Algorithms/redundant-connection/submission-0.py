class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(i):
            if i != parent[i]:
                parent[i] = find(parent[i]) # i is not the representative
            return parent[i]
        
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2: return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for i, j in edges:
            if not union(i, j): return [i, j]