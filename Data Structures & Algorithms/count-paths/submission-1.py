class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {(m - 1, n - 1): 1}
        def dfs(r, c):
            res = 0
            if (r, c) in dp:
                return dp[(r, c)]
            if r + 1 < m:
                res = dfs(r + 1, c)
            if c + 1 < n:
                res += dfs(r, c + 1)
            dp[(r, c)] = res
            return res

        return dfs(0, 0)