class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for w in strs:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1
            res[tuple(freq)].append(w)
        return list(res.values())