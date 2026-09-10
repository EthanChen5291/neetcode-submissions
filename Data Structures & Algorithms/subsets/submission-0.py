class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(curr, remaining):

            for i, n in enumerate(remaining):
                curr.append(n)

                res.append(curr[:])

                backtrack(curr, remaining[i+1:])

                curr.pop()
        
        backtrack([], nums)
        return res
