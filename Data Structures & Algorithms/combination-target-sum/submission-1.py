class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # subset
        # backtracking
        # no length requirement
        # == target requirement

        # no duplicates
        res = []

        def backtrack(start: int, curr: List[int], currSum: int):
            nonlocal res

            if currSum == target:
                res.append(curr.copy())
                return
            
            if currSum > target:
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                currSum += nums[i]

                backtrack(i, curr, currSum)

                curr.pop()
                currSum -= nums[i]
            
            return

        backtrack(0, [], 0)
        return res

        # if over target, reset


        