class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(int(a) + int(b))
                elif token == '-':
                    stack.append(int(a) - int(b))
                elif token == '*':
                    stack.append(int(a) * int(b))
                else:
                    stack.append(int(a) / int(b))
            else:
                stack.append(token)
        return int(stack[0])