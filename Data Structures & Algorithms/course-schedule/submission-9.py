class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)

        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if not adj[i]: 
                return True
            visited.add(i)
            for j in adj[i]:
                if not dfs(j): return False
            visited.remove(i)
            adj[i] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i): return False
        return True