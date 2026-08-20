class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS, freqT = [0] * 26, [0] * 26
        if len(s) != len(t): return False
        for i in range(len(s)):
            freqS[ord(s[i]) - ord('a')] += 1
            freqT[ord(t[i]) - ord('a')] += 1
        return freqS == freqT