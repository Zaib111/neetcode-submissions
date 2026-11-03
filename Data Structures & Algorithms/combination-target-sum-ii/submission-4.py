class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        res, cur, comb = [], 0, []

        def dfs(i):
            nonlocal cur
            if cur == target:
                res.append(comb.copy())
                return
            if cur > target or i == len(nums):
                return
            
            # include cur num
            cur += nums[i]
            comb.append(nums[i])
            dfs(i + 1)

            # exclude cur num
            cur -= nums[i]
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
 
        dfs(0)
        return res