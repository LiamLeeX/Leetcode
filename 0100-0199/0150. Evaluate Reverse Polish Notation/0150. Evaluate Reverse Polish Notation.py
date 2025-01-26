class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operators[token](num1, num2))
            else:
                stack.append(int(token))
        return stack[0]