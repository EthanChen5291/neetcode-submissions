class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        left = 0
        right = len(nums) - 1
        middle = -1

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            target = -nums[i]
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1
                elif currentSum == target: # equals target
                    print(str(nums[left]) + " " + str(nums[right]))
                    
                    res.append([nums[left], nums[i], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return res
            
            
                




             
