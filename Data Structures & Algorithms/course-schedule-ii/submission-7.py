class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i, j in prerequisites:
            adj[i].append(j)
        visiting = set()
        visited = set()
        res = []

        def dfs(i):
            if i in visiting:
                return False
            if not adj[i]:
                if i not in visited: res.append(i)
                visited.add(i)
                return True
            visiting.add(i)
            for j in adj[i]:
                if not dfs(j): return False
            visiting.remove(i)
            res.append(i)
            visited.add(i)
            adj[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res