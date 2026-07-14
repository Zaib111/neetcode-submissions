class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, subset, cur):
            if cur == target:
                res.append(subset.copy())
                return
            if cur > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, cur + candidates[i])

            subset.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset, cur)
        dfs(0, [], 0)
        return res