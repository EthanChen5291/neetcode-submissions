class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if self.isOperand(t):
                elt2 = stack.pop()
                elt1 = stack.pop()

                stack.append(self.applyOp(elt1, elt2, t))
            else:
                stack.append(int(t))
        
        return stack.pop()

        # add numbers to stack
    
    def isOperand(self, op: str) -> bool:
        return (op in ['*', '+', '-', '/'])
    
    def applyOp(self, num1: str, num2: str, op: str) -> int:
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        elif op == '*':
            return num1*num2
        elif op == '/': 
            return int(num1/num2)