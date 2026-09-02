class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = [0] * 26
        l = 0
        maxf = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord("A")] += 1
            maxf = max(freq[ord(s[r]) - ord("A")], maxf)
            if r - l + 1 - maxf <= k:
                res = max(res, r - l + 1)
            else:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
        return res