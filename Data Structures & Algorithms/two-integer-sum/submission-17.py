class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in indexMap:
                return [indexMap[compliment], i]
            
            indexMap[n] = i


