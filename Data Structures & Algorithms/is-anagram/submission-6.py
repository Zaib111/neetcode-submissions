class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        for c in s:
            if c in counts_s:
                counts_s[c] += 1
            else:
                counts_s[c] = 1
        counts_t = {}
        for c in t:
            if c in counts_t:
                counts_t[c] += 1
            else:
                counts_t[c] = 1
        return counts_s == counts_t
