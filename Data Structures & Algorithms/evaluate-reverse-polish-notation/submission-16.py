class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(x, y, op):
            x = int(x)
            y = int(y)

            if op == '*':
                return x * y
            elif op == '/':
                return x / y
            elif op == '+':
                return x + y
            elif op == '-':
                return x - y
        
        def isOperand(op) -> bool:
            return op in ['/','+','-','*']

        acc = None
        stack = []

        for t in tokens:
            if stack and isOperand(t):
                b = stack.pop()
                a = stack.pop()

                stack.append(calculate(a, b, t))
            else:
                stack.append(t)
        
        return int(stack[0])
        
