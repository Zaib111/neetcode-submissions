class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        freq = {}
        freq[s[r]] = 1 + freq.get(s[r], 0)
        while r < len(s):
            size = r - l + 1
            if size - max(freq.values()) <= k:
                res = max(res, size)
                r += 1
                if r < len(s):
                    freq[s[r]] = 1 + freq.get(s[r], 0)
            else:
                freq[s[l]] -= 1
                l += 1
        
        return res