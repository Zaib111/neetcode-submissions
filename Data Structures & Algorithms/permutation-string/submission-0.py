class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_1, freq_2 = [0] * 26, [0] * 26
        for c in s1:
            freq_1[ord(c) - ord('a')] += 1
        l, r = 0, 0
        while r < len(s1):
            freq_2[ord(s2[r]) - ord('a')] += 1
            r += 1
        if freq_1 == freq_2:
            return True
        # now r == len(s1) so we need to track this new character r is at
        while r < len(s2):
            freq_2[ord(s2[l]) - ord('a')] -= 1
            freq_2[ord(s2[r]) - ord('a')] += 1
            l, r = l + 1, r + 1
            if freq_1 == freq_2:
                return True
        return False