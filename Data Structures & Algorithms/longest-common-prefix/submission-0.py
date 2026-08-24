class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = float("inf")
        for w in strs:
            min_len = min(min_len, len(w))
        
        for i in range(min_len):
            res += strs[0][i]
            for w in strs:
                if w[i] != res[-1]:
                    return res[:-1]
        return res