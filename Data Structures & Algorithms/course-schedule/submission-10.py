class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)

        visiting = set()
        def dfs(i):
            if i in visiting:
                return False
            if not adj[i]: 
                return True
            visiting.add(i)
            for j in adj[i]:
                if not dfs(j): return False
            visiting.remove(i)
            adj[i] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i): return False
        return True