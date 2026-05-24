class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, count_window = {}, {}
        l = 0
        res, res_len = [-1, -1], float("infinity")
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        have, need = 0, len(count_t)

        for r in range(len(s)):
            count_window[s[r]] = 1 + count_window.get(s[r], 0)
            if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if res_len > r - l + 1:
                    res_len = r - l + 1
                    res = [l, r]
                
                count_window[s[l]] -= 1
                if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""