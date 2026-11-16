class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "*"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = i
            while s[i] != "*":
                i += 1
            count = int(s[l:i])
            i += 1
            res.append(s[i: count + i])
            i = count + i
        return res