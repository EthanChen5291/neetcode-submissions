class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # find subset with extra condition
        # can add back in, doesnt have to remove n to backtrack

        def backtrack(curr, remainder):
            total = 0
            for n in curr:
                total += n
            
            if total == target:
                res.append(curr[:])
                return
            elif total > target:
                return

            for i, n in enumerate(remainder):
                curr.append(n)

                backtrack(curr, remainder[i:])

                curr.pop()
            
        backtrack([], nums)

        return res