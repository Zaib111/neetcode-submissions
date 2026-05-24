class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.upper() for char in s if char.isalnum()]
        i, j = 0, len(filtered) - 1
        while i < j:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1
        return True