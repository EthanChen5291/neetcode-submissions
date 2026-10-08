class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], leftover: List[int]):
            res.append(curr.copy())

            for i in range(len(leftover)):
                curr.append(leftover[i])

                backtrack(curr, leftover[i+1:])

                curr.pop()
        
        backtrack([], nums)
        return res

            