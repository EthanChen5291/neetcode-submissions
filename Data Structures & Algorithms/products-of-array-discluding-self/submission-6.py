class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]
        
        multiplier = 1

        for i in range(1, len(output)): # left-side pass
            multiplier *= nums[i-1]
            output[i] *= multiplier
        
        multiplier = 1
        
        for i in reversed(range(0, len(output) - 1)):
            multiplier *= nums[i+1]
            output[i] *= multiplier
        
        return output


