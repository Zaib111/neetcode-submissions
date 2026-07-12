class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, currSum):
            if currSum == target:
                res.append(subset.copy())
                return
            if i == len(nums) or currSum > target:
                return

            subset.append(nums[i])
            currSum += nums[i]
            dfs(i, currSum)

            subset.pop()
            currSum -= nums[i]
            dfs(i + 1, currSum)


        dfs(0, 0)
        return res