class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()


        def backtrack(curr, remainder):


            for i in range(len(remainder)):
                if i > 0 and remainder[i] == remainder[i-1]:
                    continue

                curr.append(remainder[i])

                res.append(curr[:])

                backtrack(curr, remainder[i+1:])

                curr.pop()
        
        backtrack([], nums)
        return res
