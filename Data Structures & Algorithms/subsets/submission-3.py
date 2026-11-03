class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.cur = []
        def dfs(i):
            if i == len(nums):
                self.res.append(self.cur.copy())
                return
            self.cur.append(nums[i])
            dfs(i + 1)
            self.cur.pop()
            dfs(i + 1)

        dfs(0)
            
        return self.res
