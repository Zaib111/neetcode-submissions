class Solution:
    def isValid(self, s: str) -> bool:
        closed_to_open = {')': '(', '}': '{', ']': '[' }
        stack = []

        for char in s:
            if char in closed_to_open:
                if stack and stack[-1] == closed_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
