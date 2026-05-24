class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_res, t_res = {}, {}
        for i in range(len(s)):
            s_res[s[i]] = 1 + s_res.get(s[i], 0)
            t_res[t[i]] = 1 + t_res.get(t[i], 0)
        return s_res == t_res
        