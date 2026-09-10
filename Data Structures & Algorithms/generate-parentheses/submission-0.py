class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # numClosed <= numOpen at all times
        res = []

        def backtracking(curr, numOpen, numClosed):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            if numOpen > 0:
                curr.append("(")
                backtracking(curr, numOpen - 1, numClosed)
                curr.pop()
            
            if numClosed > numOpen:
                curr.append(")")
                backtracking(curr, numOpen, numClosed - 1)
                curr.pop()

        backtracking([], n, n)
        return res