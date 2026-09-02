class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1
        l, r = 0, len(s1) - 1
        while r < len(s2) and freq1 != freq2:
            freq2[ord(s2[l]) - ord("a")] -= 1
            l += 1
            r += 1
            if r < len(s2):
                freq2[ord(s2[r]) - ord("a")] += 1

        if freq1 == freq2: return True
        return False