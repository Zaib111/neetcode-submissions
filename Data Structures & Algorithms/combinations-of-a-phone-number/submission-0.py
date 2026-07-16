class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combination = []
        chars = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def dfs(i):
            if i == len(digits):
                res.append(''.join(combination))
                return
            possible_chars = chars[digits[i]]
            for char in possible_chars:
                combination.append(char)
                dfs(i + 1)
                combination.pop()
        dfs(0)
        if not digits: return []
        return res