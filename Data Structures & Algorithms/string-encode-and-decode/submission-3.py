class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            for char in word:
                string += char
            string+='__&'
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        string = ''
        i = 0
        while i < len(s):
            if s[i] == '_' and s[i + 1] == '_' and s[i + 2] == '&':
                res.append(string)
                i += 3
                string = ''
            else:
                string += s[i]
                i += 1
        return res

