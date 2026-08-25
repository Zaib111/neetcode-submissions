class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for w in strs:
            res += str(len(w)) + "#" + w
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            word = ""
            for j in range(i + 1, i + 1 + length):
                word += s[j]
            res.append(word)
            i = i + 1 + length
        return res