class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) // 2
        def dfs(i, res):
            nonlocal total
            if i == len(nums):
                return res == total
            if res > total:
                return False
            return dfs(i + 1, res + nums[i]) or dfs(i + 1, res)
            
            
        if sum(nums) % 2 == 1: return False
        return dfs(0, 0)