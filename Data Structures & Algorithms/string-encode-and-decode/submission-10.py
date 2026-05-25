class Solution:

    def encode(self, strs: List[str]) -> str:
        # since the length doesnt have to be single digit, we should denote the end of the length with a special character
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        count = ""
        i = 0
        while i < len(s):
            while s[i] != '#':
                count += s[i]
                i += 1
            i += 1
            res.append(s[i: i + int(count)])
            i += int(count)
            count = ""
        return res