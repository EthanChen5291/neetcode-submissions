class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for n in nums]

        total = 1

        for i in range(1,len(nums)):
            total = total * nums[i - 1]
            output[i] *= total
        
        print(output)

        total = 1

        for i in reversed(range(0, len(nums) - 1)):
            total = total * nums[i + 1]
            output[i] *= total
        
        return output

            



            

            
