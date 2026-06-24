class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]

        product = 1

        for i in range(1, len(nums)):
            product *= nums[i-1]

            output[i] *= product

        product = 1

        for i in reversed(range(0, len(nums) - 1)):
            product *= nums[i+1]

            output[i] *= product

        return output

            

            
