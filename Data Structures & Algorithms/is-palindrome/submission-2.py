class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char
        i, j = 0, len(new_s) - 1
        while i < j:
            if new_s[i].upper() != new_s[j].upper():
                return False
            i += 1
            j -= 1
        return True