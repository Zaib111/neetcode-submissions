class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return []
            if preMap[crs] == []:
                if crs not in res:
                    res.append(crs)
                return
            
            visited.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == []: return []
            res.append(crs)
            visited.remove(crs)
            preMap[crs] = []
        
        for crs in range(numCourses):
            if crs not in res and dfs(crs) == []: return []
        return res
            