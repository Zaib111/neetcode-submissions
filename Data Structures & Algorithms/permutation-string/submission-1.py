class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq_1, freq_2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            freq_1[ord(s1[i]) - ord('a')] += 1
            freq_2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            if freq_1[i] == freq_2[i]: matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            freq_2[ord(s2[l]) - ord('a')] -= 1
            if freq_2[ord(s2[l]) - ord('a')] == freq_1[ord(s2[l]) - ord('a')]:
                matches += 1
            elif freq_2[ord(s2[l]) - ord('a')] + 1 == freq_1[ord(s2[l]) - ord('a')]:
                matches -= 1
            l += 1

            freq_2[ord(s2[r]) - ord('a')] += 1
            if freq_2[ord(s2[r]) - ord('a')] == freq_1[ord(s2[r]) - ord('a')]:
                matches += 1
            elif freq_2[ord(s2[r]) - ord('a')] - 1 == freq_1[ord(s2[r]) - ord('a')]:
                matches -= 1
        return matches == 26