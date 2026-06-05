class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        def makeNumberDict(nums: list[int]) -> dict:
            numberDict = {}

            for i, n in enumerate(nums): 
                if n in numberDict:
                    numberDict[n].append(i)
                else:
                    numberDict[n] = [i]
            
            return numberDict

        numberDict = makeNumberDict(nums)

        for i in range(0, len(nums)):
            secondNum = (target - nums[i])

            if secondNum in numberDict:
                for k in range(0, len(numberDict[secondNum])):
                    candidate = numberDict[secondNum][k]
                    if candidate != i:
                        return [i, candidate] if i < candidate else [candidate, i]
            
        return False
        

        

