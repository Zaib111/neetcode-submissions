class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # populating/creating t map to track counts and creating window map
        if t == "":
            return ""
        
        window, count_t = {}, {}
        l = 0
        res, res_length = [-1, -1], float("infinity")
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        have, need = 0, len(count_t)
        
        for r in range(len(s)):
            if s[r] in count_t:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == count_t[s[r]]:
                    have += 1
            # Valid Window
            while have == need:
                # since we have a valid window, we are setting the minimum result length
                if res_length > r - l + 1:
                    res, res_length = [l, r], r - l + 1
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < count_t[s[l]]:
                        have -= 1
                l += 1
        l, r = res
        if res == [-1, -1]:
            return ""
        return s[l:r + 1]