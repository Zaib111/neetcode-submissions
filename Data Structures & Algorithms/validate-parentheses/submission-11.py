class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in pairs:
                if not stack or (stack and stack[-1] != pairs[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack