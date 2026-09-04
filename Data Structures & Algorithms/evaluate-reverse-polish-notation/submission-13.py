class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for c in tokens:
            if c in operators:
                b, a = int(stack.pop()), int(stack.pop())
                if c == '+': stack.append(str(a + b))
                elif c == '-': stack.append(str(a - b))
                elif c == '*': stack.append(str(a * b))
                else: stack.append(str(int(a / b)))
            else:
                stack.append(c)
        return int(stack[0])
                    