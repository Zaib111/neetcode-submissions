class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [0, -1] # [string, l, r]

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_l, cur_r = res
                if r - l > cur_r - cur_l:
                    res = [l, r]
                l, r = l - 1, r + 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_l, cur_r = res
                if r - l > cur_r - cur_l:
                    res = [l, r]
                l, r = l - 1, r + 1

        l, r = res
        return s[l: r + 1]