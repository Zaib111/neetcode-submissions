class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = [0] * 26
        l = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord("A")] += 1
            if r - l + 1 - max(freq) <= k:
                res = max(res, r - l + 1)
            else:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
        return res