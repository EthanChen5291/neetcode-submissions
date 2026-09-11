class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def getDigits(n):
            digitsMap = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }
            return digitsMap[n]

        # digit cannot be combined with its own chars
        if not digits:
            return []

        res = []

        def backtrack(curr, idx):
            if idx == len(digits):
                res.append("".join(curr))
                return
            
            chars = getDigits(digits[idx])
    
            for c in chars:
                curr.append(c)

                backtrack(curr, idx+1)

                curr.pop()
        
        backtrack([], 0)
        return res




