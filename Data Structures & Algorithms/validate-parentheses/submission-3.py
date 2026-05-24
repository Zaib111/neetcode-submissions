class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in closing and len(stack) > 0:
                if closing[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(char)
        if stack != []:
            return False
        return True