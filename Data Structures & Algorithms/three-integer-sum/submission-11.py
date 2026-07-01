class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums) - 1

            compliment = -(n)

            while left < right:
                twoSum = nums[left] + nums[right]

                if twoSum < compliment:
                    left += 1
                elif twoSum > compliment:
                    right -= 1
                else:
                    res.append([nums[left], nums[right], nums[i]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res
            



