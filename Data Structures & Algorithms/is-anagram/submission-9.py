class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_s = {}
        res_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            res_s[s[i]] = 1 + res_s.get(s[i], 0)
            res_t[t[i]] = 1 + res_t.get(t[i], 0)
        return res_s == res_t
      