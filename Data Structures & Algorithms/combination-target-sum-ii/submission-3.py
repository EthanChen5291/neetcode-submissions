class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # no duplicates 
        res = []
        candidates.sort()

        def backtrack(curr, remainder):
            total = sum(curr)
            
            if total == target:
                res.append(curr[:])
                return
                
            elif total > target:
                return
            
            for i, n in enumerate(remainder):
                if i > 0 and remainder[i] == remainder[i-1]:
                    continue

                curr.append(n)

                backtrack(curr, remainder[i+1:])

                curr.pop()
        
        backtrack([], candidates)
        return res