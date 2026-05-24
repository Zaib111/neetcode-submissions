class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in valid:
                if stack and stack[-1] == valid[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        return False