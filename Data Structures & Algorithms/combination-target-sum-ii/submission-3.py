class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, sublist, cur):
            if cur == target:
                res.append(sublist.copy())
                return
            if i == len(candidates) or cur > target:
                return
            
            sublist.append(candidates[i])
            dfs(i + 1, sublist, cur + candidates[i])

            sublist.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sublist, cur)
        dfs(0, [], 0)
        return res