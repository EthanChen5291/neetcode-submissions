class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        def isOpening(c: str) -> bool:
            return (c in ['[', '(', '{'])

        def getClosing(c: str) -> bool:
            if c == '(':
                return ')'
            if c == '[':
                return ']'
            if c == '{':
                return '}'
        
        stack = []

        for char in s:
            if isOpening(char):
                stack.append(char)
            elif stack and char == getClosing(stack[-1]):
                stack.pop()
            else:
                return False
        
        return not stack
                

