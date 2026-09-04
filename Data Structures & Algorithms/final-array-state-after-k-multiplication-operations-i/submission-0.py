class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # find FIRST minimum

        # minimum * x
        currMin = float('inf') # get minimum

        for i in range(k):
            minIdx = nums.index(min(nums))
            nums[minIdx] *= multiplier
        
        return nums