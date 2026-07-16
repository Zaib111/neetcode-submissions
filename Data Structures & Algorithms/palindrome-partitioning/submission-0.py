class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, sublist):
            if i == len(s):
                res.append(sublist.copy())
                return
            for k in range(i, len(s)):
                if self.isPalindrome(s, i, k):
                    sublist.append(s[i:k + 1])
                    dfs(k + 1, sublist)
                    sublist.pop()

        dfs(0, [])
        return res
    
    def isPalindrome(self, s: str, i: int, k: int):
        while i <= k:
            if s[i] != s[k]: return False
            i, k = i + 1, k - 1
        return True