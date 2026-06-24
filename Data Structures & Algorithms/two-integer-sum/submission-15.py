class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenMap = {} # number -> index

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in seenMap:
                return [seenMap[compliment], i]
            
            seenMap[n] = i
        
        return []
