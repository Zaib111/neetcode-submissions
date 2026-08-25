class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {} # (i, res)
        total = sum(nums) // 2
        def dfs(i, res):
            nonlocal total
            if (i, res) in dp:
                return dp[(i, res)]
            if i == len(nums):
                dp[(i, res)] = res == total
                return res == total
            if res > total:
                dp[i] = False
                return False
            temp = dfs(i + 1, res + nums[i]) or dfs(i + 1, res)
            dp[(i, res)] = temp
            return temp
            
        if sum(nums) % 2 == 1: return False
        return dfs(0, 0)