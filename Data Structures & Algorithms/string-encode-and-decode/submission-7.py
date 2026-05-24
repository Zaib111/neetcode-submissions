class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            limit = ""
            while s[i] != "#":
                limit += s[i]
                i += 1
            limit = int(limit)
            temp_res = ""
            for j in range(i + 1, limit + i + 1):
                temp_res += s[j]
            res.append(temp_res)
            i += limit + 1
        return res