class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for tok in tokens:
            if self.isOperator(tok):
                n2 = nums.pop()
                n1 = nums.pop()

                res = self.calculate(n1, n2, tok)
                nums.append(res)
            else:
                nums.append(int(tok))
        
        return nums[0]

    
    def isOperator(self, op: str) -> bool:
        return (op in ['-', '+', '*', '/'])

    def calculate(self, num1: int, num2: int, op: str) -> int:
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        elif op == '/':
            return int(num1/num2)
        elif op == '*':
            return num1*num2