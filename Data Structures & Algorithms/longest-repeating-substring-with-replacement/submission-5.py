class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        substring_len = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            substring_len = max(substring_len, r - l + 1)
            r += 1
        return substring_len