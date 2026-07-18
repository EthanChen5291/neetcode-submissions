class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if stack and not(self.isOpening(char)):
                if self.isMatching(stack[-1], char):
                    stack.pop()
                else:
                    return False
            elif self.isOpening(char):
                stack.append(char)
            else:
                return False
        
        return not(stack)


    def isOpening(self, s: str) -> bool:
        return (s == '[' or s == '{' or s == '(')

    def isMatching(self, s1: str, s2: str) -> bool:
        matches = (s1 == '[' and s2 == ']') or (s1 == '(' and s2 == ')') or (s1 == '{' and s2 == '}')

        return matches
        
 



