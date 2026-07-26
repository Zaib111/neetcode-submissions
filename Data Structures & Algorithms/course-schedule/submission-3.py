class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(crs, visited):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre, visited):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs, set()): return False
        return True