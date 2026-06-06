class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1, freq2 = [0] * 26, [0] * 26
        matches = 0
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[l]) - ord('a')
            freq2[index] -= 1
            if freq1[index] == freq2[index]:
                matches += 1
            elif freq2[index] == freq1[index] - 1:
                matches -= 1
            l += 1

            index = ord(s2[r]) - ord('a')
            freq2[index] += 1
            if freq1[index] == freq2[index]:
                matches += 1
            elif freq2[index] == 1 + freq1[index]:
                matches -= 1
        return matches == 26 # could be true on the last iteration 