class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur, open_num,  close_num):
            if len(cur) == 2 * n:
                if open_num == close_num:
                    res.append(cur)
                return
            cur += "("
            dfs(cur, open_num + 1, close_num)

            cur = cur[:-1]
            if close_num < open_num:
                cur += ")"
                dfs(cur, open_num, close_num + 1)
        dfs("", 0, 0)
        return res