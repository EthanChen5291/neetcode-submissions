class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if self.isOpeningParens(c):
                stack.append(c)
            else:
                if stack: 
                    last = stack.pop()
                    if self.isClosingParens(last, c):
                        continue
                    else:
                        return False
                else:
                    return False
        
        return True if not stack else False
            

    
    def isOpeningParens(self, s: str) -> bool:
        return (s in ['[','{', '('])

    def isClosingParens(self, opening: str, closing: str) -> bool:
        if opening == '[':
            return (closing == ']')
        elif opening == '(':
            return (closing == ')')
        if opening == '{':
            return (closing == '}')