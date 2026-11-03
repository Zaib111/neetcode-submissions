class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.cur_sum, self.combination, self.res = 0, [], []

        def dfs(i):
            if self.cur_sum == target:
                self.res.append(self.combination.copy())
                return
            elif self.cur_sum > target or i == len(nums):
                return
            
            # include and then go back to the same number
            self.combination.append(nums[i])
            self.cur_sum += nums[i]
            dfs(i)

            # exclude and then move to next number
            self.combination.pop()
            self.cur_sum -= nums[i]
            dfs(i + 1)
        dfs(0)
        return self.res