class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = [False] * len(nums)
        perm = []
        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for i in range(len(nums)):
                if not seen[i]:
                    perm.append(nums[i])
                    seen[i] = True
                    dfs()
                    perm.pop()
                    seen[i] = False
        
        dfs()
        return res