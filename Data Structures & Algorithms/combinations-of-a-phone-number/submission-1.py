class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(i, comb):
            if i == len(digits):
                res.append(comb)
                return
            chars = digits_to_chars[digits[i]]
            for c in chars:
                dfs(i + 1, comb + c)
        dfs(0, "")
        if not digits: return []
        return res