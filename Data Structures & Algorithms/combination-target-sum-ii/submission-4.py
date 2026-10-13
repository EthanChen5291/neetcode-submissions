class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # duplicates -> index


        # unique
        # subsets of target case == target
        # base case > target

        # start idx -> backtrack(start+1, curr, currSum)

        res = []
        candidates.sort()

        def backtrack(start: int, curr: List[int], currSum: int) -> None:
            nonlocal res

            if currSum == target:
                res.append(curr.copy())
                return
            
            # [2, 2, 2]
            
            if currSum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                curr.append(candidates[i])
                currSum += candidates[i]

                backtrack(i+1, curr, currSum)

                curr.pop()
                currSum -= candidates[i]
            
            return

        backtrack(0, [], 0)
        return res

