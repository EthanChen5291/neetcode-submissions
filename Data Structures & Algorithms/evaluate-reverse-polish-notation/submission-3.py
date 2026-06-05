class Solution:
    def evalRPN(self, tokens: List[str]) -> int:       
        l = len(tokens)
        stack = []
        
        for t in tokens:
            if self.isOperator(t):
                b = stack.pop()
                a = stack.pop()
                stack.append(self.applyOperator(a, t, b))
            else:
                stack.append(int(t))

        return stack[0]
            

    def isOperator(self, op: str) -> bool:
        if op == "*" or op == "-" or op == "+" or op == "/":
            return True
        
        return False

    def applyOperator(self, num1: str, op: str, num2: str) -> int:
        a = int(num1)
        b = int(num2)

        if op == "-":
            return a - b
        elif op == "+":
            return a + b
        elif op == "/" and b != 0:
            return int(a / b)
        elif op == "*":
            return a * b
            
        