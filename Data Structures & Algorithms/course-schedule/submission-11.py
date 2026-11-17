class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = defaultdict(list)
        for i, j in prerequisites:
            pre_map[i].append(j)
        
        visiting = set()
        def dfs(i):
            if not pre_map[i]: return True
            if i in visiting: return False
            visiting.add(i)
            for j in pre_map[i]:
                if not dfs(j): return False
            visiting.remove(i)
            pre_map[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True